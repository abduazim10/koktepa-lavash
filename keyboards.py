from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton



start_keyboards = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Menu 🍴'),
    KeyboardButton('🛍 Savat')
).add(
    KeyboardButton('✍️ Ariza qoldirish'), 
    KeyboardButton('⚙️ Sozlamalar')
)


    
contact = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Telefon raqam jonatish', request_contact=True))

menu_keyboards = ReplyKeyboardMarkup(resize_keyboard=True)
menu_keyboards.add(KeyboardButton('🌯 Lavash'), KeyboardButton('🌭 Hot dog')),
menu_keyboards.add(KeyboardButton('🍔 Burger'),KeyboardButton('🍕 Pizza')),
menu_keyboards.add(KeyboardButton('🍟 Sneklar'))
menu_keyboards.add(KeyboardButton('🔙 Bosh sahifa'))

zakaz_keyboards = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton('Ha'),
        KeyboardButton('Yoq'),
    ]
])


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
location_keyboards = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, keyboard=[
    [
        KeyboardButton(text="Lokatsiya Jonatish 📍",  request_location=True)
    ]
])

phone_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, keyboard=[
    [
        KeyboardButton(text="Telefon Raqam Jonatish",  request_contact=True)
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
        KeyboardButton('pepperoni pizza'), KeyboardButton('margarita pizza'), KeyboardButton('4 pizza'),
    ],
    [
        KeyboardButton('qazili pizza'), KeyboardButton('qo\'ziqorinli pizza')
    ],
    [
        KeyboardButton('🔙 Orqaga'),
    ]
])
snek_keyboards = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, keyboard=[
    [
        KeyboardButton('Kichik Fri'), KeyboardButton('Ortancha Fri'), KeyboardButton('Katta Fri'),
    ],
    [
        KeyboardButton('Naggets 5'), KeyboardButton('Naggets 8'), KeyboardButton('Naggets 15'),
    ],
    [
        KeyboardButton('🔙 Orqaga'),
    ]
])
