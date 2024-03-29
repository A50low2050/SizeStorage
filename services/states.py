from aiogram.fsm.state import StatesGroup, State


class ModelAdd(StatesGroup):
    get_name = State()
    get_description = State()
    get_photo = State()
    get_link_file = State()


class ModelUpdate(StatesGroup):
    unique_id = State()
    get_name = State()
    get_description = State()
    get_photo_id = State()
    get_file_link = State()


class ObjectAdd(StatesGroup):
    get_name = State()
    get_description = State()
    get_photo = State()
    get_link_file = State()


class ObjectUpdate(StatesGroup):
    unique_id = State()
    get_name = State()
    get_description = State()
    get_photo_id = State()
    get_file_link = State()
