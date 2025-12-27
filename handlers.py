from aiogram import types
from aiogram.filters import CommandStart
from aiogram import Router
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

router = Router()

start_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="/start")]],
    resize_keyboard=True
)

@router.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer("سلام 👋 خوش آمدید!", reply_markup=start_kb)
    await message.answer("پیام خود را بنویسید!", reply_markup=start_kb)

@router.message()
async def echo_handler(message: types.Message):
    await message.answer(f"تو گفتی: {message.text}")
