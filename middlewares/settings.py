from environs import Env
from dataclasses import dataclass


@dataclass
class Bots:
    bot_token: str
    admin_id: int
    psg_user: str
    psg_password: str
    host: str
    port: int
    database: str


@dataclass
class Settings:
    bots: Bots


def get_settings(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        bots=Bots(
            bot_token=env.str("BOT_TOKEN"),
            admin_id=env.str("ADMIN_ID"),
            psg_user=env.str("PSG_USER"),
            psg_password=env.str("PSG_PASSWORD"),
            host=env.str("HOST"),
            port=env.int("PORT"),
            database=env.str("DATABASE")
        )
    )


config = get_settings('.env')

user = config.bots.psg_user
psw = config.bots.psg_password
database = config.bots.database
host = config.bots.host
port = config.bots.port

POSTGRES_URL = f'postgresql://{user}:{psw}@{host}:{port}/{database}'


DEFAULT_LIMIT = 2
DEFAULT_OFFSET = 0
