from aiogram.fsm.state import StatesGroup, State


class ModelAdd(StatesGroup):
    get_name = State()
    get_description = State()
    get_photo = State()
    get_link_file = State()


class ObjectAdd(StatesGroup):
    get_name = State()
    get_description = State()
    get_photo = State()
    get_link_file = State()
