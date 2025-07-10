# [Drinks API](https://github.com/Maiz22/drinks_api)
This project is a RESTful API created as the core of an automated drink mixer or cocktail mixer. It provides the user with a simple way of adding ingredients and combining them to create long drinks and cocktails.<br>
The project has been created using Python's FastAPI together with SQLModel as the ORM and Pydantic for data validation. PostgreSQL is used as the database system. As is standard for FastAPI applications, asynchronous request handling is managed by Python's ASGI web server implementation called Uvicorn.<br>
Note: This project is currently still in development and has not yet been deployed on a server. To see a more detailed example of an API that includes deployment, Docker containerization, Nginx reverse proxy, caching (Redis DB), etc., please check out my [Social Media FastAPI](https://github.com/Maiz22/fastapi_post_api) project.

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
  - POST: Uploads an image to the ingredient by its id.
- "/ingredients/by-name/\<name\>
  - GET: Get an ingredient by its name.
- "/drinks
  - GET: Get a list of all drinks.
  - POST: Create a new drink. 
- "/drinks/\<id\>
  - GET: Get drink by its id.
  - PUT: Edit drink by its id.
  - DELETE: Delete drink by its id.
- "/drinks/\<id\>/upload-image"
  - POST: Uploads an image to the drink by its id.
- "/drinks/by-name/\<name\>
  - GET: Get a drink by its name.
- "/links"
  - POST: Creates a link between a drink and its ingredient.
- "/links/\<drink_id\>/\<ingredient_id\>"
  - PUT: Edits a link between a drink and its ingredient.
  - DELETE: Deletes a link between a drink and its ingredient.
- "/docs"
  - GET: Swagger UI Documentation showing all schemas and allowing users to make tests.

## How does it work?
In order to create a drink, we first need to create the ingredients by sending a POST request to the `/ingredients` endpoint. To add corresponding pictures to the added ingredients, we send a POST request to `/ingredients/<id>/upload-image` using the ID(s) of the previously created ingredient(s).
In the same way we created our ingredients, we can now add a drink with a corresponding picture to the database by sending a POST request to the `/drinks` endpoint, followed by another POST request to the `/drinks/<id>/upload-image` route.
To connect ingredients to drinks, we use the `/links` endpoint. By sending a POST request containing the drink_id, the ingredient_id, and the amount (of the ingredient), we link ingredients to drinks.
For more information and all schemas, please refer to the following "Get Started" chapter and check out the Swagger UI at the `/docs` endpoint.

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

