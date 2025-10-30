# BUG-REPORTING-TOOL-FOR-QA-ANALYSIS-GAME-TESTING
(Flask + SQLite)
Simple full-stack bug reporting app with CRUD, search, and filtering.

## Setup
1. Python 3.8+
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate    # Windows
   pip install -r requirements.txt
   ```
2. Initialize DB:
   ```bash
   python init_db.py
   ```
3. Run the app:
   ```bash
   export FLASK_APP=app.py
   flask run
   # or on Windows PowerShell:
   # $env:FLASK_APP = "app.py"; flask run
   ```
4. Open http://127.0.0.1:5000 in your browser.
