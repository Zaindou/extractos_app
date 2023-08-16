from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_caching import Cache
from config import Config
from flask import Flask
import logging

# Crear la instancia de la base de datos y otras extensiones
db = SQLAlchemy()
cache = Cache()

logging.basicConfig(
    filename="logs.log",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s",
)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar la extensión de la base de datos y otras extensiones
    db.init_app(app)
    # Inicializar la extensión de migración
    migrate = Migrate(app, db)
    # Initialize the cache extension
    cache.init_app(app)


    # Importar y registrar blueprints
    from app.routes import main, extractos
    # Es un buen lugar para importar tareas para asegurarse de que sean reconocidas

    app.register_blueprint(main.main)
    app.register_blueprint(extractos.extractos, url_prefix="/extractos")




    return app




