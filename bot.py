import logging
from aiogram import Bot, Dispatcher, types, executor

from config import API_TOKEN
from keyboards import start_keyboards, menu_keyboards, lavash_keyboards, contact, buy_product
from aiogram.types import InputFile

logging.basicConfig(level=logging.INFO)

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)

cart = []


@dp.message_handler(commands='start')
async def welcome(message: types.Message):
    await message.answer(f'Assalomu aleykum {message.from_user.full_name}, fast food botimizga xush kelibsiz\n'
                         f'Birortasini tanlang', reply_markup=start_keyboards)


@dp.message_handler()
async def keyboards_func(message: types.Message):
    try:
        if message.text == '🍴 Menu' or message.text == '🔙 Orqaga':
            await message.answer('Kategoriyani tanlang', reply_markup=menu_keyboards)

        elif message.text == '🔙 Bosh sahifa':
            await message.answer('Bosh sahifaga qaytdik', reply_markup=start_keyboards)

        elif message.text == '🛍 Mening zakazlarim':
            await message.answer(f'Bu mening zakazlarim bo\'limi\n{cart}')
        elif message.text == '✍️ Ariza qoldirish':
            await message.answer('Bu ariza qoldirish joyi, admin bilan bog\'lanish uchun @mirolimov_a',
                                 reply_markup=contact)
        elif message.text == '⚙️ Sozlamalar':
            await message.answer('Bu sozlamalar joyi:')

        elif message.text == '🌯 Lavash':
            lavash_rasm = types.InputFile('images/lavash/lavash.jpg')
            await message.answer_photo(photo=lavash_rasm, caption="Bu lavash menyusi", reply_markup=lavash_keyboards)

        elif message.text == 'mini lavash':
            mini_l = InputFile('images/lavash/mini_lavash.png')
            await message.answer_photo(photo=mini_l, caption='Narxi 17900 sum', reply_markup=buy_product)
        elif message.text == 'big lavash':
            big_l = InputFile('images/lavash/big_lavash.png')
            await message.answer_photo(photo=big_l, caption='Narxi 22900 sum')
        elif message.text == 'mini lavash + cheese':
            mini_l_c = InputFile('images/lavash/mini_lavash_cheese.jpg')
            await message.answer_photo(photo=mini_l_c, caption='Narxi 19900 sum')
        elif message.text == 'big lavash + cheese':
            big_l_c = InputFile('images/lavash/big_lavash_cheese.jpg')
            await message.answer_photo(photo=big_l_c, caption='Narxi 24900 sum')

        elif message.text == '🌭 Hot dog':
            hot_dog_rasm = InputFile('images/hot_dog/hot_dog.jpg')
            await message.answer_photo(photo=hot_dog_rasm)
        elif message.text == 'mini hot dog':
            mini_h_d = InputFile('images/hot_dog/mini_hot_dog.jpg')
            await message.answer_photo(photo=mini_h_d, caption='Narxi 14900 sum')
        elif message.text == 'big hot dog':
            big_h_d = InputFile('images/hot_dog/big_hot_dog.jpg')
            await message.answer_photo(photo=big_h_d, caption='Narxi 19900 sum')
        elif message.text == 'ultra hot dog':
            ultra_h_d = InputFile('images/hot_dog/ultra_hot_dog.jpg')
            await message.answer_photo(photo=ultra_h_d, caption='Narxi 24900 sum')

        elif message.text == '🌮 Taco':
            taco_rasm = InputFile('images/taco/taco.jpg')
            await message.answer_photo(photo=taco_rasm)
        elif message.text == 'mini taco':
            mini_taco = InputFile('images/taco/mini_taco.jpg')
            await message.answer_photo(photo=mini_taco, caption='Narxi 19900 sum')
        elif message.text == 'big taco':
            big_taco = InputFile('images/taco/big_taco.jpg')
            await message.answer_photo(photo=big_taco, caption='Narxi 24900 sum')

        elif message.text == '🍔 Burger':
            burger_rasm = InputFile('images/burger/burger.jpg')
            await message.answer_photo(photo=burger_rasm)
        elif message.text == 'mini burger':
            mini_burger = InputFile('images/burger/mini_burger.jpg')
            await message.answer_photo(photo=mini_burger, caption='Narxi 14900 sum')
        elif message.text == 'big burger':
            big_burger = InputFile('images/burger/big_burger.jpg')
            await message.answer_photo(photo=big_burger, caption='Narxi 19900 sum')
        elif message.text == 'cheese burger':
            cheese_burger = InputFile('images/burger/cheese_burger.jpg')
            await message.answer_photo(photo=cheese_burger, caption='Narxi 24900 sum')

        elif message.text == '🍕 Pizza':
            pizza_rasm = InputFile('images/pizza/pizza.jpg')
            await message.answer_photo(photo=pizza_rasm)
        elif message.text == 'pipperoni pizza':
            pipperoni_pizza = InputFile('images/pizza/pipperoni_pizza.jpg')
            await message.answer_photo(photo=pipperoni_pizza, caption='Narxi 65000 sum')
        elif message.text == 'margarita pizza':
            margarita_pizza = InputFile('images/pizza/margarita_pizza.jpg')
            await message.answer_photo(photo=margarita_pizza, caption='Narxi 55000 sum')
        elif message.text == '4 pizza':
            pizza_4 = InputFile('images/pizza/4_pizza.jpg')
            await message.answer_photo(photo=pizza_4, caption='Narxi 80000 sum')
        elif message.text == 'qazili pizza':
            qaizli_pizza = InputFile('images/pizza/qazili_pizza.jpg')
            await message.answer_photo(photo=qaizli_pizza, caption='Narxi 85000 sum')
        elif message.text == 'qo\'ziqorinli pizza':
            q_pizza = InputFile('images/pizza/qo\'ziqorinli_pizza.jpg')
            await message.answer_photo(photo=q_pizza, caption='Narxi 75000 sum')

    except Exception as e:
        print('Error: ', e)
        await message.answer(f'Xatolik yuz berdi, iltimos qaytadan urinib ko\'ring | ERROR {e}')


@dp.callback_query_handler()
async def callback(call: types.CallbackQuery):
    call_data = call.data
    global cart
    if call_data == 'savatga_qoshish':
        cart.append(call.message.caption)
        await call.answer('Savatga qo\'shildi')

        await call.message.answer(cart)


if __name__ == '__main__':
    executor.start_polling(dp)
