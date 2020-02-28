from alpha_vantage.timeseries import TimeSeries
import json
import os
from datetime import datetime
import pymysql


class getStockData():
    def __init__(self, symbols):
        self.key = 'LLDB7JEVIFVJ5JOM'
        self.symbols = symbols
        self.ts = TimeSeries(self.key)

    def get_historical_data(self):
        data_list = []
        for symbol in self.symbols:
            data, meta_data = self.ts.get_daily(symbol)
            self.collect_stock(symbol + "_hist", data)

            for time, info in data.items():
                format_str = '%Y-%m-%d'
                time = datetime.strptime(time, format_str).date()
                tmp = {'symbol': symbol,
                       'time': time,
                       'open': float(info['1. open']),
                       'high': float(info['2. high']),
                       'low': float(info['3. low']),
                       'close': float(info['4. close']),
                       'volume': int(info['5. volume'])}
                data_list.append(tmp)
        # print(data_list)
        # print(type(data_list))
        return data_list

    def get_realtime_data(self):
        data_list = []
        for symbol in self.symbols:
            data, meta_data = self.ts.get_intraday(symbol, interval='1min')
            self.collect_stock(symbol + "_real", data)

            for time, info in data.items():
                format_str = '%Y-%m-%d %H:%M:%S'
                time = datetime.strptime(time, format_str)
                tmp = {'symbol': symbol,
                       'time': time,
                       'price': float(info['4. close']),
                       'volume': int(info['5. volume'])}
                data_list.append(tmp)
        return data_list

    def collect_stock(self, symbol, data):
        datapath = "./stockdata/" + symbol + ".json"
        os.makedirs(os.path.dirname(datapath), exist_ok=True)

        with open(datapath, "w") as outfile:
            json.dump(data, outfile, indent=4)

    def store_historical_data(self, data_list):
        conn = pymysql.connect("localhost", "root", "mysql", "ece568project")
        cursor = conn.cursor()
        for i, item in enumerate(data_list):
            cursor.execute("INSERT INTO historical (symbol, time, open, high, low, close, volume) "
                           "VALUES(%s, %s, %s, %s, %s, %s, %s)", (item['symbol'], item['time'],
                           item['open'], item['high'], item['low'], item['close'], item['volume']))
        conn.commit()
        conn.close()

    def store_realtime_data(self, data_list):
        conn = pymysql.connect("localhost", "root", "mysql", "ece568project")
        cursor = conn.cursor()
        for i, item in enumerate(data_list):
            cursor.execute("INSERT INTO realtime (symbol, time, price, volume) "
                           "VALUES(%s, %s, %s, %s)", (item['symbol'], item['time'], item['price'],
                                                                  item['volume']))
        conn.commit()
        conn.close()

if __name__ == '__main__':

   data = getStockData(['GOOG', 'FB']).get_realtime_data()
   getStockData(['GOOG', 'FB']).store_realtime_data(data)