import logging
from logging import Handler, handlers
from multiprocessing import context
import os
from signal import Handlers
import requests
import time
import string
import random
from urllib.request import urlopen
import json
import string
import random

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint



from aiogram import Bot, Dispatcher, executor, types
from bs4 import BeautifulSoup


##
uniproxy = requests.session()
uniproxy.proxies = uniproxy 
##

proxys = {
    'http':'http://xvpdohon-rotate:j3hvas2j91cd@p.webshare.io:80/',
    'https': 'http://bnvudhvm-rotate:jkgnyp9lecnr@p.webshare.io:80/',
    'https':'http://kpsldceh-rotate:58keli6fhazy@p.webshare.io:80/',
    'https':'http://urzeqtzv-rotate:f24yk1gwccta@p.webshare.io:80/',
    'https':'http://oiinvlnx-rotate:r2lx2vr4jbjo@p.webshare.io:80/',
    'https':'http://xvpdohon-rotate:j3hvas2j91cd@p.webshare.io:80/',
    'https':'http://bnvudhvm-rotate:jkgnyp9lecnr@p.webshare.io:80/',
    'https':'http://kpsldceh-rotate:58keli6fhazy@p.webshare.io:80/',
    'https':'http://urzeqtzv-rotate:f24yk1gwccta@p.webshare.io:80/',
    'https':'http://oiinvlnx-rotate:r2lx2vr4jbjo@p.webshare.io:80/',
    'https':'http://hftsdyhr-rotate:iziwp0qs6av1@p.webshare.io:80/'}


comand = "/.,*"
bot = bool(os.environ.get('bot', True))
token = os.environ.get("token", None)

bot = Bot(token="6188249734:AAH0h51am6PcCseOo1OgfFvpo0BKj8LTJks", parse_mode=types.ParseMode.HTML)
iniciar = Dispatcher(bot)

button1 = InlineKeyboardButton(text="𝗢𝘄𝗻𝗲𝗿", callback_data="creador")
button2 = InlineKeyboardButton(text="𝗚𝗮𝘁𝗲𝘀", callback_data="gate")
button3 = InlineKeyboardButton(text="𝗠𝘆 𝗦𝗰𝗿𝗮𝗽𝗽𝗲𝗿", callback_data="randomvalue_of10")
keyboard_inline = InlineKeyboardMarkup().add(button1, button2, button3)

admins = [5629056050, 5019536742]



@iniciar.callback_query_handler(text=["randomvalue_of10", "creador", "gate"])
async def random_value(call: types.CallbackQuery):
    if call.data == "creador":
        await call.message.answer("☘ 𝗢𝘄𝗻𝗲𝗿 𝗕𝗼𝘁 ☘: @DiegoAkk")
    if call.data == "gate":
        await call.message.answer("""
<b>🛠 𝗚𝗮𝘁𝗲𝘀 𝗱𝗲𝗹 𝗕𝗼𝘁 🛠 </b>

🔵 [🝂] /auth: **Stripe Charged Auth** | Status: On ✅        
🟡 [🝂] /stp: **Stripe Auth** | Status: On ✅

                        
                        """)
    elif call.data == "randomvalue_of10":
        await call.message.answer("💰UNETE A NUESTRO SCRAPPER GRATUITO: @KURAMAVIPSCRAPPER💰")
    await call.answer()


########################## COMDANDO START ################################


@iniciar.message_handler(commands=['start'])
async def start_answer(message: types.Message):
    await message.answer_photo('https://imgur.com/ZO72OAT', "a", reply_markup=keyboard_inline)


########################## FIN COMANDO START ################################


########################## COMANDO CMDS ################################


@iniciar.message_handler(commands=["cmds"], commands_prefix=comand)
async def cmds(message: types.Message):
    cmd = await message.reply("<b>LISTA DE COMANDOS 𝐊𝐔𝐑𝐀𝐌𝐀 𝐂𝐇𝐊 </b>")
    time.sleep(1)
    await cmd.edit_text("""
𝗠𝗶𝘀 𝗰𝗼𝗺𝗮𝗻𝗱𝗼𝘀 𝘀𝗼𝗻

○ /cmds  ✅
○ /gates ✅
○ /bin ✅

                        """)
                        
########################## FIN COMANDO CMDS ################################




########################## COMDANDO GATES ################################


@iniciar.message_handler(commands=["gates"], commands_prefix=comand)
async def gates(message: types.Message):
    cmd = await message.reply("<b>LISTA DE COMANDOS 𝐊𝐔𝐑𝐀𝐌𝐀 𝐂𝐇𝐊 </b>")
    time.sleep(1)
    await cmd.edit_text("""
<b>🛠 𝗚𝗮𝘁𝗲𝘀 𝗱𝗲𝗹 𝗕𝗼𝘁 🛠 </b>

🔵 [🝂] /auth: <b>Stripe Charged Auth</b> | <b>Status: Off</b> ❌        
🟡 [🝂] /stp: <b>Stripe Auth</b> | <b>Status: Off</b> ❌          
                                       
                        """)
########################## FIN COMANDO GATES ################################


########################## INFO BIN ################################

@iniciar.message_handler(commands=['bin'], commands_prefix=comand)
async def helpstr(message: types.Message):
    await message.answer_chat_action("typing")
    BIN = message.text[len("/bin "): 11]
    if len(BIN) < 6:
        return await message.reply("<b>❗️ ERROR INGRESE BIEN EL BIN  ❗️</b>")
    if not BIN:
        return await message.reply("Did u Really Know how to use me.")
    bin1 = await message.reply(f"<b>💳BIN: {BIN}\nᴘʀᴏᴄᴇss: [🔴]</b>")
    apis1 = uniproxy.get(f"https://projectslost.xyz/bin/?bin={BIN}").json()
    ID = message.from_user.id
    FIRST = message.from_user.first_name
    result=apis1['status']
    banke=apis1['bank']
    bank=banke['name']
    brand=apis1['brand']
    bn=apis1['query']
    typ=apis1['type']
    lv=apis1['level']
    country1=apis1['country']
    country=country1['name']
    
    
    bin2 = await bin1.edit_text(f"<b>💳BIN: {BIN}\nᴘʀᴏᴄᴇss: [🔴][🟡]</b>")
    time.sleep(1)
    bin3 = await bin2.edit_text(f"<b>💳BIN: {BIN}\nᴘʀᴏᴄᴇss: [🔴][🟡][🟢]</b>")

    await bin3.edit_text(f"""
[ϟ] <b>Bin Lookup</b>
━━━━━━━━━━━━━
[Ϟ] <b>Bin</b>: {bn}
[Ϟ] <b>Vendor</b>: {brand}
[Ϟ] <b>Type</b>: {typ}
[Ϟ] <b>Level</b>: {lv}
[Ϟ] <b>Bank</b>: {bank}
[Ϟ] <b>Country</b>: {country}
━━━━━━━━━━━━━
<b>Checked By:</b> <a href="tg://user?id={ID}">{FIRST}</a>

""")

########################## FIN INFO BIN ################################



 ################## GATE AUTH ######################################   

@iniciar.message_handler(commands=["auth"], commands_prefix=comand)
async def auth(message: types.Message):
    ini = time.perf_counter()
    ccs = message.text[len('/auth '):]
    ccs1 = ccs
    if not ccs1:
        await message.reply("Gate Off ❌")
    
@iniciar.message_handler(commands=['stp'], commands_prefix=comand)
async def da(message: types.Message):
    contra = await message.reply("<b>ᴘʀᴏᴄᴇss: ❗ Comprobando acceso ❗</b>")
    time.sleep(1)
    user = message.from_user.id
    if user in admins :
        await contra.edit_text('Estas autorizado!')
    
    else:
        await contra.edit_text('❗ No tienes acceso para utilizar este comando. ❗ Contacta a @DiegoAkk.')
        return str;
    ini = time.perf_counter()
    ccs = message.text[len('/stp '):]
    
    if not ccs:
        await contra.edit_text("Gate Off ❌ ")



@iniciar.message_handler(commands=['pene'], commands_prefix=comand)  
async def pene(message: types.Message):
    contra = await message.reply("<b>ᴘʀᴏᴄᴇss: ❗ Comprobando acceso ❗</b>")
    time.sleep(1)
    user = message.from_user.id
    if user in admins :
        await contra.edit_text('Estas autorizado!')
    
    else:
        await contra.edit_text('❗ No tienes acceso para utilizar este comando. ❗ Contacta a @DiegoAkk.')
        return str;
    ini = time.perf_counter()
    ccs = message.text[len('/pene '):]   

    if not ccs:
        await contra.edit_text("❗ ERROR INGRESE BIEN LA TARJETA ❗")

    spli = ccs.split('|')
    cc = spli[0]
    mes = spli[1]
    ano = spli[2]
    cvv = spli[3]
    m1 = await contra.edit_text(f"<b>💳ᴄᴀʀᴅ: {ccs}\nᴘʀᴏᴄᴇss: [🔴]</b>")

    headels = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'accept': 'application/json',
    'content-type': 'application/x-www-form-urlencoded'
    }

    session = requests.session()

    api201 = session.post("https://api.stripe.com/v1/payment_intents/pi_3MbaLOJeGhFfMJgC1jwsOBWM/confirm", headers=headels).json()
    
    await message.reply(f"{api201}")

print("CODIGO EN LINEA")
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    executor.start_polling(iniciar, skip_updates=True)
    
