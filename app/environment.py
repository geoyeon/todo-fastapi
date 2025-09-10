from pydantic_settings import BaseSettings, SettingsConfigDict

class Environments(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="../.env",
        env_file_encoding="utf-8"
    )

    mongo_db_uri: str
    mongo_db_name: str

environments = Environments()