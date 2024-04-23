import tomllib
from pathlib import Path
from pydantic import BaseModel


class PostgresConfig(BaseModel):
    link: str


class TelegramConfig(BaseModel):
    token: str


class ChromeDriverConfig(BaseModel):
    path: str


class RedisConfig(BaseModel):
    host: str
    port: int


class Config(BaseModel):
    postgres: PostgresConfig
    telegram: TelegramConfig
    chromedriver: ChromeDriverConfig
    redis: RedisConfig


config_name = 'config.toml'
config_file = Path(config_name)
if not config_file.exists():
    parent_dir_config_file = Path('..') / config_file
    config = Config.model_validate(tomllib.loads(parent_dir_config_file.read_text(encoding='utf-8')))
else:
    config = Config.model_validate(tomllib.loads(Path(config_name).read_text(encoding='utf-8')))
