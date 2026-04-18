from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile, CallbackQuery

import asyncio
import config
import keyboards

dp = Dispatcher()
router = Router()
dp.include_router(router)

async def on_startup():
    print("Бот успешно запущен!")

@router.message(Command("start"))
async def start_cmd(message: Message):

    banner = FSInputFile("imgs/banner.jpg")

    await message.answer_photo(
        photo=banner,
        caption=f"Приветствую на <b>{config.project_name}</b>,\n{config.project_desc}\n<b>Выберите регион, чтобы продолжить:</b>",
        reply_markup=keyboards.regions
    )

@router.callback_query()
async def callback(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer()

    if callback.data == "payed":
        await callback.message.answer(f"<b>Отлично!</b>\nМы получили вашу оплату!\n\nКоординаты: <b>55.788924, 37.688632</b>")

    if callback.data in config.available_regions:
        status = config.available_regions[callback.data]

    if status:
        await callback.message.answer(f"Выбранный регион: <b>{callback.data}</b>\n\nК оплате: <b>0.001 BTC</b>\nАдрес: <b>0x0000000000000000</b>", reply_markup=keyboards.pay)
    else:
        await callback.message.answer("К сожалению, этот регион не доступен!")


async def main():
    bot = Bot(token=config.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.startup.register(on_startup)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())