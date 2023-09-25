from urllib.parse import quote_plus
from os.path import join, dirname
from dotenv import load_dotenv
import os


class Config:
    # Configuración de Flask
    SECRET_KEY = os.environ.get("SECRET_KEY") or "my-secret-key"
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Carga las variables de entorno
    dotenv_path = os.path.join(BASE_DIR, ".env")
    load_dotenv(dotenv_path)

    # Configuración de la base de datos
    DB_USER = os.environ.get("DB_USER")
    DB_PASSWORD = quote_plus(os.environ.get("DB_PASSWORD"))
    DB_HOST = os.environ.get("DB_HOST")
    DB_NAME = os.environ.get("DB_NAME")

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    )

    # Configuración del correo
    MAIL_BASE_URL = os.environ.get("MAIL_BASE_URL")
    MAIL_API_KEY = os.environ.get("MAIL_API_KEY")
    MAIL_DOMAIN = "qnt.com.co"
    DOMAINS = [
        "qnt.com.co",
        "extractoscuenta3.qnt.com.co",
        "extractoscuenta2.qnt.com.co",
        "extractoscuenta.qnt.com.co",
        "extractosmora2.qnt.com.co",
        "extractosmora.qnt.com.co",
        "disgnostico.qnt.com.co",
        "especiales.qnt.com.co",
        "no-responder.qnt.com.co",
    ]
    EMAIL_REPLYTO = "diagnosticofinanciero@qnt.com.co"
    CHECK_THRESHOLD = 20

    # Configuración de la aplicación
    APP_BASE_URL = os.environ.get("APP_BASE_URL")
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "app/uploaded_files")
    ALLOWED_EXTENSIONS = {"xls", "xlsx"}
    CACHE_REDIS_URL = os.environ.get("CACHE_REDIS_URL")
    CACHE_TIMEOUT = os.environ.get("CACHE_TIMEOUT", 300)
    CACHE_TYPE = "RedisCache"

    # Configuración de Celery (si decide usarlo)
    # CELERY_BROKER_URL = 'redis://localhost:6379/0'
    # CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'
    # CELERY_TASK_SERIALIZER = 'json'
    # CELERY_RESULT_SERIALIZER = 'json'
    # CELERY_ACCEPT_CONTENT = ['json']
    # CELERY_TIMEZONE = 'America/Bogota'
    # CELERY_ENABLE_UTC = True

    # broker_url = "redis://localhost:6379/0"
    # result_backend = "redis://localhost:6379/1"
    # task_serializer = "json"
    # result_serializer = "json"
    # accept_content = ["json"]
    # timezone = "America/Bogota"
    # enable_utc = True
    # imports = ("app.routes.extractos",)
