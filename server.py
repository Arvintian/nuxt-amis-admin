from nuxt import register_blueprint
from controllers.login import bp_login


register_blueprint(bp_login, url_prefix="/api/login")
