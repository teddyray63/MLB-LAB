#!/usr/bin/env python3
"""Deterministic JSON structure inspector for evidence-first investigations."""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any, Iterable


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Recursively walk a JSON file and emit concrete paths, types, "
            "keys, array lengths, and scalar values."
        )
    )
    parser.add_argument("json_file", help="Path to the JSON file to inspect")
    parser.add_argument(
        "--match",
        nargs="+",
        metavar="TERM",
        help=(
            "Print only paths, keys, or scalar string values matching at "
            "least one term (case-insensitive)"
        ),
    )
    return parser.parse_args(argv)


def normalize_terms(terms: Iterable[str]) -> list[str]:
    return [term.casefold() for term in terms]


def term_matches(text: str, terms: list[str]) -> bool:
    folded = text.casefold()
    return any(term in folded for term in terms)


def format_scalar(value: Any) -> tuple[str, str]:
    if value is None:
        return "null", "null"
    if isinstance(value, bool):
        return "boolean", str(value).lower()
    if isinstance(value, int) and not isinstance(value, bool):
        return "number", str(value)
    if isinstance(value, float):
        return "number", repr(value)
    if isinstance(value, str):
        return "string", json.dumps(value, ensure_ascii=False)
    raise TypeError(f"Unsupported scalar type: {type(value)!r}")


def object_keys_line(path: str, keys: list[str]) -> str:
    key_list = ", ".join(keys)
    return f"{path} type=object keys=[{key_list}]"


def array_line(path: str, length: int) -> str:
    return f"{path} type=array length={length}"


def scalar_line(path: str, node_type: str, rendered_value: str) -> str:
    return f"{path} type={node_type} value={rendered_value}"


def collect_lines(value: Any, path: str, terms: list[str] | None) -> list[str]:
    lines: list[str] = []

    if isinstance(value, dict):
        keys = sorted(value.keys())
        line = object_keys_line(path, keys)
        if terms is None or term_matches(path, terms) or any(
            term_matches(key, terms) for key in keys
        ):
            lines.append(line)
        for key in keys:
            child_path = f"{path}.{key}" if path != "$" else f"$.{key}"
            lines.extend(collect_lines(value[key], child_path, terms))
        return lines

    if isinstance(value, list):
        line = array_line(path, len(value))
        if terms is None or term_matches(path, terms):
            lines.append(line)
        for index, item in enumerate(value):
            lines.extend(collect_lines(item, f"{path}[{index}]", terms))
        return lines

    node_type, rendered_value = format_scalar(value)
    line = scalar_line(path, node_type, rendered_value)
    if terms is None:
        lines.append(line)
        return lines

    if term_matches(path, terms):
        lines.append(line)
        return lines

    if node_type == "string" and term_matches(json.loads(rendered_value), terms):
        lines.append(line)

    return lines


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    terms = normalize_terms(args.match) if args.match else None

    try:
        with open(args.json_file, encoding="utf-8") as handle:
            data = json.load(handle)
    except OSError as exc:
        print(f"error: cannot read file: {exc}", file=sys.stderr)
        return 1
    except json.JSONDecodeError as exc:
        print(f"error: invalid JSON: {exc}", file=sys.stderr)
        return 1

    for line in collect_lines(data, "$", terms):
        print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
