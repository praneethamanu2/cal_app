from typing import List, Iterator, Callable
from app.calculator.repl import run_repl

def _make_input(lines):
    it: Iterator[str] = iter(lines)
    def _inner(_prompt: str = "") -> str:
        return next(it)
    return _inner

def test_repl_happy_path_and_errors():
    lines = [
        "help",
        "add 1 2",
        "divide 4 2",
        "divide 1 0",      # ZeroDivisionError path
        "multiply 2 3 4",
        "add 1 x",         # invalid number (LBYL)
        "power 2 3",       # unknown operation
        "history",         # should list past successful calcs
        "exit",
    ]
    outputs: List[str] = []
    run_repl(input_fn=_make_input(lines), output_fn=outputs.append)

    text = "\n".join(outputs)
    assert "Calculator ready." in text
    assert "Commands:" in text
    assert "add 1.0 2.0 = 3.0" in text
    assert "divide 4.0 2.0 = 2.0" in text
    assert "Error: division by zero." in text
    assert "multiply 2.0 3.0 4.0 = 24.0" in text
    assert "Error: Invalid number(s)." in text
    assert "Error: Unknown operation" in text
    assert "Goodbye!" in text

def test_repl_blank_lines_and_empty_history():
    lines = ["", "   ", "history", "exit"]
    outputs: List[str] = []
    run_repl(input_fn=_make_input(lines), output_fn=outputs.append)
    text = "\n".join(outputs)
    assert "(no history)" in text
    assert "Goodbye!" in text

def test_repl_eof_and_keyboardinterrupt():
    def input_eof(_prompt: str) -> str:
        raise EOFError
    out1: List[str] = []
    run_repl(input_fn=input_eof, output_fn=out1.append)
    assert "Exiting." in "\n".join(out1)

    def input_kb(_prompt: str) -> str:
        raise KeyboardInterrupt
    out2: List[str] = []
    run_repl(input_fn=input_kb, output_fn=out2.append)
    assert "Exiting." in "\n".join(out2)
