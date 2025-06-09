from app.conection_db import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120),  nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f"<Usuario {self.email}>"

