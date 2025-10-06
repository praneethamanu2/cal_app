from __future__ import annotations
import re
from typing import Callable, List, Tuple
from app.calculation.factory import CalculationFactory

_HELP = """Commands:
  add|subtract|multiply|divide <n1> <n2> [n3...]
  help       Show this help
  history    Show calculation history
  exit       Quit
"""

_NUM = re.compile(r"^-?\d+(\.\d+)?$")  # LBYL: validate numbers

def _parse_numbers(tokens: List[str]) -> Tuple[float, ...]:
    if not tokens or not all(_NUM.match(t) for t in tokens):
        raise ValueError("Invalid number(s).")
    return tuple(float(t) for t in tokens)

def run_repl(
    input_fn: Callable[[str], str] = input,
    output_fn: Callable[[str], None] = print,
) -> None:
    factory = CalculationFactory()
    history: List[str] = []
    output_fn("Calculator ready. Type 'help' for instructions.")
    while True:
        try:
            line = input_fn("> ").strip()
        except (EOFError, KeyboardInterrupt):
            output_fn("\nExiting.")
            break
        if not line:
            continue
        tokens = line.split()
        cmd = tokens[0].lower()

        if cmd == "help":
            output_fn(_HELP)
            continue
        if cmd == "history":
            if not history:
                output_fn("(no history)")
            else:
                for entry in history:
                    output_fn(entry)
            continue
        if cmd == "exit":
            output_fn("Goodbye!")
            break

        try:
            operands = _parse_numbers(tokens[1:])
            calc = factory.create(cmd, operands)
            entry = str(calc)
            history.append(entry)
            output_fn(entry)
        except ZeroDivisionError:
            output_fn("Error: division by zero.")
        except ValueError as e:
            output_fn(f"Error: {e}")

def main() -> None:
    run_repl()  # pragma: no cover

if __name__ == "__main__":  # pragma: no cover
    main()
