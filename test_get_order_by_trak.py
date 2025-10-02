# Флоренко Александр 35 когорта дипломчик
import sender_stand_reqoest

def test_get_order_by_trak():
    status = sender_stand_reqoest.get_order_status(sender_stand_reqoest.order_track)
    assert status == 200