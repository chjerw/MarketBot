#НЕ ИЗМЕНЯЙТЕ ЭТОТ ФАЙЛ
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import available_regions

regions = InlineKeyboardBuilder()
for name, available in available_regions.items():
    regions.button(
        text=f"{name} {'✅' if available else '🚫'}",
        callback_data=name
    )
regions.adjust(2)
regions = regions.as_markup()

pay = InlineKeyboardBuilder()
pay.button(
    text="Я оплатил",
    callback_data="payed"
)
pay = pay.as_markup()