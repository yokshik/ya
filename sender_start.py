import requests
import configuration
import data

# Павел Адамов 6-я когорта - финальный проекта. Инженер по тестированию plus
def post_new_order(body):
    return requests.post(configuration.URL + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)

def get_info_orders(track):
    return requests.get(configuration.URL + configuration.CREATE_ORDER_PATH + f"/track?t={track}",
                        headers=data.headers)


def test_get_order_by_track():
    response = post_new_order(data.user_body)
    assert response.status_code == 201

    order_track = response.json()["track"]

    response_track = get_info_orders(order_track)
    assert response_track.status_code == 200

    print('code: 200')
    print(response_track.text)


test_get_order_by_track()









