from functools import wraps
from flask import session, redirect, url_for, request

# 로그인 인터셉터
def login_required(f):
    @wraps(f)
    def decorated_func(*args, **kwargs):
        # 세션에 아이디가 없으면 로그인 페이지로 이동
        if session.get("id") is None or session.get("id") == "":
            return redirect(url_for("users.member_login", next_url=request.url))
        return f(*args, **kwargs)
    return decorated_func
