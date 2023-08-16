from app import db

# Products Model
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.String(20), db.ForeignKey("cliente.id"), nullable=False)
    periodo = db.Column(db.Date)
    numero_producto = db.Column(db.String(20))
    dia_pago = db.Column(db.Date)
    valor_cuota_mensual = db.Column(db.Float)
    valor_mora = db.Column(db.Float)
    dias_mora = db.Column(db.Integer)
    siguiente_pago = db.Column(db.Date)
    numero_obligaciones = db.Column(db.Integer)
    saldo_total = db.Column(db.Float)
    meses_castigo = db.Column(db.Integer)
    fecha_corte = db.Column(db.Date)

# class ProductosEstadoCuenta(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     id_cliente = db.Column(db.String(20), db.ForeignKey("cliente.id"), nullable=False)
#     periodo = db.Column(db.Date)
#     numero_producto = db.Column(db.String(20))
#     saldo_total = db.Column(db.Float)
#     meses_castigo = db.Column(db.Integer)
#     fecha_corte = db.Column(db.Date)


