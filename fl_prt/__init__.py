from flask import Flask
from flask_mail import Mail
from .config.settings import conf

mail = Mail()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(conf[config_name])

    mail.init_app(app)

    from .main import main as main
    from .work import work as work

    app.register_blueprint(main, url_prefix='/')
    app.register_blueprint(work, url_prefix='/work')

    return app
