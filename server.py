from nuxt import register_blueprint
from controllers.basic import bp_basic


register_blueprint(bp_basic, url_prefix="/api/basic")
