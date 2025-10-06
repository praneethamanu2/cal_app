# 🧮 Python Command-Line Calculator

A professional-grade, modular **command-line calculator** written in Python.  
This project demonstrates clean architecture, error handling, unit testing, and continuous integration with **GitHub Actions** enforcing **100% test coverage**.

---

## 🚀 Features

- **REPL interface** for continuous calculations.
- **Arithmetic operations:** addition, subtraction, multiplication, and division.
- **Commands:** `help`, `history`, and `exit`.
- **Input validation:** uses both *LBYL* (Look Before You Leap) and *EAFP* (Easier to Ask Forgiveness than Permission) paradigms.
- **Error handling:** gracefully handles invalid input and division by zero.
- **Calculation history** for the current session.
- **Comprehensive tests** with 100% line and branch coverage.
- **CI/CD integration** using GitHub Actions.

---

## 🗂️ Project Structure

calculator_app/
│
├── app/
│ ├── calculator/
│ │ └── repl.py
│ ├── calculation/
│ │ ├── calculation.py
│ │ ├── factory.py
│ │ └── init.py
│ ├── operation/
│ │ └── operations.py
│ └── init.py
│
├── tests/
│ ├── test_operations.py
│ ├── test_calculations.py
│ ├── test_repl.py
│ └── conftest.py
│
├── .github/
│ └── workflows/
│ └── python-app.yml
│
├── pyproject.toml
├── .coveragerc
└── README.md

yaml
Copy code

---

## 🧰 Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/praneethamanu2/calculator_app.git
cd calculator_app
2️⃣ Create and activate a virtual environment
bash
Copy code
python3 -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
3️⃣ Install dependencies
bash
Copy code
python -m pip install --upgrade pip
pip install pytest pytest-cov coverage
🧮 Run the Calculator
bash
Copy code
python -m app.calculator.repl
Then type:

bash
Copy code
add 2 3
multiply 4 5
history
exit
🧪 Running Tests
Run all tests and measure coverage:

bash
Copy code
pytest --cov=app --cov-branch
View the coverage report:

bash
Copy code
coverage report
Generate an HTML coverage report:

bash
Copy code
coverage html
open htmlcov/index.html
✅ Continuous Integration (GitHub Actions)
Every push or pull request to the main branch triggers automated tests and coverage checks via the workflow:
.github/workflows/python-app.yml

If coverage drops below 100%, the build fails.

Example snippet:

yaml
Copy code
- name: Run tests with coverage
  run: pytest --cov=app --cov-branch
- name: Check coverage
  run: coverage report --fail-under=100
🧠 Design Principles
Modular architecture: separation of calculator logic, calculations, and operations.

DRY principle: no duplicate logic across modules.

Error handling:

LBYL → checks number format using regex before conversion.

EAFP → handles ZeroDivisionError in the REPL loop.

Clean testing strategy: parameterized tests for arithmetic and factory logic, simulated REPL inputs for CLI coverage.

📈 Example Session
shell
Copy code
Calculator ready. Type 'help' for instructions.
> add 2 3
add 2.0 3.0 = 5.0
> divide 10 0
Error: division by zero.
> multiply 2 3 4
multiply 2.0 3.0 4.0 = 24.0
> history
add 2.0 3.0 = 5.0
multiply 2.0 3.0 4.0 = 24.0
> exit
Goodbye!
