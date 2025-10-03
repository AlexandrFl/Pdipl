# Флоренко Александр 35 когорта дипломчик
import data
import sender_stand_reqoest


def test_get_order_by_trak():
    order = sender_stand_reqoest.create_order(data.order)
    order_track = order["track"]
    print("2. Order track – ", order_track)
    status = sender_stand_reqoest.get_order_status(order_track)
    assert status.status_code == 200