#QR generator by 0xy, ver-0.2
from aiogram import Bot, Dispatcher, types, executor
from config import token
from keyboard import menu
import locale
import qrcode
import image


bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def starter(msg: types.Message):
	await msg.answer('Приветствую тебя в боте! \nПришле мне любой текст и я сделаю QR-Code!', reply_markup= menu() )

@dp.message_handler(text="Создать QR-Code")
async def starter(msg: types.Message):
	await msg.answer('Пришли текст, из которого нужно сделать QR-Code.')

@dp.message_handler()
async def send_text_based_qr(msg: types.Message):
	qr = qrcode.QRCode(
	version=1,
	error_correction=qrcode.constants.ERROR_CORRECT_L,
	box_size=6,
	border=4,
	)

	await msg.answer('Ваш текст принят на обработку! \nПожалуйста подождите!')
	print('Принят текст на обработку от: ', msg.from_user.id)
	qr.add_data(msg.text)
	qr.make(fit=True)
	img = qr.make_image(fill_color="black", back_color="white")	
	img.save('code.png')
	qr.clear()

	with open('code.png', 'rb') as photo:
		await bot.send_photo(msg.chat.id, photo)
		await bot.send_message(msg.chat.id, 'Ваш QR-Code готов!', reply_markup= menu())
		print('Готовый QR-Code отправлен:', msg.from_user.id)



executor.start_polling(dp)