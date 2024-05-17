from nuxt import logger, Request
from nuxt.utils import make_sync_response
import traceback


class AuthMiddleware(object):

    def __init__(self, get_response, app):
        self.current_app = app
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request: Request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if not request.path in ["/api/basic/login"]:
            token = request.cookies.get("token", None)
            if not token:
                token = request.headers.get("token", None)
            if not token:
                return make_sync_response(request, {
                    "status": -1,
                    "msg": "token is empty"
                })

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
