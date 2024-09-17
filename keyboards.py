from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

start_keyboards = ReplyKeyboardMarkup(resize_keyboard=True)
start_keyboards.add(KeyboardButton('🍴 Menu'))
start_keyboards.add(KeyboardButton('🛍 Mening zakazlarim'))
start_keyboards.add(KeyboardButton('✍️ Ariza qoldirish'), KeyboardButton('⚙️ Sozlamalar'))

contact = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Telefon raqam jonatish', request_contact=True))

menu_keyboards = ReplyKeyboardMarkup(resize_keyboard=True)
menu_keyboards.add(KeyboardButton('🌯 Lavash'), KeyboardButton('🌭 Hot dog')),
menu_keyboards.add(KeyboardButton('🌮 Taco'), KeyboardButton('🍔 Burger')),
menu_keyboards.add(KeyboardButton('🍕 Pizza'), KeyboardButton('🥩 Steyk')),
menu_keyboards.add(KeyboardButton('🍦 Muzqaymoq'), KeyboardButton('🎂 Tort')),
menu_keyboards.add(KeyboardButton('🍟 Kartoshka Fri'))
menu_keyboards.add(KeyboardButton('🔙 Bosh sahifa'))

# lavash_keyboards = ReplyKeyboardMarkup(resize_keyboard=True)
# lavash_keyboards.add(KeyboardButton('mini lavash'), KeyboardButton('big lavash')),
# lavash_keyboards.add(KeyboardButton('mini lavash + cheese'), KeyboardButton('big lavash + cheese')),
# lavash_keyboards.add(KeyboardButton('🔙 Orqaga'))

buy_product = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton('🛒 Savatga qo\'shish', callback_data='savatga_qoshish'),
        InlineKeyboardButton('🔙 Orqaga', callback_data='orqaga'),
    ]
]
                                   )

lavash_keyboards = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton('mini lavash'),
        KeyboardButton('big lavash'),
    ],
    [
        KeyboardButton('mini lavash + cheese'),
        KeyboardButton('big lavash + cheese'),
    ],
    [
        KeyboardButton('🔙 Orqaga'),
    ]
])

hot_dog_keyboards = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, keyboard=[
    [
        KeyboardButton('mini hot dog'), KeyboardButton('big hot dog'), KeyboardButton('ultra hot dog'),
    ],
    [
        KeyboardButton('🔙 Orqaga'),
    ]
])

taco_keyboards = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, keyboard=[
    [
        KeyboardButton('mini taco'), KeyboardButton('big taco'),
    ],
    [
        KeyboardButton('🔙 Orqaga'),
    ]
])

burger_keyboards = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, keyboard=[
    [
        KeyboardButton('mini burger'), KeyboardButton('big burger'), KeyboardButton('cheese burger'),
    ],
    [
        KeyboardButton('🔙 Orqaga'),
    ]
])

pizza_keyboards = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, keyboard=[
    [
        KeyboardButton('pipperoni pizza'), KeyboardButton('margarita pizza'), KeyboardButton('4 pizza'),
    ],
    [
        KeyboardButton('qazili pizza'), KeyboardButton('qo\'ziqorinli pizza')
    ],
    [
        KeyboardButton('🔙 Orqaga'),
    ]
])
