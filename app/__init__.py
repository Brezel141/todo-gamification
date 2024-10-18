from flask import Flask
from .extensions import db, login_manager
from .routes import main
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inizializzazione delle estensioni
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'

    # Registrazione del Blueprint
    app.register_blueprint(main)

    # Creazione delle tabelle nel database
    with app.app_context():
        db.create_all()

    return app
