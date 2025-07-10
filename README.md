# Drinks API
This project is a RESTful API created as the core of an automated drink mixer or cocktail mixer. It provides the user a simple way of adding ingredients and combining them to create longdrinks and cocktails. 
The project has been created using Python's FastAPI together with SQLModel as ORM and Pydantic for data validation. PostgreSQL is used as database system. As per default for FastAPI applications, the asynchronous request handling is managed by Python's ASGI web server implementation called Uvicorn. 
<br>Note: This projects is currently still in development and has not yet beend deployed on a server. To see a more detailed example that includes Deployment, Docker Containerization, Nginx Reverse Proxy, Caching (Redis DB) etc. please check out my Social Media FastAPI project.

## API Endpoints and Requests


## Get Started
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

