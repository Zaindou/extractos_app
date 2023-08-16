import re


def is_valid_string(value, max_length=20):
    if not isinstance(value, str):
        return False
    return len(value) <= max_length


def is_valid_name(value):
    return is_valid_string(value, 80)


def is_valid_email(email):
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return re.match(email_regex, email) is not None and is_valid_string(email, 80)


def is_valid_integer(value):
    try:
        int(value)
        return True
    except (ValueError, TypeError):
        return False


def is_valid_float(value):
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False


# VALIDATOR STATEMENT-DEBT
def validate_row(row, idx):
    if not is_valid_name(row[2]):
        return (
            jsonify(
                {"error": f"Invalid name for 'nombre_titular' at row {idx}: {row[2]}"}
            ),
            400,
        )

    if row[6] and not is_valid_email(row[6]):
        return (
            jsonify({"error": f"Invalid email for 'mail_1' at row {idx}: {row[6]}"}),
            400,
        )
    if row[7] and not is_valid_email(row[7]):
        return (
            jsonify({"error": f"Invalid email for 'mail_2' at row {idx}: {row[7]}"}),
            400,
        )
    if row[8] and not is_valid_email(row[8]):
        return (
            jsonify({"error": f"Invalid email for 'mail_3' at row {idx}: {row[8]}"}),
            400,
        )

    if not row[6] and not row[7] and not row[8]:
        return (
            jsonify(
                {
                    "error": f"Algun(os) clientes no cuentan con correo, revisa el archivo. {idx}"
                }
            ),
            400,
        )

    if not is_valid_float(row[12]):
        return (
            jsonify(
                {
                    "error": f"Invalid float value for 'valor_cuota_mensual' at row {idx}: {row[12]}"
                }
            ),
            400,
        )

    if not is_valid_float(row[13]):
        return (
            jsonify(
                {
                    "error": f"Invalid float value for 'valor_mora' at row {idx}: {row[13]}"
                }
            ),
            400,
        )
