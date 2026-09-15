#!/usr/bin/env python3
"""Parse and compile every Python code cell in the repository notebooks."""

from __future__ import annotations

import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]


def compilable_python(source: str) -> str:
    """Replace line-oriented IPython magics with comments before compilation."""
    lines: list[str] = []
    for line in source.splitlines(keepends=True):
        if line.lstrip().startswith(("%", "!")):
            indent = line[: len(line) - len(line.lstrip())]
            lines.append(f"{indent}# IPython-only: {line.lstrip()}")
        else:
            lines.append(line)
    return "".join(lines)


def check_notebook(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # JSON validity is part of the check.
        return [f"{path.relative_to(ROOT)}: invalid notebook JSON: {exc}"]

    if notebook.get("nbformat") != 4:
        errors.append(f"{path.relative_to(ROOT)}: expected nbformat 4")

    for index, cell in enumerate(notebook.get("cells", [])):
        if cell.get("cell_type") != "code":
            continue
        source = compilable_python("".join(cell.get("source", [])))
        try:
            compile(source, f"{path.name}:cell-{index}", "exec")
        except SyntaxError as exc:
            errors.append(
                f"{path.relative_to(ROOT)} cell {index}, line {exc.lineno}: {exc.msg}"
            )
    return errors


def main() -> int:
    notebooks = sorted((ROOT / "code").glob("*.ipynb"))
    if not notebooks:
        print("No notebooks found in code/", file=sys.stderr)
        return 1

    errors = [error for path in notebooks for error in check_notebook(path)]
    if errors:
        print("Notebook checks failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Notebook checks passed: {len(notebooks)} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
