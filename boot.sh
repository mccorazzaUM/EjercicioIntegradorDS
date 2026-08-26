python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
python -m fastapi dev app/main.py