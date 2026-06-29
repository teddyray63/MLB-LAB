from typing import Any


def normalize_name(name: Any) -> str:
    if not isinstance(name, str):
        return ""
    name = name.strip()
    if "," in name:
        last, first = [x.strip() for x in name.split(",", 1)]
        return f"{first} {last}".lower()
    return name.lower()


def nz(v: Any) -> Any:
    return 0 if v is None else v
