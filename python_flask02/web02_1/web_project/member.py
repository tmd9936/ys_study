from web_project import *



@app.route("/logout", methods=["GET"])
def logout():
    session.clear()
    return redirect(url_for("list"))

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
