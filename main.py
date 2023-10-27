import telebot
from telebot import custom_filters
from telebot import StateMemoryStorage
from telebot.handler_backends import StatesGroup, State

state_storage = StateMemoryStorage()
# Вставить свой токет или оставить как есть, тогда мы создадим его сами
bot = telebot.TeleBot("5850048784:AAEXpV2OOvffjHiK7_XL-pUOcq4_vJjAse4",
                      state_storage=state_storage, parse_mode='Markdown')


class PollState(StatesGroup):
    name = State()
    age = State()


class HelpState(StatesGroup):
    wait_text = State()


text_button_1 = "Связь с администрацией"  # Можно менять текст
text_button_2 = "Грядущие мероприятия"  # Можно менять текст
text_button_3 = "Ссылка на сайт с доп. информацией"  # Можно менять текст

menu_keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_button_1,
    )
)

menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_button_2,
    ),
    telebot.types.KeyboardButton(
        text_button_3,
    )
)


@bot.message_handler(state="*", commands=['start'])
def start_ex(message):
    bot.send_message(
        message.chat.id,
        'Привет! Что будем делать?',  # Можно менять текст
        reply_markup=menu_keyboard)


@bot.message_handler(func=lambda message: text_button_1 == message.text)
def help_command(message):
    bot.send_message(message.chat.id, """Состав администрации: 
Директор: Вячеслав Валерьевич Малков (45-32-01)
Завуч: Германова Наталья Викторовна (natali@bk.ru)
Заместитель: Михеева Наталья Сергеевна (63-01-28)""", reply_markup=menu_keyboard)  # Можно менять текст


@ bot.message_handler(func=lambda message: text_button_2 == message.text)
def help_command(message):
    bot.send_message(message.chat.id, """Совсем СКОРО в колледже:
1. День самоуправления *16.11.2023* (для записи напиши в [группу] (https://vk.com/mkeiitss))
2. Фото-акция в честь Дня отца "Мы с папой молодцы! до *29.10.2023* (для участия отправь фото в [группу] (https://vk.com/gapou_mo_mkeiit)
3. Спортивное ориентирование *17.10.30*(для записи подойди в кабинет 411)""", reply_markup=menu_keyboard)  # Можно менять текст


@ bot.message_handler(func=lambda message: text_button_3 == message.text)
def help_command(message):
    bot.send_message(message.chat.id, "Чтобы получить ссылку кликни на слово [МКЭиИТ] (https://mkeiit.ru/)",
                     reply_markup=menu_keyboard)  # Можно менять текст


bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.TextMatchFilter())

bot.infinity_polling()

