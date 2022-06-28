from pathlib import Path
from typing import Optional

from pydantic import BaseSettings, Field, BaseModel
from dotenv import load_dotenv

base_path = Path(__file__).resolve().parent.parent
env_file_path = base_path / "scripts" / "docker" / ".env"

load_dotenv(dotenv_path=env_file_path)


class AppConfig(BaseModel):
    """Application configurations."""

    POSTGIS_VERSION_TAG: str = "14-3.1"

    CTCN_SCHEMA: str = "ctcn"
    CITIES: str = "comuni"
    CTMP_SCHEMA: str = "ctmp"
    SHEETS: str = "fogli"
    BUILDINGS: str = "fabbricati"
    LANDS: str = "particelle"
    CUIDENTI: str = "cuidenti"
    CUARCUIU: str = "cuarcuiu"
    CTPARTIC: str = "ctpartic"
    CTQUALIT: str = "ctqualit"
    CTTITOLA: str = "cttitola"
    CTTITOLI: str = "cttitoli"
    CTFISICA: str = "ctfisica"
    CTNONFIS: str = "ctnonfis"


class GlobalConfig(BaseSettings):
    """Global configurations."""

    # These variables will be loaded from the .env file. However, if
    # there is a shell environment variable having the same name,
    # that will take precedence.

    APP_CONFIG: AppConfig = AppConfig()

    # define global variables with the Field class
    ENV_STATE: Optional[str] = Field(None, env="ENV_STATE")

    # environment specific variables do not need the Field class
    POSTGRES_HOST: Optional[str] = None
    POSTGRES_PORT: Optional[int] = None
    POSTGRES_USER: Optional[str] = None
    POSTGRES_PASS: Optional[str] = None
    POSTGRES_DB: Optional[str] = None


class DevConfig(GlobalConfig):
    """Development configurations."""

    class Config:
        env_prefix: str = "DEV_"


class ProdConfig(GlobalConfig):
    """Production configurations."""

    class Config:
        env_prefix: str = "PROD_"


class FactoryConfig:
    """Returns a config instance depending on the ENV_STATE variable."""

    def __init__(self, env_state: Optional[str]):
        self.env_state = env_state

    def __call__(self):
        if self.env_state == "dev":
            return DevConfig()

        elif self.env_state == "prod":
            return ProdConfig()


cnf = FactoryConfig(GlobalConfig().ENV_STATE)()
