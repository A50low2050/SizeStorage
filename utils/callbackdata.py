from aiogram.filters.callback_data import CallbackData


class ModelInfo(CallbackData, prefix='model'):
    unique_id: int
    name: str
