from flask import Blueprint, jsonify
import requests
import json
from flask import request
import jwt
import datetime
from flask import current_app as app
from app.conection_db import db
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash

from models.model import Usuario

create_bp = Blueprint('create', __name__)


@create_bp.route('/', methods=['POST'])
def create_user():
    data = request.json
    email = data.get('email')
    password = data.get('password') 
    if not email or not password:
        return jsonify({'error': 'Email y contraseña son requeridos'}), 400

    if Usuario.query.filter_by(email=email).first():
        return jsonify({'error': 'El usuario ya existe'}), 400

    # Cifrar la contraseña antes de guardar
    hashed_password = generate_password_hash(password)
    nuevo_usuario = Usuario(email=email, password=hashed_password)
    db.session.add(nuevo_usuario)
    db.session.commit()

 
    return jsonify({
        'message': 'Usuario creado exitosamente',

    }), 201