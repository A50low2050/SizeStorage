from aiogram.filters.callback_data import CallbackData


class ModelInfo(CallbackData, prefix='model'):
    type_handler: str
    unique_id: int
    name: str


class ModelUpdateState(CallbackData, prefix='model_update'):
    unique_id: int
    name: str


class ObjectInfo(CallbackData, prefix='object'):
    type_handler: str
    unique_id: int
    name: str


class Paginator(CallbackData, prefix='paginator'):
    action: str
    limit: int
    offset: int
