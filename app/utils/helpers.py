from datetime import datetime
from config import Config
from io import BytesIO
import PyPDF2
import locale


ALLOWED_EXTENSIONS = Config.ALLOWED_EXTENSIONS

def encrypt_pdf(pdf_content, password):
    pdf_writer = PyPDF2.PdfFileWriter()
    pdf_reader = PyPDF2.PdfFileReader(BytesIO(pdf_content))

    for page in range(pdf_reader.numPages):
        pdf_writer.addPage(pdf_reader.getPage(page))

    pdf_writer.encrypt(str(password))

    encrypted_pdf = BytesIO()
    pdf_writer.write(encrypted_pdf)

    return encrypted_pdf.getvalue()

# Periods are received as strings, this function converts them to date format.
def period_to_date(periodo_str):
    # Mapeo de los meses
    meses = {
        "ENE": "01",
        "FEB": "02",
        "MAR": "03",
        "ABR": "04",
        "MAY": "05",
        "JUN": "06",
        "JUL": "07",
        "AGO": "08",
        "SEP": "09",
        "OCT": "10",
        "NOV": "11",
        "DIC": "12",
        "ene": "01",
        "feb": "02",
        "mar": "03",
        "abr": "04",
        "may": "05",
        "jun": "06",
        "jul": "07",
        "ago": "08",
        "sep": "09",
        "oct": "10",
        "nov": "11",
        "dic": "12",
    }

    partes = periodo_str.split("-")

    if len(partes) == 3:
        mes, dia, año = partes
        return f"{año}-{meses[mes]}-{dia.zfill(2)}"
    elif len(partes) == 2:
        mes, año = partes
        return f"{año}-{meses[mes]}-01"
    else:
        raise ValueError(f"Formato no reconocido: {periodo_str}")


def date_to_period(date):
    # Set the locale to Spanish
    locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")
    # Format the date as a string with the abbreviated month name in Spanish
    period = date.strftime("%b-%Y").replace(".", "").upper()
    locale.setlocale(locale.LC_TIME, "")
    return period


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def get_primary_email(cliente):
    if cliente.mail_1:
        return cliente.mail_1
    elif cliente.mail_2:
        return cliente.mail_2
    elif cliente.mail_3:
        return cliente.mail_3
    else:
        return None

def mask_string(s):
    if not s:
        return ''
    return '*' * (len(s) - 5) + s[-5:]


def format_currency(value):
    if value is None:
        return "$0"
    locale.setlocale(locale.LC_ALL, 'es_CO.UTF-8') 
    formatted_value = locale.currency(value, grouping=True, symbol=False)  
    return formatted_value.split(',')[0]