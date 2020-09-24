from . import *
from datetime import datetime

@members_blueprint.route("/join", methods=["GET","POST"])
def member_join():
    if request.method == "POST":
        name = request.form.get("name", type=str)
        email = request.form.get("email", type=str)
        pw = request.form.get("pw", type=str)
        pw2 = request.form.get("pw2", type=str)

        if name == "" or email == "" or pw == "" or pw2 == "":
            flash("값이 입력되지 않았습니다.. 다시 확인하세요!!")
            return render_template("join.html", title="회원가입")

        if pw != pw2:
            flash("비밀번호가 다릅니다.")

            return render_template("join.html", title="회원가입")

        
        # members collection 객체를 생성 또는 가져오기
        members = mongo.db.members

        # 중복된 회원이 있는지 확인하기
        cnt = members.find({"email":email}).count()

        if cnt > 0:
            flash("이미 가입된 회원입니다.")
            return render_template("join.html", title="회원가입")


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
        return render_template("join.html", title="회원가입")


@members_blueprint.route('/login', methods=['GET','POST'])
def member_login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("pw")
        
        next_url = request.form.get("next_url")

        members = mongo.db.members
        doc = members.find_one({"email": email})

        if doc is None:
            flash("이메일이 존재하지 않습니다.. 다시 로그인 하세요")
            return redirect(url_for("member.member_login"))
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
                    return redirect(url_for('home'))
            else:
                flash("비밀번호가 일치하지 않습니다. 다시 확인하세요")
                return redirect(url_for('member.member_login'))

        return ""
    else:
        next_url = request.args.get("next_url", type=str)
        if next_url is not None:
            return render_template("login.html", next_url=next_url, title="로그인")
        else:
            return render_template("login.html", title="로그인")   

  
@members_blueprint.route('/logout', methods=['GET'])
def logout():
    session.clear()
    # sss
    return redirect(url_for("home"))
