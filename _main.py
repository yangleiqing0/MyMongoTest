from create_app import app
from views import login_blueprint, zz_blueprint, dg_blueprint, mm_blueprint


def register_init():
    app.register_blueprint(login_blueprint)
    app.register_blueprint(zz_blueprint)
    app.register_blueprint(dg_blueprint)
    app.register_blueprint(mm_blueprint)
    return app
