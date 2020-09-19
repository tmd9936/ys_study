# pip install flask-pymongo

from flask import Flask
from flask import request, render_template
from flask_pymongo import PyMongo
from datetime import datetime, timedelta
from bson.objectid import ObjectId
from flask import abort, redirect, url_for, flash
from flask import session
from functools import wraps
import time
import math

def login_required(f):
    @wraps(f)
    def decorated_func(*args, **kwargs):
        if session.get("id") is None or session.get("id") == "":
            # request.url 현재 url을 의미함
            return redirect(url_for("member_login", 
                                next_url=request.url))
        return f(*args, **kwargs)
    return decorated_func

app = Flask(__name__)
# myweb 데이터베이스명 생성, 있으면 그냥 연결
app.config["MONGO_URI"] = "mongodb://localhost:27017/myweb"

# 30분 동안 session 유지되는 환경설정(30분간 아무반응이 없으면 session값은 사라짐)
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=30)
# flash를 사용하게되면 SECRET_KEY를 사용해야한다.
app.config["SECRET_KEY"] = "some_key"

mongo = PyMongo(app)

@app.route("/logout", methods=["GET"])
def logout():
    session.clear()
    return redirect(url_for("list"))

######################################
# flask에서 사용하는 template filter
@app.template_filter("datetime_format")
def datetime_format(value):
    if value is None:
        return ""

    # 클라이언트의 현재 시스템의 local 타임 (컴퓨터의 시간)
    now_timestamp = time.time()

    # datetime 객체에는 fromtimestamp, utcfromtimestaop 함수가 있다.

    # fromtimestamp를 이용하면 클라이언트의 시간을 기준으로
    # datetime 객체를 만들어 준다.
    # 클라이언트의 local 타임을 datetime형식으로 만들어서 표현해줌
    print(datetime.fromtimestamp(now_timestamp))

    # utcfromtimestamp는 UTC datetime을 리턴한다.
    # db에 저장된 UTC format
    print(datetime.utcfromtimestamp(now_timestamp))

    # 클라이언트의 현재 datetime형식의 시간 - 현재 datetime형식의 UTC 시간
    offset_time = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    print("offset_time : ", offset_time)

    # value는 db에 저장되어 있는 timestamp형식의 utc타임
    # value를 datetime 객체로 만든후 시간차를 더해줌
    value = datetime.fromtimestamp((int(value) / 1000)) + offset_time

    return value.strftime("%Y-%m-%d %H:%M:%S")

@app.route("/list")
def list():
    # 페이지 값
    # page 매개변수가 없을 경우 기본값을 1로
    page = request.args.get("page", default=1, type=int)

    # 한페이지당 몇개의 게시글을 출력 할 지를 받아옴.(인자로 받아와서 처리함)
    limit = request.args.get("limit", 10, type=int)

    # search 변수의 기본값을 -1로 설정
    search = request.args.get("search", -1, type=int)

    # 기본값이 없는 문자열로 받아옴
    keyword = request.args.get("keyword", type=str)

    # 최종 쿼리를 완성해서 보내는 객체
    query = {}

    # 검색어를 추가할 리스트 객체
    # regex => SQL의 like연산자 기능, 검색어 '길' => 홍길동, 갓길, 길길
    # 길이 포함된 문자열을 모두 검색
    search_list = []

    if search == 0:
        search_list.append({"title":{"$regex" : keyword}})
    elif search == 1:
        search_list.append({"contents":{"$regex" : keyword}})
    elif search == 2:
        search_list.append({"title":{"$regex" : keyword}})
        search_list.append({"contents":{"$regex" : keyword}})
    elif search == 3:
        search_list.append({"name":{"$regex" : keyword}})

    if len(search_list) > 0:
        query = {"$or":search_list}
    
    '''
        {
            "$or" : [
                {"title":{"$regex" : 손흥민}},
                {"title":{"$regex" : 김말똥}},
                {"title":{"$regex" : 홍길동}}
            ]
        }
        {
            "$and" : [
                {"title":{"$regex" : 손흥민}},
                {"title":{"$regex" : 김말똥}},
                {"title":{"$regex" : 홍길동}}
            ]
        }
    '''

    print(query)
    
    board = mongo.db.board
    # docs = board.find({}).skip((page-1)*limit).limit(limit)
    docs = board.find(query).skip((page-1)*limit).limit(limit).sort("regdate", -1)

    # 리스트의 전체 갯수
    tot_count = board.find(query).count()

    # 마지막 페이지의 수를 구하기
    last_page_num = math.ceil(tot_count / limit)
    
    # 페이지 블럭을 5개씩 표현
    block_size = 5

    # 현재 블럭의 위치 : 0, 1
    block_num = int((page-1)/ block_size)

    # 블럭의 블럭의 시작값 : 첫번째 블럭일 경우에는 시작값 :1, 두번째: 2
    block_start = int((block_size * block_num)+1)

    # 블럭의 마지막 값 : 첫번째 블럭의 마지막 값 :5, 두번째 : 10
    block_last = block_start + (block_size - 1)

    # if block_last > last_page_num:
    #     block_last = last_page_num

    if keyword is None:
        keyword = ""


    return render_template("list.html", docs = docs, 
                                        limit = limit,
                                        page = page,
                                        block_start = block_start,
                                        block_last = block_last,
                                        last_page_num = last_page_num,
                                        keyword=keyword,
                                        search=search)



######################################
# @app.route("/view")
# def board_view():
#   idx = request.args.get("idx")


# clean-url, fancy-url 표기 방식은 (보안적인 측면 고려, 사용편의성 고려한 표기방식)
@app.route("/view/<idx>")
@login_required
def board_view(idx):

    #
    page = request.args.get("page", default=1, type=int)
    search = request.args.get("search",-1,type=int)
    keyword = request.args.get("keyword",'',str)
    
    if idx is not None:
        board = mongo.db.board

        # data = board.find_one({"_id":ObjectId(idx)})
        # return_document=False는 조회수가 업데이트 된 후(보고난 후)에 변수에 할당
        # return_document=True는 볼 때 바로 조회수에 할당됨
        data = board.find_one_and_update({"_id":ObjectId(idx)}, 
                        {"$inc":{"hit":1}}, return_document=True)

        if data is not None:
            result = {
                "id" : data.get("_id"),
                "name" : data.get("name"),
                "title" : data.get("title"),
                "contents": data.get("contents"),
                "regdate" :data.get("regdate"),
                "hit" : data.get("hit"),
                "writer_id":data.get("writer_id","")
            }

            # print(result)

            return render_template("view.html", result = result, search= search, page=page, keyword=keyword)


    return abort(404)

@app.route("/write", methods=["GET", "POST"])
@login_required
def board_write():
    if request.method == "POST":
        name = request.form.get("name")
        title = request.form.get("title")
        contents = request.form.get("contents")
        print(name, title, contents)

        # UTC는 국제 표준시 (참고: GMT(Greenwich Mean Time) - 그리니치 평균시, 세계 협정시)
        # UTC와 GMT는 혼용되어 사용됨, 시간차가 거의 없음.


        # UTC Time은 밀리세컨드(millisecond: 1000분의 1초)로 표현되기 때문 *1000을 해주고
        # 소수점이 나오는 걸 방지하기 위해 round함수로 반올림 해준다.
        current_utc_time = round((datetime.utcnow().timestamp()) * 1000)


        # board 컬렉션 생성해서 board라는 이름으로 받음
        board = mongo.db.board

        post_data = {
            "name":name,
            "title":title,
            "contents":contents,
            "regdate": current_utc_time,
            # 글 수정 삭제시 본인의 글인지 확인하기 위한 용도
            "writer_id":session.get("id"), 
            "hit" : 0
        }

        doc = board.insert_one(post_data)
        print(doc.inserted_id)


        # 렌더링을 할 경우에는 inserted_id는 Object객체이므로 문자열로 형변환 해야한다
        # return str(doc.inserted_id)
        return redirect(url_for("board_view", idx=doc.inserted_id))
    else :
        return render_template("write.html")

@app.route("/join", methods=["GET","POST"])
def member_join():
    if request.method == "POST":
        name = request.form.get("name", type=str)
        email = request.form.get("email", type=str)
        pw = request.form.get("pw", type=str)
        pw2 = request.form.get("pw2", type=str)

        if name == "" or email == "" or pw == "" or pw2 == "":
            '''
            플라스크는 flashing 시스템을 가지고 사용자에게 피드백을 주는
            간편한 메가니즘을 제공한다.

            이 시스템은 기본적으로 요청의 끝에 메세지를 기록하고 있다.
            이 메시지를 사용하기 위해서는 리스트의 마지막 요소를 가져오면 된다.

            주로 템플릿에 메세지를 전달하게 된다.
            해당 메세지는 일회성이다.

            '''
            flash("값이 입력되지 않았습니다.. 다시 확인하세요!!")
            return render_template("join.html" )

        if pw != pw2:
            flash("비밀번호가 다릅니다.")

            return render_template("join.html" )
        
        # members collection 객체를 생성 또는 가져오기
        members = mongo.db.members

        # 중복된 회원이 있는지 확인하기
        cnt = members.find({"email":email}).count()

        if cnt > 0:
            flash("이미 가입된 회원입니다.")
            return render_template("join.html" )

        # 회원가입 하기

        current_utc_time = round(datetime.utcnow().timestamp() * 1000)
        post_data = {
            "name" : name,
            "email" : email,
            "pw" : pw,
            "join_date" : "",
            "login_time" : current_utc_time,
            "login_count":0,
        }

        members.insert_one(post_data)

        return "<h3>회원가입 처리 되었습니다.</h3>"
    else:
        return render_template("join.html")

@app.route("/login", methods=["GET","POST"])
def member_login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("pw")
        
        next_url = request.form.get("next_url")

        members = mongo.db.members
        doc = members.find_one({"email": email})

        if doc is None:
            flash("이메일이 존재하지 않습니다.. 다시 로그인 하세요")
            return redirect(url_for("member_login"))
        else:
            if doc.get("pw") == password:
                session["email"] = email
                session["name"] = doc.get('name')
                session["id"] = str(doc.get('_id'))
                
                # 세션의 유지시간을 조작가능 설정
                session.permanent = True
                if next_url is not None:
                    return redirect(next_url)
                else:      

                    return redirect(url_for('list'))
            else:
                flash("비밀번호가 일치하지 않습니다. 다시 확인하세요")
                return redirect(url_for('member_login'))

        return ""
    else:
        next_url = request.args.get("next_url", type=str)
        if next_url is not None:
            return render_template("login.html", next_url=next_url)
        else:
            return render_template("login.html")

@app.route("/modify/<idx>", methods=["GET","POST"])
def modify(idx):
    if request.method == "GET":
        board = mongo.db.board
        data = board.find_one({"_id":ObjectId(idx)})

        if data is None:
            flash("게시물이 존재하지 않습니다.")
            return redirect(url_for("list"))
        else:
            if session.get("id") == data.get("writer_id"):
                return render_template("modify.html", data=data)
            else:
                flash("글 수정 권한이 없습니다.")     
                return render_template("modify.html", data=data)
    # POST
    else:
        title = request.form.get('title')
        contents = request.form.get("contents")

        board = mongo.db.board
        data = board.find_one({"_id":ObjectId(idx)})

        if session.get('id') == data.get('writer_id'):
            board.update_one({"_id":ObjectId(idx)}, 
                {"$set":
                    {
                        "title":title,
                        "contents":contents
                    }
                }
            )

            flash('수정되었습니다.')
            return redirect(url_for("board_view", idx = idx))
        else:
            flash("글수정 권한이 없습니다.")
            return redirect(url_for("list"))
    
    return ""

@app.route("/delete/<idx>")
def delete(idx):
    board = mongo.db.board
    data = board.find_one({"_id":ObjectId(idx)})
    if data.get("writer_id") == session.get("id"):
        board.delete_one({"_id":ObjectId(idx)})
        flash("삭제됨")
    else:
        flash("대상없음")

    return redirect(url_for("list"))

if __name__ == "__main__":
    app.run(debug=True)