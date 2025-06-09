from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from app.routes.login import login_bp
# from app.routes.bancos import bancos_bp
# from app.routes.cuentas import cuentas_bp
# from app.routes.saldos import saldos_bp
from app.routes.create import create_bp
from app.conection_db import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Cargar configuración (incluye DB URI y debug)
    jwt = JWTManager(app)
    # Inicializar db con la app
    db.init_app(app)
    

    # Registrar blueprints
    app.register_blueprint(login_bp, url_prefix='/api/v1/login')
    # app.register_blueprint(bancos_bp, url_prefix='/api/v1/bancos')
    # app.register_blueprint(cuentas_bp, url_prefix='/api/v1/cuentas')
    # app.register_blueprint(saldos_bp, url_prefix='/api/v1/saldos')
    app.register_blueprint(create_bp, url_prefix='/api/v1/create')

    return app

app = create_app()
#CORS(app)
CORS(app, supports_credentials=True, origins=["http://localhost:5173"])

#CORS(app, supports_credentials=True)
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host="localhost", port=5000, debug=True)
