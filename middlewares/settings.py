# TOKEN_BOT = '6604747356:AAGOg7npHpV0RcP1RMl_58tsorFJCX3vfxQ'
# ADMIN_ID = 1

from environs import Env
from dataclasses import dataclass


@dataclass
class Bots:
    bot_token: str
    admin_id: int


@dataclass
class Settings:
    bots: Bots


def get_settings(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        bots=Bots(
            bot_token=env.str("BOT_TOKEN"),
            admin_id=env.str("ADMIN_ID")
        )
    )


config = get_settings('.env')
