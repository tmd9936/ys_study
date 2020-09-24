from functools import wraps
from web_project import session, redirect, url_for, request

def login_required(f):
    @wraps(f)
    def decorated_func(*args, **kwargs):
        if session.get("id") is None or session.get("id") == "":
            # request.url 현재 url을 의미함
            return redirect(url_for("member.member_login", 
                                next_url=request.url))
        return f(*args, **kwargs)
    return decorated_func

