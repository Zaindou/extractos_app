from app import db

# Statement Model
class Extracto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.String(20), db.ForeignKey("cliente.id"), nullable=False)
    id_contacto = db.Column(db.String(20), nullable=False)
    periodo = db.Column(db.Date)
    codigo_de_cargue = db.Column(db.String(100))
    tipo_extracto = db.Column(db.String(100))
    visitado = db.Column(db.Boolean)
    veces_visitado = db.Column(db.Integer, default=0, nullable=False)
    ultima_visita = db.Column(db.Date)
