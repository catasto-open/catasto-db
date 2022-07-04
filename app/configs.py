from pathlib import Path
from typing import Optional

from pydantic import BaseSettings, Field, BaseModel
from dotenv import load_dotenv

base_path = Path(__file__).resolve().parent.parent
env_file_path = base_path / "scripts" / "docker" / ".env"

load_dotenv(dotenv_path=env_file_path)


class AppConfig(BaseModel):
    """Application configurations."""

    COMPOSE_PROJECT_NAME: str = "catasto-open"

    POSTGIS_VERSION_TAG: str = "14-3.1"
    GS_VERSION: str = "2.20.4"
    GS_WFS_VERSION: str = "1.0.0"

    CATASTO_OPEN_CITY_LAYER = "catasto_comuni"
    CATASTO_OPEN_SECTION_LAYER = "catasto_sezioni"
    CATASTO_OPEN_SHEET_LAYER = "catasto_fogli"
    CATASTO_OPEN_LAND_LAYER = "catasto_terreni"
    CATASTO_OPEN_BUILDING_LAYER = "catasto_fabbricati"
    CATASTO_OPEN_NATURAL_SUBJECT_LAYER = "catasto_persone_fisiche"
    CATASTO_OPEN_LEGAL_SUBJECT_LAYER = "catasto_persone_giuridiche"
    CATASTO_OPEN_SUBJECT_PROPERTY_LAYER = "catasto_particelle_soggetto"
    CATASTO_OPEN_LAND_DETAIL_LAYER = "catasto_dettagli_terreno"
    CATASTO_OPEN_BUILDING_DETAIL_LAYER = "catasto_dettagli_fabbricato"
    CATASTO_OPEN_PROPERTY_OWNER_LAYER = "catasto_titolari_immobile"

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
    POSTGRES_HOST_PORT: Optional[int] = None
    POSTGRES_CONTAINER_PORT: Optional[int] = None
    POSTGRES_USER: Optional[str] = None
    POSTGRES_PASS: Optional[str] = None
    POSTGRES_DB: Optional[str] = None

    CATASTO_OPEN_GS_WORKSPACE: Optional[str] = None
    CATASTO_OPEN_GS_WORKSPACE_NAMESPACE: Optional[str] = None
    CATASTO_OPEN_GS_DATASTORE: Optional[str] = None

    GEOSERVER_HOST: Optional[str] = None
    GEOSERVER_HOST_PORT: Optional[str] = None
    GEOSERVER_CONTAINER_PORT: Optional[str] = None
    GEOSERVER_DATA_DIR: Optional[str] = None
    GEOWEBCACHE_CACHE_DIR: Optional[str] = None
    GEOSERVER_ADMIN_PASSWORD: Optional[str] = None
    GEOSERVER_ADMIN_USER: Optional[str] = None
    INITIAL_MEMORY: Optional[str] = None
    MAXIMUM_MEMORY: Optional[str] = None


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
