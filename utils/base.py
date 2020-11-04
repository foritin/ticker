import datetime


def ts_to_datetime(ts: int):
    assert isinstance(ts, int)
    if len(ts) == 13:
        return datetime.datetime.fromtimestamp(ts/1000)
