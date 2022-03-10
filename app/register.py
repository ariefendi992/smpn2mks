from app.controllers.c_hello import hello


def registerApp(app):
    app.register_blueprint(hello)
