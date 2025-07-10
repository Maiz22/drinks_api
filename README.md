# Drinks API
This project is a RESTful API created as the core of an automated drink mixer or cocktail mixer. It provides the user a simple way of adding ingredients and combining them to create longdrinks and cocktails.<br>
The project has been created using Python's FastAPI together with SQLModel as ORM and Pydantic for data validation. PostgreSQL is used as database system. As per default for FastAPI applications, the asynchronous request handling is managed by Python's ASGI web server implementation called Uvicorn.<br>
Note: This projects is currently still in development and has not yet beend deployed on a server. To see a more detailed example that includes Deployment, Docker Containerization, Nginx Reverse Proxy, Caching (Redis DB) etc. please check out my Social Media FastAPI project.

## API Endpoints, Requests and Features
- "/"
  -  GET: Root endpoint displaying a simple welcome message to the user.
- "/ingredients"
  -  GET: Get a list of all ingredients.
  -  POST: Create a new ingredient.
- "/ingredients/\<id\>"
  - GET: Get ingredient by its id.
  - PUT: Updated ingredient properties by its id.
  - DELETE: Delete an ingredient by its id
- "/ingredients/\<id\>/upload-image"
  - POST: Uploads an image to the ingredient.
- "ingredients/by-name/\<name\>
  - GET: Get an ingredient by its name.

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
5. Create `.env` file and populate according to the `.env.example`
6. Run application:
- `uvicorn src.main:app --reload`

Test it in with Postman or in your browser go to:
- `http://localhost:8000/docs`

