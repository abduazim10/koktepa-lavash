import logging
from aiogram import Bot, Dispatcher, types, executor

from config import API_TOKEN
from keyboards import start_keyboards, menu_keyboards, lavash_keyboards, contact, buy_product,hot_dog_keyboards,location_keyboards , snek_keyboards,zakaz_keyboards,phone_keyboard,pizza_keyboards,burger_keyboards
from aiogram.types import InputFile
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN, proxy='http://proxy.server:3128')
dp = Dispatcher(bot=bot, storage=MemoryStorage())

cart = []
class TaskStates(StatesGroup):
    status = State()
    locatin = State()
    number = State()

@dp.message_handler(commands='start')
async def welcome(message: types.Message):
    await message.answer(f'Assalomu aleykum {message.from_user.full_name}, fast food botimizga xush kelibsiz\n'
                         f'Birortasini tanlang', reply_markup=start_keyboards)

@dp.message_handler(lambda message: message.text == "🛍 Savat")
async def keyboards_func(message: types.Message):
    if not cart:
        await message.answer('Savatta hech nima yoq')
    else:
        cart_items = "\n".join(cart)  # Narsalarni yangi qatordan ajratib ko'rsatadi
        await message.answer(f'Savtda:\n{cart_items}\nShular bor zakazni tasdiqlaysizmi?', reply_markup=zakaz_keyboards)
        await TaskStates.status.set()

@dp.message_handler(state=TaskStates.status)
async def process_add_task(message: types.Message, state: FSMContext):
    status1 = message.text
    if status1 == 'Yoq':
        await state.finish()
        await message.answer('Zakaz Otmen qilindi')
    elif status1 == 'Ha':
        await state.update_data(status =message.text)
        await message.answer(text='Locatsiani yuboring:' ,reply_markup=location_keyboards)
        await TaskStates.next()
global latitude
global longitude
@dp.message_handler(content_types=types.ContentType.LOCATION, state=TaskStates.locatin)
async def process_location(message: types.Message, state: FSMContext):
    await state.update_data(location=message.location)
    global latitude
    global longitude
    latitude = message.location.latitude
    longitude = message.location.longitude
    await message.answer(text="Telefon raqamingizni yuboring", reply_markup=phone_keyboard)
    await TaskStates.next()

@dp.message_handler(content_types=types.ContentType.CONTACT, state=TaskStates.number)
async def process_phone(message: types.Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    global latitude
    global longitude
    await state.finish()
    await message.answer(f'Zakazingiz 45minut ichida sizga boradi!')
    cart_items = "\n".join(cart)
    user_info = f'{cart_items}\n{data["number"]}'


    await bot.send_message(chat_id='6313238207', text=f'Yangi Zakaz:\n{user_info} \n{message.from_user.full_name}')
    await bot.send_location(chat_id='6313238207', latitude=latitude, longitude=longitude)

@dp.message_handler(lambda message: message.text == 'Menu 🍴' or message.text == '🔙 Orqaga')
async def keyboards_func(message: types.Message):
    await message.answer('Kategoriyani tanlang', reply_markup=menu_keyboards)

@dp.message_handler()
async def keyboards_func(message: types.Message):
    try:

        if message.text == '🔙 Bosh sahifa':
            await message.answer('Bosh sahifaga qaytdik', reply_markup=start_keyboards)

        
        elif message.text == '✍️ Ariza qoldirish':
            await message.answer('Bu ariza qoldirish joyi, admin bilan bog\'lanish uchun @Az1zov1ch_A')
        elif message.text == '⚙️ Sozlamalar':
            await message.answer('Bu sozlamalar joyi:')

        elif message.text == '🌯 Lavash':
            
            await message.answer_photo(photo='http://cc.oqtepalavash.uz/api/image/pc-544206df-3e7c-4390-a640-6e808ed7b40d.jpg', caption="Bu lavash menyusi", reply_markup=lavash_keyboards)

        elif message.text == 'mini lavash':
            await message.answer_photo(photo='http://cc.oqtepalavash.uz/api/image/40486e62-d5c9-4d36-8ca8-74f94c204be2.png', caption='mini lavash\nNarxi 27 000 sum', reply_markup=buy_product)  
        elif message.text == 'big lavash':
            await message.answer_photo(photo='http://cc.oqtepalavash.uz/api/image/da52bd62-8233-4e07-abf4-590f16da0d5a.png', caption='big lavash\nNarxi 32 000 sum',reply_markup=buy_product)
        elif message.text == 'mini lavash + cheese':
            
            await message.answer_photo(photo='http://cc.oqtepalavash.uz/api/image/7885ced2-9aab-4bcd-b2f5-14b149463b52.png', caption='mini lavash + cheese\nNarxi 29 000 sum',reply_markup=buy_product)
        elif message.text == 'big lavash + cheese':
            
            await message.answer_photo(photo='http://cc.oqtepalavash.uz/api/image/47d338c6-65ef-43dc-91d5-00ef8671073d.png', caption='big lavash + cheese\nNarxi 34 000  sum',reply_markup=buy_product)

        elif message.text == '🌭 Hot dog':
            
            await message.answer_photo(photo='http://cc.oqtepalavash.uz/api/image/pc-8448cd0a-af6b-47a1-8b3a-79d9eb5eb0bd.jpg', reply_markup= hot_dog_keyboards)
        elif message.text == 'mini hot dog':
            
            await message.answer_photo(photo='http://cc.oqtepalavash.uz/api/image/4ba84e47-e14f-475b-b1fc-ead298cfa2e3.png', caption='mini hot dog\nNarxi 11 000 sum',reply_markup=buy_product)
        elif message.text == 'big hot dog':
            
            await message.answer_photo(photo='http://cc.oqtepalavash.uz/api/image/818b8a47-fd7f-4164-8859-e7b9b4fb2fc3.png', caption='big hot dog\nNarxi 14 000 sum',reply_markup=buy_product)
        elif message.text == 'ultra hot dog':
            
            await message.answer_photo(photo='http://cc.oqtepalavash.uz/api/image/10b4be39-022f-4076-a563-ea3f23cefedb.png', caption='ultra hot dog\nNarxi 17 000 sum',reply_markup=buy_product)

        

        elif message.text == '🍔 Burger':
            
            await message.answer_photo(photo='http://cc.oqtepalavash.uz/api/image/pc-8448cd0a-af6b-47a1-8b3a-79d9eb5eb0bd.jpg' , reply_markup=burger_keyboards)
        elif message.text == 'burger':
            await message.answer_photo(photo='http://cc.oqtepalavash.uz/api/image/d9d553d9-ddb0-41cd-9523-ad67057beb4c.png', caption='burger\nNarxi 21 000 sum',reply_markup=buy_product)
        elif message.text == 'big burger':
           
            await message.answer_photo(photo='http://cc.oqtepalavash.uz/api/image/51cbea60-9599-46b4-817b-a0583c7a303b.png', caption='big burger\nNarxi 25 000 sum',reply_markup=buy_product)
        elif message.text == 'cheese burger':
            
            await message.answer_photo(photo='http://cc.oqtepalavash.uz/api/image/2c5b49c7-ed11-4219-a3f3-3725b1ddbf8d.png', caption='cheese burger\nNarxi 27 000 sum',reply_markup=buy_product)

        elif message.text == '🍕 Pizza':
            
            await message.answer_photo(photo='http://cc.oqtepalavash.uz/api/image/pc-7660904a-3880-4e6c-8f87-82bf2628e84a.jpg' , reply_markup=pizza_keyboards)
        elif message.text == 'pepperoni pizza':
           
            await message.answer_photo(photo='http://cc.oqtepalavash.uz/api/image/a910174e-e070-4b5f-b52c-2b363e1f64fe.png', caption='pepperoni pizza\nNarxi 67 000 sum',reply_markup=buy_product)
        elif message.text == 'margarita pizza':
            
            await message.answer_photo(photo='https://bellissimo.uz/_next/image?url=https%3A%2F%2Fio.bellissimo.uz%2Fimages%2Fd356188d-b9b4-4c06-9251-4429a17adfd5.jpg&w=1920&q=100', caption='margarita pizza\nNarxi 63 000 sum',reply_markup=buy_product)
        elif message.text == '4 pizza':
            await message.answer_photo(photo='https://bellissimo.uz/_next/image?url=https%3A%2F%2Fio.bellissimo.uz%2Fimages%2Fc14e362c-57a5-49fd-9a80-b14ce099b777.jpg&w=1920&q=100', caption='4 pizza\nNarxi 92 000 sum',reply_markup=buy_product)
        elif message.text == 'Super Miks':
            
            await message.answer_photo(photo='https://bellissimo.uz/_next/image?url=https%3A%2F%2Fio.bellissimo.uz%2Fimages%2F94844930-5c66-4c12-a670-93b048169dbe.jpg&w=1920&q=100', caption='Super Miks\nNarxi 92 000 sum',reply_markup=buy_product)
        elif message.text == 'qo\'ziqorinli pizza':
            
            await message.answer_photo(photo='https://bellissimo.uz/_next/image?url=https%3A%2F%2Fio.bellissimo.uz%2Fimages%2F15f8411b-947d-405b-9c78-016711ba8da1.jpg&w=1920&q=100', caption='qo\'ziqorinli pizza\naNarxi 63 000 sum',reply_markup=buy_product)
        elif message.text =='🍟 Sneklar':
            await message.answer_photo(photo='http://cc.oqtepalavash.uz/api/image/pc-f5bcbebe-6103-4e3d-a89e-6f9563bead24.jpg', reply_markup=snek_keyboards)
        elif message.text == 'Kichik Fri':
            await message.answer_photo(photo='http://cc.oqtepalavash.uz/api/image/53e9540b-f29d-47d2-ac55-1ac1e2ae830f.png',caption='Kichik Fri\nNarxi 10 000sum', reply_markup=buy_product)
        elif message.text == 'Ortancha Fri':
            await message.answer_photo(photo='http://cc.oqtepalavash.uz/api/image/6d1b3bf8-ad8a-4924-822a-f25840ec7d98.png',caption='Ortancha Fri\nNarxi 16 000sum', reply_markup=buy_product)
        elif message.text == 'Katta Fri':
            await message.answer_photo(photo='http://cc.oqtepalavash.uz/api/image/664f18a9-329d-4b6d-b477-77c9cd928ef4.png',caption='Katta Fri\nNarxi 22 000sum', reply_markup=buy_product)
        elif message.text == 'Naggets 5':
            await message.answer_photo(photo='http://cc.oqtepalavash.uz/api/image/0ba7423f-afe6-4d9d-b29f-87db8e756a01.png',caption='Naggets 5\nNarxi 16 000sum', reply_markup=buy_product)
        elif message.text == 'Naggets 8':
            await message.answer_photo(photo='http://cc.oqtepalavash.uz/api/image/381e1f32-a1de-463d-b3e8-8cba33a3f47b.png',caption='Naggets 8\nNarxi 22 000sum', reply_markup=buy_product)
        elif message.text == 'Naggets 15':
            await message.answer_photo(photo='http://cc.oqtepalavash.uz/api/image/c169cd49-8686-4e16-af76-1d74d268eb82.png',caption='Naggets 15\nNarxi 39 000sum', reply_markup=buy_product)
        
        

    except Exception as e:
        print('Error: ', e)
        await message.answer(f'Xatolik yuz berdi, iltimos qaytadan urinib ko\'ring | ERROR {e}')


@dp.callback_query_handler()
async def callback(call: types.CallbackQuery):
    call_data = call.data  # 'savatga_qoshish'
    global cart
    if call_data == 'savatga_qoshish':
        cart.append(call.message.caption)
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await bot.send_message(chat_id=call.message.chat.id, text='Savatga qoshildi')
        
        

        # await call.message.answer(cart)
    if call_data == 'orqaga':
        await bot.send_message(call.from_user.id, 'Kategoriyani tanlang', reply_markup=menu_keyboards)



if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)
