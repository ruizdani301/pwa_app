from flask import Blueprint, jsonify, request, request, make_response
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
import http.cookies
#from app.extensions import session
from models.model import Usuario

login_bp = Blueprint('login', __name__)

cookie = http.cookies.SimpleCookie()
@login_bp.route('/', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    print(email, password)
    if not email or not password:
        return jsonify({'error': 'Email y contraseña son requeridos'}), 400

    usuario = Usuario.query.filter_by(email=email).first()
    if not usuario or not check_password_hash(usuario.password, password):    
        return jsonify({'error': 'Credenciales inválidas'}), 401

    
    access_token = create_access_token(identity=usuario.email, additional_claims={"role": "user"})

    
    # response = make_response(jsonify({'message': 'Login exitoso', 'token': access_token, "email": email}), 200)


    return (jsonify({'message': 'Login exitoso', 'token': access_token, "email": email}), 200)
