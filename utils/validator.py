def require_fields(data, fields):
    return [field for field in fields if not data.get(field)]


def is_valid_level(level):
    return level in {"N1", "N2", "N3", "N4", "N5"}
