from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings


# load_dotenv()


class Settings(BaseSettings):
    """
    Settings class loading all of our env vars directly
    from the .env file if it exists (in dev).
    If there is  no .env file in production it will look
    in our OS.
    """

    db_host: str = Field(validation_alias="POSTGRES_HOST_ADDRESS")
    db_name: str = Field(validation_alias="POSTGRES_DB_NAME")
    db_user: str = Field(validation_alias="POSTGRES_USERNAME")
    db_port: str = Field(validation_alias="POSTGRES_PORT")
    db_pw: str = Field(validation_alias="POSTGRES_PASSWORD")
    db_service_name: str = Field(validation_alias="POSTGRES_SERVICE_NAME")
    debug: bool = Field(validation_alias="DEBUG")
    is_dev: bool = Field(validation_alias="DEV")

    class Config:
        env_file = "....env"


settings = Settings()
