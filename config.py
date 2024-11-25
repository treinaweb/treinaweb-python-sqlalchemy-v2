from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    db_host: str
    db_user: str
    db_password: str
    db_port: str
    db_name: str

    model_config = SettingsConfigDict(env_file=".env")


config = Config()
