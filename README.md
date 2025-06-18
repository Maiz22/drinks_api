# Mixer API
In your terminal:
1. Clone git repository:
- `git clone https://github.com/Maiz22/drinks_api.git`
2. Create venv + activate venv:
- `python -m venv venv`
- `venv\Scripts\activate`
3. Install requirements:
- `pip install -r requirements.txt`
4. Create Postgress DB (e.g. with PGAdmin)
5. Create `.env` file and populate accoding to the `.env.example`
6. Run application:
- `uvicorn src.main:app --reload`

Test it in your browser go to:
- `http://localhost:8000/docs`
