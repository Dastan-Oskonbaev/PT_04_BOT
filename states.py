from aiogram.fsm.state import State, StatesGroup

class Survey(StatesGroup):
    name = State()
    age = State()
    hobby = State()


class Product(StatesGroup):
    product_name = State()
    price = State()
    quantity = State()


