from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "GeoLedger"
    environment: str = "development"

    backend_host: str = "127.0.0.1"
    backend_port: int = 8000

    database_url: str = "postgresql://geoledger:geoledger@localhost:5432/geoledger"

    allowed_origins: list[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()