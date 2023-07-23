import requests
import configuration
import data

# Павел Адамов 6-я когорта - финальный проекта. Инженер по тестированию plus
def post_new_order(body):
    return requests.post(configuration.URL + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)

def get_info_orders(track):
    return requests.get(configuration.URL + configuration.CREATE_ORDER_PATH + "/track?t="+track,
                         headers=data.headers)


response = post_new_order(data.user_body);

if response.status_code == 201:
    order_track = response.text.split(":")[1].split("}")[0]

    response_track = get_info_orders(order_track)

    if response_track.status_code == 200:
        print('code: 200')
    else:
        print('Возвращенный код отличается от 200 и равен ', str(response_track.status_code))

    print(response_track.text)

else:
    print('fnc get_info_orders return ' + str(response.status_code) + ' status code')









