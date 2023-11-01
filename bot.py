import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Command

from aiogram.dispatcher.storage import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from btn import *
from states import *


BOT_TOKEN = "6600379465:AAEf5a5cCTMtJ3HSj1L8Msd94UdK-w1fEoY"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, parse_mode='html')
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)


async def command_menu(dp: Dispatcher):
  await dp.bot.set_my_commands(
    [
      types.BotCommand('start', 'Ishga tushirish'),
      types.BotCommand('help', 'Bot malumot')
    ]
  )


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
  await message.answer(f"<b>Assalom alaykum {message.from_user.first_name} UstozShogird kanalining rasmiy botiga xush kelibsiz!</b>\n\n/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!", reply_markup=menu)

@dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
  await message.answer(f"UzGeeks faollari tomonidan tuzilgan Ustoz-Shogird kanali.\n\nBu yerda Programmalash bo`yicha\n#Ustoz,\n#Shogird,\n#oquvKursi,\n#Sherik,\n#Xodim va\n#IshJoyi\ntopsihingiz mumkin.\n\nElon berish: @{(await bot.get_me()).username}\n\nAdmin: @UstozShogirdAdminBot")

#####################################----------SherikKerak----------##############################33

@dp.message_handler(text='Sherik kerak')
async def sherik_kerak_handler(message: types.Message):
  context = """<b>Sherik topish uchun ariza berish</b>

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi."""
  await message.answer(context)
  await message.answer("<b>Ism, familiyangizni kiriting?</b>")

  await SherikKerakState.fio.set()


@dp.message_handler(content_types=['text'], state=SherikKerakState.fio)
async def sherik_kerak_fio_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(fio=text)

  context = """<b>📚 Texnologiya:</b>

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#"""
  await message.answer(context)
  await SherikKerakState.texnologiya.set()

@dp.message_handler(content_types=['text'], state=SherikKerakState.texnologiya)
async def sherik_kerak_texnologiya_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(texnalogiya=text)

  context = """📞 <b>Aloqa:</b> 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67"""
  await message.answer(context)
  await SherikKerakState.aloqa.set()

@dp.message_handler(content_types=['text'], state=SherikKerakState.aloqa)
async def sherik_kerak_aloqa_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(aloqa=text)

  context = """<b>🌐 Hudud:</b> 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting."""
  await message.answer(context)
  await SherikKerakState.hudud.set()

@dp.message_handler(content_types=['text'], state=SherikKerakState.hudud)
async def sherik_kerak_hudud_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(hudud=text)

  context = """<b>💰 Narxi:</b>

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?"""
  
  await message.answer(context)
  await SherikKerakState.narxi.set()

@dp.message_handler(content_types=['text'], state=SherikKerakState.narxi)
async def sherik_kerak_narxi_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(narxi=text)
  await SherikKerakState.kasbi.set()
  
  context = """<b>👨🏻‍💻 Kasbi:</b> 

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba"""
  await message.answer(context)

@dp.message_handler(content_types=['text'], state=SherikKerakState.kasbi)
async def sherik_kerak_kasbi_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(kasbi=text)
  await SherikKerakState.murojat_vaqti.set()

  context = """<b>🕰 Murojaat qilish vaqti:</b> 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00"""
  await message.answer(context)

@dp.message_handler(content_types=['text'], state=SherikKerakState.murojat_vaqti)
async def sherik_kerak_vaqti_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(vaqti=text)
  await SherikKerakState.maqsad.set()

  context = """<b>🔎 Maqsad:</b> 

Maqsadingizni qisqacha yozib bering."""
  await message.answer(context)

@dp.message_handler(content_types=['text'], state=SherikKerakState.maqsad)
async def sherik_kerak_maqsad_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(maqsad=text)

  info = await state.get_data()
  context = f"""<b>Sherik kerak:</b>

🏅 Sherik:<b>{info["fio"]}</b>
📚 Texnologiya: <b>{info["texnalogiya"]}</b> 
🇺🇿 Telegram: <b>@{message.from_user.username}</b>
📞 Aloqa: <b>{info["aloqa"]}</b>
🌐 Hudud: <b>{info["hudud"]}</b> 
💰 Narxi: <b>{info["narxi"]}</b>
👨🏻‍💻 Kasbi: <b>{info["kasbi"]}</b>
🕰 Murojaat qilish vaqti: <b>{info["vaqti"]}</b>
🔎 Maqsad: <b>{info["maqsad"]}</b>

#sherik"""
  await message.answer(context)
  await state.finish()

###############################----------IshJoyiKerak----------###################################################

@dp.message_handler(text='Ish joyi kerak')
async def ish_joyi_kerak_handler(message: types.Message):
  context = """<b>Ish joyi topish uchun ariza berish</b>

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi."""
  await message.answer(context)
  await message.answer("<b>Ism, familiyangizni kiriting?</b>")

  await IshJoyiKerakState.fio.set()


@dp.message_handler(content_types=['text'], state=IshJoyiKerakState.fio)
async def ish_joyi_kerak_fio_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(fio=text)

  context = """<b>🕑 Yosh:</b> 

Yoshingizni kiriting?
Masalan, 19"""
  await message.answer(context)
  await IshJoyiKerakState.age.set()

@dp.message_handler(content_types=['text'], state=IshJoyiKerakState.age)
async def ish_joyi_kerak_age_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(age=text)

  context = """<b>📚 Texnologiya:</b>

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#"""
  await message.answer(context)
  await IshJoyiKerakState.texnologiya.set()

@dp.message_handler(content_types=['text'], state=IshJoyiKerakState.texnologiya)
async def ish_joyi_kerak_texnologiya_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(texnologiya=text)

  context = """📞 <b>Aloqa:</b> 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67"""
  await message.answer(context)
  await IshJoyiKerakState.aloqa.set()

@dp.message_handler(content_types=['text'], state=IshJoyiKerakState.aloqa)
async def ish_joyi_aloqa_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(aloqa=text)

  context = """<b>🌐 Hudud:</b> 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting."""
  await message.answer(context)
  await IshJoyiKerakState.hudud.set()

@dp.message_handler(content_types=['text'], state=IshJoyiKerakState.hudud)
async def ish_joyi_kerak_hudud_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(hudud=text)

  context = """<b>💰 Narxi:</b>

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?"""
  
  await message.answer(context)
  await IshJoyiKerakState.narxi.set()

@dp.message_handler(content_types=['text'], state=IshJoyiKerakState.narxi)
async def ish_joyi_kerak_narxi_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(narxi=text)
  await IshJoyiKerakState.kasbi.set()
  
  context = """<b>👨🏻‍💻 Kasbi:</b> 

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba"""
  await message.answer(context)

@dp.message_handler(content_types=['text'], state=IshJoyiKerakState.kasbi)
async def ish_joyi_kerak_kasbi_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(kasbi=text)
  await IshJoyiKerakState.murojat_vaqti.set()

  context = """<b>🕰 Murojaat qilish vaqti:</b> 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00"""
  await message.answer(context)

@dp.message_handler(content_types=['text'], state=IshJoyiKerakState.murojat_vaqti)
async def ish_joyi_kerak_vaqti_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(vaqti=text)
  await IshJoyiKerakState.maqsad.set()

  context = """<b>🔎 Maqsad:</b> 

Maqsadingizni qisqacha yozib bering."""
  await message.answer(context)

@dp.message_handler(content_types=['text'], state=IshJoyiKerakState.maqsad)
async def ish_joyi_kerak_maqsad_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(maqsad=text)

  info = await state.get_data()
  context = f"""<b>Ish joyi kerak:</b>

👨‍💼 Xodim: <b>{info["fio"]}</b>
🕑 Yosh: <b>{info["age"]}</b>
📚 Texnologiya: <b>{info["texnologiya"]}</b>
🇺🇿 Telegram: <b>@{message.from_user.username}</b> 
📞 Aloqa: <b>{info["aloqa"]}</b>
🌐 Hudud: <b>{info["hudud"]}</b>
💰 Narxi: <b>{info["narxi"]}</b>
👨🏻‍💻 Kasbi: <b>{info["kasbi"]}</b> 
🕰 Murojaat qilish vaqti: <b>{info["vaqti"]}</b>
🔎 Maqsad: <b>{info["maqsad"]}</b>

#xodim"""
  await message.answer(context)
  await state.finish()

################################################----------HodimKerak----------###################################################

@dp.message_handler(text='Hodim kerak')
async def hodim_kerak_handler(message: types.Message):
  context = """<b>Xodim topish uchun ariza berish</b>

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi."""
  await message.answer(context)
  await message.answer("<b>🎓 Idora nomi?</b>")

  await HodimKerakState.idora.set()


@dp.message_handler(content_types=['text'], state=HodimKerakState.idora)
async def hodim_kerak_idora_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(idora=text)

  context = """<b>📚 Texnologiya:</b>

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#"""
  await message.answer(context)
  await HodimKerakState.texnologiya.set()

@dp.message_handler(content_types=['text'], state=HodimKerakState.texnologiya)
async def hodim_kerak_texnologiya_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(texnologiya=text)

  context = """<b>📞 Aloqa:</b> 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67"""
  await message.answer(context)
  await HodimKerakState.aloqa.set()

@dp.message_handler(content_types=['text'], state=HodimKerakState.aloqa)
async def hodim_kerak_aloqa_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(aloqa=text)

  context = """<b>🌐 Hudud:</b> 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting."""
  await message.answer(context)
  await HodimKerakState.hudud.set()

@dp.message_handler(content_types=['text'], state=HodimKerakState.hudud)
async def hodim_kerak_hudud_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(hudud=text)

  context = """✍️Mas'ul ism sharifi?"""
  await message.answer(context)
  await HodimKerakState.fio.set()

@dp.message_handler(content_types=['text'], state=HodimKerakState.fio)
async def hodim_kerak_fio_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(fio=text)

  context = """<b>🕰 Murojaat qilish vaqti:</b> 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00"""
  
  await message.answer(context)
  await HodimKerakState.murojat_vaqti.set()

@dp.message_handler(content_types=['text'], state=HodimKerakState.murojat_vaqti)
async def hodim_kerak_murojat_vaqti_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(murojat_vaqti=text)
  
  context = """🕰 Ish vaqtini kiriting?"""
  await message.answer(context)
  await HodimKerakState.ish_vaqti.set()

@dp.message_handler(content_types=['text'], state=HodimKerakState.ish_vaqti)
async def hodim_kerak_ish_vaqti_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(ish_vaqti=text)

  context = """💰 Maoshni kiriting?"""
  await message.answer(context)
  await HodimKerakState.maosh.set()

@dp.message_handler(content_types=['text'], state=HodimKerakState.maosh)
async def hodim_kerak_maosh_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(maosh=text)

  context = """‼️ Qo`shimcha ma`lumotlar?"""
  await message.answer(context)
  await HodimKerakState.info.set()

@dp.message_handler(content_types=['text'], state=HodimKerakState.info)
async def hodim_kerak_info_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(info=text)

  info = await state.get_data()
  context = f"""<b>Xodim kerak:</b>

🏢 Idora: <b>{info["idora"]}</b>
📚 Texnologiya: <b>{info["texnologiya"]}</b> 
🇺🇿 Telegram: <b>@{message.from_user.username}</b> 
📞 Aloqa: <b>{info["aloqa"]}</b>
🌐 Hudud: <b>{info["hudud"]}</b> 
✍️ Mas'ul: <b>{info["fio"]}</b>
🕰 Murojaat vaqti: <b>{info["murojat_vaqti"]}</b> 
🕰 Ish vaqti: <b>{info["ish_vaqti"]}</b>
💰 Maosh: <b>{info["maosh"]}</b>
‼️ Qo`shimcha: <b>{info["info"]}</b>

#ishJoyi"""
  await message.answer(context)
  await state.finish()

#############################----------UstozKerak----------###############################
@dp.message_handler(text='Ustoz kerak')
async def ish_joyi_kerak_handler(message: types.Message):
  context = """<b>Ustoz topish uchun ariza berish</b>

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi."""
  await message.answer(context)
  await message.answer("<b>Ism, familiyangizni kiriting?</b>")

  await UstozKerakState.fio.set()


@dp.message_handler(content_types=['text'], state=UstozKerakState.fio)
async def ustoz_kerak_fio_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(fio=text)

  context = """<b>🕑 Yosh:</b> 

Yoshingizni kiriting?
Masalan, 19"""
  await message.answer(context)
  await UstozKerakState.age.set()

@dp.message_handler(content_types=['text'], state=UstozKerakState.age)
async def ustoz_kerak_age_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(age=text)

  context = """<b>📚 Texnologiya:</b>

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#"""
  await message.answer(context)
  await UstozKerakState.texnologiya.set()

@dp.message_handler(content_types=['text'], state=UstozKerakState.texnologiya)
async def ustoz_kerak_texnologiya_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(texnologiya=text)

  context = """📞 <b>Aloqa:</b> 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67"""
  await message.answer(context)
  await UstozKerakState.aloqa.set()

@dp.message_handler(content_types=['text'], state=UstozKerakState.aloqa)
async def ustoz_aloqa_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(aloqa=text)

  context = """<b>🌐 Hudud:</b> 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting."""
  await message.answer(context)
  await UstozKerakState.hudud.set()

@dp.message_handler(content_types=['text'], state=UstozKerakState.hudud)
async def ustoz_kerak_hudud_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(hudud=text)

  context = """<b>💰 Narxi:</b>

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?"""
  
  await message.answer(context)
  await UstozKerakState.narxi.set()

@dp.message_handler(content_types=['text'], state=UstozKerakState.narxi)
async def ustoz_kerak_narxi_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(narxi=text)
  
  context = """<b>👨🏻‍💻 Kasbi:</b> 

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba"""
  await message.answer(context)
  await UstozKerakState.kasbi.set()

@dp.message_handler(content_types=['text'], state=UstozKerakState.kasbi)
async def ustoz_kerak_kasbi_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(kasbi=text)

  context = """<b>🕰 Murojaat qilish vaqti:</b> 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00"""
  await message.answer(context)
  await UstozKerakState.murojat_vaqti.set()

@dp.message_handler(content_types=['text'], state=UstozKerakState.murojat_vaqti)
async def ustoz_kerak_vaqti_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(vaqti=text)

  context = """<b>🔎 Maqsad:</b> 

Maqsadingizni qisqacha yozib bering."""
  await message.answer(context)
  await UstozKerakState.maqsad.set()

@dp.message_handler(content_types=['text'], state=UstozKerakState.maqsad)
async def ustoz_kerak_maqsad_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(maqsad=text)

  info = await state.get_data()
  context = f"""<b>Ustoz kerak:</b>

🎓 Shogird: <b>{info["fio"]}</b>
🌐 Yosh: <b>{info["age"]}</b>
📚 Texnologiya: <b>{info["texnologiya"]}</b>
🇺🇿 Telegram:  <b>@{message.from_user.username}</b>
📞 Aloqa: <b>{info["aloqa"]}</b>
🌐 Hudud: <b>{info["hudud"]}</b> 
💰 Narxi: <b>{info["narxi"]}</b> 
👨🏻‍💻 Kasbi: <b>{info["kasbi"]}</b>
🕰 Murojaat qilish vaqti: <b>{info["vaqti"]}</b>
🔎 Maqsad: <b>{info["maqsad"]}</b> 

#ustoz"""
  await message.answer(context)
  await state.finish()

#####################################----------ShogirtKerak----------##########################################
@dp.message_handler(text='Shogird kerak')
async def shogird_kerak_handler(message: types.Message):
  context = """<b>Shogird topish uchun ariza berish</b>

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi."""
  await message.answer(context)
  await message.answer("<b>Ism, familiyangizni kiriting?</b>")

  await ShogirtKerakState.fio.set()


@dp.message_handler(content_types=['text'], state=ShogirtKerakState.fio)
async def shogird_kerak_fio_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(fio=text)

  context = """<b>🕑 Yosh:</b> 

Yoshingizni kiriting?
Masalan, 19"""
  await message.answer(context)
  await ShogirtKerakState.age.set()

@dp.message_handler(content_types=['text'], state=ShogirtKerakState.age)
async def shogird_kerak_age_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(age=text)

  context = """<b>📚 Texnologiya:</b>

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#"""
  await message.answer(context)
  await ShogirtKerakState.texnologiya.set()

@dp.message_handler(content_types=['text'], state=ShogirtKerakState.texnologiya)
async def shogird_kerak_texnologiya_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(texnologiya=text)

  context = """📞 <b>Aloqa:</b> 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67"""
  await message.answer(context)
  await ShogirtKerakState.aloqa.set()

@dp.message_handler(content_types=['text'], state=ShogirtKerakState.aloqa)
async def shogirt_aloqa_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(aloqa=text)

  context = """<b>🌐 Hudud:</b> 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting."""
  await message.answer(context)
  await ShogirtKerakState.hudud.set()

@dp.message_handler(content_types=['text'], state=ShogirtKerakState.hudud)
async def shogird_kerak_hudud_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(hudud=text)

  context = """<b>💰 Narxi:</b>

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?"""
  
  await message.answer(context)
  await ShogirtKerakState.narxi.set()

@dp.message_handler(content_types=['text'], state=ShogirtKerakState.narxi)
async def shogird_kerak_narxi_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(narxi=text)
  
  context = """<b>👨🏻‍💻 Kasbi:</b> 

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba"""
  await message.answer(context)
  await ShogirtKerakState.kasbi.set()

@dp.message_handler(content_types=['text'], state=ShogirtKerakState.kasbi)
async def shogird_kerak_kasbi_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(kasbi=text)

  context = """<b>🕰 Murojaat qilish vaqti:</b> 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00"""
  await message.answer(context)
  await ShogirtKerakState.murojat_vaqti.set()

@dp.message_handler(content_types=['text'], state=ShogirtKerakState.murojat_vaqti)
async def shogird_kerak_vaqti_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(vaqti=text)

  context = """<b>🔎 Maqsad:</b> 

Maqsadingizni qisqacha yozib bering."""
  await message.answer(context)
  await ShogirtKerakState.maqsad.set()

@dp.message_handler(content_types=['text'], state=ShogirtKerakState.maqsad)
async def ustoz_kerak_maqsad_state(message: types.Message, state: FSMContext):
  text = message.text
  await state.update_data(maqsad=text)

  info = await state.get_data()
  context = f"""<b>Shogird kerak:</b>

🎓 Ustoz: <b>{info["fio"]}</b>
🌐 Yosh: <b>{info["age"]}</b>
📚 Texnologiya: Sadfg 
🇺🇿 Telegram: <b>@{message.from_user.username}</b> 
📞 Aloqa: <b>{info["aloqa"]}</b>
🌐 Hudud: <b>{info["hudud"]}</b> 
💰 Narxi: <b>{info["narxi"]}</b> 
👨🏻‍💻 Kasbi: <b>{info["kasbi"]}</b> 
🕰 Murojaat qilish vaqti: <b>{info["vaqti"]}</b> 
🔎 Maqsad: <b>{info["maqsad"]}</b> 

#shogird"""
  await message.answer(context)
  await state.finish()


if __name__ == "__main__":
  executor.start_polling(dp, on_startup=command_menu)