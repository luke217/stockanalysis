from db_init import *
from get_stock import *

stocks = ['GOOG', 'FB']
create_db()
data_hist = getStockData(stocks).get_historical_data()
getStockData(stocks).store_historical_data(data_hist)
data_real = getStockData(stocks).get_realtime_data()
getStockData(stocks).store_realtime_data(data_real)