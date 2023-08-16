from app import db

class Cliente(db.Model):
    id = db.Column(db.String(20), primary_key=True, nullable=False)
    id_contacto = db.Column(db.String(20), nullable=False)
    nombre_titular = db.Column(db.String(80), nullable=False)
    telefono_1 = db.Column(db.String(20))
    telefono_2 = db.Column(db.String(20))
    telefono_3 = db.Column(db.String(20))
    mail_1 = db.Column(db.String(80))
    mail_2 = db.Column(db.String(80))
    mail_3 = db.Column(db.String(80))
    periodo = db.Column(db.Date)

    productos = db.relationship("Producto", backref="cliente")
    extractos = db.relationship("Extracto", backref="cliente")