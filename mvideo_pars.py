import requests
import json


def error_checker(status_code):
    if status_code == 200:
        print('request succesful')
    else:
        print(f'request has a problems. status code = {status_code}')


def data_getter():
    # taking product`s ids
    cookies = {
        '__lhash_': 'f636d5938c20485be52a5827d947fcf2',
        'CACHE_INDICATOR': 'false',
        'COMPARISON_INDICATOR': 'false',
        'HINTS_FIO_COOKIE_NAME': '2',
        'MVID_2_exp_in_1': '2',
        'MVID_AB_SERVICES_DESCRIPTION': 'var2',
        'MVID_ADDRESS_COMMENT_AB_TEST': '2',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'false',
        'MVID_CART_MULTI_DELETE': 'false',
        'MVID_CATALOG_STATE': '1',
        'MVID_CHECKOUT_REGISTRATION_AB_TEST': '2',
        'MVID_CITY_ID': 'CityCZ_2128',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_GIFT_KIT': 'true',
        'MVID_GUEST_ID': '20977738510',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '2300000100000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '1',
        'MVID_MCLICK': 'true',
        'MVID_MOBILE_FILTERS': 'false',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_NEW_SUGGESTIONS': 'true',
        'MVID_REGION_ID': '11',
        'MVID_REGION_SHOP': 'S911',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'new',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_WEBP_ENABLED': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'flacktory': 'no',
        'searchType2': '1',
        'utm_term': '%D0%BC%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%20%D0%BA%D0%B0%D1%82%D0%B0%D0%BB%D0%BE%D0%B3%20%D0%B2%D0%BE%D0%BB%D0%B3%D0%BE%D0%B3%D1%80%D0%B0%D0%B4',
        'admitad_uid': '%D0%BC%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%20%D0%BA%D0%B0%D1%82%D0%B0%D0%BB%D0%BE%D0%B3%20%D0%B2%D0%BE%D0%BB%D0%B3%D0%BE%D0%B3%D1%80%D0%B0%D0%B4',
        '__sourceid': 'yandex',
        '__allsource': 'yandex',
        '__cpatrack': 'yandex_cpc',
        'authError': '',
        'SMSError': '',
        'partnerSrc': 'yandex',
        '_ym_uid': '1656686542935965514',
        '_ym_d': '1656686542',
        'tmr_lvidTS': '1656686542587',
        'tmr_lvid': 'ccdf4fa227b99257f8cd1ac905780532',
        'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
        '_gid': 'GA1.2.2131520862.1656686543',
        'st_uid': 'd69d47609e81fd47299f5fe3a6c16bea',
        'advcake_track_id': 'f2754e2b-7aa3-58fc-f85f-b23019f413a1',
        'advcake_click_id': '',
        'advcake_utm_webmaster': 'pid%7C10489666877_%7Ccid%7C28926497%7Cgid%7C2827215028%7Caid%7C4634042841%7Cpos%7Cpremium1%7Ckey%7C%25D0%25BC%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%2520%25D0%25BA%25D0%25B0%25D1%2582%25D0%25B0%25D0%25BB%25D0%25BE%25D0%25B3%2520%25D0%25B2%25D0%25BE%25D0%25BB%25D0%25B3%25D0%25BE%25D0%25B3%25D1%2580%25D0%25B0%25D0%25B4%7Caddphrases%7Cno%7Cdvc%7Cdesktop%7Cregion%7C38%7Cregion_name%7C%25D0%2592%25D0%25BE%25D0%25BB%25D0%25B3%25D0%25BE%25D0%25B3%25D1%2580%25D0%25B0%25D0%25B4%7Ccoef_goal%7C0%7Cdesktop',
        'advcake_utm_partner': 'ipr_Volgograd_image_name_geo_search',
        'advcake_track_url': 'https%3A%2F%2Fwww.mvideo.ru%2F%3Futm_source%3Dyandex%26utm_medium%3Dcpc%26utm_campaign%3Dipr_Volgograd_image_name_geo_search%26utm_content%3Dpid%7C10489666877_%7Ccid%7C28926497%7Cgid%7C2827215028%7Caid%7C4634042841%7Cpos%7Cpremium1%7Ckey%7C%25D0%25BC%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%2520%25D0%25BA%25D0%25B0%25D1%2582%25D0%25B0%25D0%25BB%25D0%25BE%25D0%25B3%2520%25D0%25B2%25D0%25BE%25D0%25BB%25D0%25B3%25D0%25BE%25D0%25B3%25D1%2580%25D0%25B0%25D0%25B4%7Caddphrases%7Cno%7Cdvc%7Cdesktop%7Cregion%7C38%7Cregion_name%7C%25D0%2592%25D0%25BE%25D0%25BB%25D0%25B3%25D0%25BE%25D0%25B3%25D1%2580%25D0%25B0%25D0%25B4%7Ccoef_goal%7C0%7Cdesktop%26utm_term%3D%25D0%25BC%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%2520%25D0%25BA%25D0%25B0%25D1%2582%25D0%25B0%25D0%25BB%25D0%25BE%25D0%25B3%2520%25D0%25B2%25D0%25BE%25D0%25BB%25D0%25B3%25D0%25BE%25D0%25B3%25D1%2580%25D0%25B0%25D0%25B4%26reff%3Dyandex_cpc_ipr_Volgograd_image_name_geo_search%26yadclid%3D34164872%26yadordid%3D16323953%26yclid%3D9127353154490073087',
        'advcake_session_id': '8d08a259-9134-a1f1-1af2-f767b0a37b12',
        '_ym_isad': '1',
        'flocktory-uuid': 'b62efaf6-74bf-43f9-a508-57f4f11d4469-9',
        'uxs_uid': '04c4f490-f94c-11ec-a83d-7350b3035dec',
        'afUserId': 'ff83b1f5-8a44-405c-afe9-5d5f8f8c36e2-p',
        'BIGipServeratg-ps-prod_tcp80': '1141169162.20480.0000',
        'bIPs': '-826759811',
        'AF_SYNC': '1656686543633',
        '__SourceTracker': 'yandex.ru__organic',
        'admitad_deduplication_cookie': 'yandex.ru__organic',
        '__ttl__widget__ui': '1656687099604-88d7217ad187',
        '_ga': 'GA1.2.834949151.1656686542',
        'mindboxDeviceUUID': 'bbb73008-db21-418c-9569-cc3c1f1e5bc9',
        'directCrm-session': '%7B%22deviceGuid%22%3A%22bbb73008-db21-418c-9569-cc3c1f1e5bc9%22%7D',
        'tmr_detect': '0%7C1656687260281',
        'tmr_reqNum': '24',
        'JSESSIONID': 'FWxnv1cBFj1fyyT4hjmHr4Q2HGCcsLJpTwyPVcFy6dB75CP3vWKG!7213203',
        'MVID_ENVCLOUD': 'prod2',
        '_ga_CFMZTSS5FM': 'GS1.1.1656691808.2.0.1656691808.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1656691808.2.0.1656691808.60',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        # Requests sorts cookies= alphabetically
        # 'cookie': '__lhash_=f636d5938c20485be52a5827d947fcf2; CACHE_INDICATOR=false; COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=2; MVID_2_exp_in_1=2; MVID_AB_SERVICES_DESCRIPTION=var2; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=false; MVID_CART_MULTI_DELETE=false; MVID_CATALOG_STATE=1; MVID_CHECKOUT_REGISTRATION_AB_TEST=2; MVID_CITY_ID=CityCZ_2128; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GUEST_ID=20977738510; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=2300000100000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=1; MVID_MCLICK=true; MVID_MOBILE_FILTERS=false; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_NEW_SUGGESTIONS=true; MVID_REGION_ID=11; MVID_REGION_SHOP=S911; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TAXI_DELIVERY_INTERVALS_VIEW=new; MVID_TIMEZONE_OFFSET=3; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; flacktory=no; searchType2=1; utm_term=%D0%BC%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%20%D0%BA%D0%B0%D1%82%D0%B0%D0%BB%D0%BE%D0%B3%20%D0%B2%D0%BE%D0%BB%D0%B3%D0%BE%D0%B3%D1%80%D0%B0%D0%B4; admitad_uid=%D0%BC%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%20%D0%BA%D0%B0%D1%82%D0%B0%D0%BB%D0%BE%D0%B3%20%D0%B2%D0%BE%D0%BB%D0%B3%D0%BE%D0%B3%D1%80%D0%B0%D0%B4; __sourceid=yandex; __allsource=yandex; __cpatrack=yandex_cpc; authError=; SMSError=; partnerSrc=yandex; _ym_uid=1656686542935965514; _ym_d=1656686542; tmr_lvidTS=1656686542587; tmr_lvid=ccdf4fa227b99257f8cd1ac905780532; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; _gid=GA1.2.2131520862.1656686543; st_uid=d69d47609e81fd47299f5fe3a6c16bea; advcake_track_id=f2754e2b-7aa3-58fc-f85f-b23019f413a1; advcake_click_id=; advcake_utm_webmaster=pid%7C10489666877_%7Ccid%7C28926497%7Cgid%7C2827215028%7Caid%7C4634042841%7Cpos%7Cpremium1%7Ckey%7C%25D0%25BC%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%2520%25D0%25BA%25D0%25B0%25D1%2582%25D0%25B0%25D0%25BB%25D0%25BE%25D0%25B3%2520%25D0%25B2%25D0%25BE%25D0%25BB%25D0%25B3%25D0%25BE%25D0%25B3%25D1%2580%25D0%25B0%25D0%25B4%7Caddphrases%7Cno%7Cdvc%7Cdesktop%7Cregion%7C38%7Cregion_name%7C%25D0%2592%25D0%25BE%25D0%25BB%25D0%25B3%25D0%25BE%25D0%25B3%25D1%2580%25D0%25B0%25D0%25B4%7Ccoef_goal%7C0%7Cdesktop; advcake_utm_partner=ipr_Volgograd_image_name_geo_search; advcake_track_url=https%3A%2F%2Fwww.mvideo.ru%2F%3Futm_source%3Dyandex%26utm_medium%3Dcpc%26utm_campaign%3Dipr_Volgograd_image_name_geo_search%26utm_content%3Dpid%7C10489666877_%7Ccid%7C28926497%7Cgid%7C2827215028%7Caid%7C4634042841%7Cpos%7Cpremium1%7Ckey%7C%25D0%25BC%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%2520%25D0%25BA%25D0%25B0%25D1%2582%25D0%25B0%25D0%25BB%25D0%25BE%25D0%25B3%2520%25D0%25B2%25D0%25BE%25D0%25BB%25D0%25B3%25D0%25BE%25D0%25B3%25D1%2580%25D0%25B0%25D0%25B4%7Caddphrases%7Cno%7Cdvc%7Cdesktop%7Cregion%7C38%7Cregion_name%7C%25D0%2592%25D0%25BE%25D0%25BB%25D0%25B3%25D0%25BE%25D0%25B3%25D1%2580%25D0%25B0%25D0%25B4%7Ccoef_goal%7C0%7Cdesktop%26utm_term%3D%25D0%25BC%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%2520%25D0%25BA%25D0%25B0%25D1%2582%25D0%25B0%25D0%25BB%25D0%25BE%25D0%25B3%2520%25D0%25B2%25D0%25BE%25D0%25BB%25D0%25B3%25D0%25BE%25D0%25B3%25D1%2580%25D0%25B0%25D0%25B4%26reff%3Dyandex_cpc_ipr_Volgograd_image_name_geo_search%26yadclid%3D34164872%26yadordid%3D16323953%26yclid%3D9127353154490073087; advcake_session_id=8d08a259-9134-a1f1-1af2-f767b0a37b12; _ym_isad=1; flocktory-uuid=b62efaf6-74bf-43f9-a508-57f4f11d4469-9; uxs_uid=04c4f490-f94c-11ec-a83d-7350b3035dec; afUserId=ff83b1f5-8a44-405c-afe9-5d5f8f8c36e2-p; BIGipServeratg-ps-prod_tcp80=1141169162.20480.0000; bIPs=-826759811; AF_SYNC=1656686543633; __SourceTracker=yandex.ru__organic; admitad_deduplication_cookie=yandex.ru__organic; __ttl__widget__ui=1656687099604-88d7217ad187; _ga=GA1.2.834949151.1656686542; mindboxDeviceUUID=bbb73008-db21-418c-9569-cc3c1f1e5bc9; directCrm-session=%7B%22deviceGuid%22%3A%22bbb73008-db21-418c-9569-cc3c1f1e5bc9%22%7D; tmr_detect=0%7C1656687260281; tmr_reqNum=24; JSESSIONID=FWxnv1cBFj1fyyT4hjmHr4Q2HGCcsLJpTwyPVcFy6dB75CP3vWKG!7213203; MVID_ENVCLOUD=prod2; _ga_CFMZTSS5FM=GS1.1.1656691808.2.0.1656691808.0; _ga_BNX5WPP3YK=GS1.1.1656691808.2.0.1656691808.60',
        'referer': 'https://www.mvideo.ru/product-list-page?q=%D0%BC%D0%BE%D0%BD%D0%B8%D1%82%D0%BE%D1%80%D1%8B&category=101',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'x-set-application-id': '91b29288-79a4-44f2-a071-c3f78d0c4993',
    }

    params = {
        'query': 'мониторы',
        'categoryId': '101',
        'offset': '0',
        'limit': '24',
        'filterParams': 'WyJ0b2xrby12LW5hbGljaGlpIiwiLTEyIiwiZGEiXQ==',
        'doTranslit': 'true',
        'context': 'eyJxdWVyeSI6IjIzNDkzIiwic2hvcElkcyI6WyJTOTExIl0sInN0cmF0ZWd5SWQiOiJzdGVwMiIsImhpZGRlbkZpcnN0R3JvdXAiOltdLCJmaXJzdEdyb3VwIjpbXSwicmVzcG9uc2VUeXBlIjoicGxhaW4iLCJiaVN0YXRzIjp7fX0=',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/search', params=params, cookies=cookies,
                            headers=headers)
    error_checker(response.status_code)

    product_ids = response.json().get('body').get('products')
    with open('products_id.json', 'w') as file:
        json.dump(product_ids, file, indent=4, ensure_ascii=False)

    json_data = {
        'productIds': product_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                             json=json_data).json()
    products_info = response.get('body').get('products')
    with open('products_info.json', 'w') as file:
        json.dump(products_info, file, indent=4, ensure_ascii=False)
    print('products id created')

    params = {
        'productIds': '30051364,30059510,30059511,30054149,30059512,30041167,30056080,30057503,30058309,30058318,30054775,30058870,30039349,30054970,30056697,30058317,30059579,30057804,30057915,30050968,30059738,30054328,30051548,30048375',
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
                            headers=headers).json()
    products_price = response.get('body').get('materialPrices')

    prices = {}
    for elem in products_price:
        current_id = elem['productId']
        current_price = elem['price']['salePrice']
        prices[current_id] = current_price

    for elem in products_info:
        current_id = elem['productId']
        elem['price'] = prices[current_id]

    with open('products_list.json', 'w') as file:
        json.dump(products_info, file, indent=4, ensure_ascii=False)

    print('products list created')


def main():
    data_getter()


if __name__ == '__main__':
    main()
