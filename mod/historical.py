from utils.config_loader import Config
from binance.client import Client
import pytz


class BnHistory(Config):

    def __init__(self):
        super(Config, self).__init__()
        self.client = None
        self.period_map = None
        self.data_format = None

    def initial(self):
        self.load_config()
        self.client = Client(
            self.CONFIG.BINANCE.api_key,
            self.CONFIG.BINANCE.secret_key
        )
        self.period_map = {
            '1m': Client.KLINE_INTERVAL_1MINUTE,
            '5m': Client.KLINE_INTERVAL_5MINUTE,
            '15m': Client.KLINE_INTERVAL_15MINUTE,
            '30m': Client.KLINE_INTERVAL_30MINUTE,
            '1h': Client.KLINE_INTERVAL_1HOUR,
            '4h': Client.KLINE_INTERVAL_4HOUR,
            '1d': Client.KLINE_INTERVAL_1DAY
        }
        self.data_format = [
            'open_time', 'open', 'high', 'low', 'close', 'volume',
            'close_time', 'quote_asset_volume', 'number_of_trades',
            'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume',
            'ignore'
                            ]

    def get_kline(self, period, start='', end=''):
        if period not in self.period_map.keys():
            raise ValueError(f"params error,period: {period}")
        gen = self.client.get_historical_klines_generator(
            "BTCUSDT", self.period_map.get(period), start, end_str=end
        )
        return gen


if __name__ == '__main__':
    import datetime
    instance = BnHistory()
    instance.initial()
    gen = instance.get_kline(period='1m', start='2020-01-01 15:01:00+08:00', end='2020-01-01 15:02:00+08:00')
    for one in gen:
        print(dict(zip(instance.data_format, one)))
        print(datetime.datetime.fromtimestamp(one[0]/1000), one[1:])