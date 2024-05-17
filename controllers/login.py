from nuxt import Request
from nuxt.utils import make_sync_response
from nuxt import Blueprint


bp_login = Blueprint("bp_login")


@bp_login.route("", methods=["POST"])
def login(request: Request):
    username, password = request.json.get("username"), request.json.get("password")
    if "{}:{}".format(username, password) != "admin:admin":
        return {
            "status": -1,
            "msg": "username/password incorrect"
        }
    rsp = make_sync_response(request, {
        "status": 0,
        "msg": "success",
        "data": {
            "token": "amis"
        }
    })
    rsp.set_cookie('token', 'amis', max_age=3600)
    return rsp
