import requests
import json
from parser_config import headers, cookies, params_1, params_2, json_data


class ParserMvideo:
    @staticmethod
    def error_checker(status_code):
        if status_code == 200:
            print('request succesful')
        else:
            print(f'request has a problems. status code = {status_code}')

    def start(self):
        # taking product`s ids
        json_data['productIds'] = self.parser_id()
        # taking product`s info
        products_info = self.parser_products(json_data)
        # taking product`s prices
        products_price = self.parser_prices()
        prices = {}
        for elem in products_price:
            current_id = elem['productId']
            current_price = elem['price']['salePrice']
            prices[current_id] = current_price

        for elem in products_info:
            current_id = elem['productId']
            elem['price'] = prices[current_id]
        # saving list of products
        self.save_file("products_list", products_info)
        print('products list created')

    def parser_id(self):
        response = requests.get('https://www.mvideo.ru/bff/products/search', params=params_1, cookies=cookies,
                                headers=headers)
        self.error_checker(response.status_code)

        product_ids = response.json().get('body').get('products')
        self.save_file("products_id", product_ids)
        return product_ids

    def parser_products(self, json_data):
        response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                                 json=json_data).json()
        products_info = response.get('body').get('products')
        self.save_file("products_info", products_info)
        print('products id created')
        return products_info

    def parser_prices(self):
        response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params_2, cookies=cookies,
                                headers=headers).json()
        products_price = response.get('body').get('materialPrices')
        return products_price

    def save_file(self, name, data):
        with open(f'{name}.json', 'w') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)


def main():
    ParserMvideo().start()


if __name__ == '__main__':
    main()
