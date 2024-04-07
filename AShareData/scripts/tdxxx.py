from pytdx.hq import TdxHq_API
from pytdx.params import TDXParams
import datetime as dt
api = TdxHq_API()
# num_days = dt.date.today() - dt.timedelta(days=300)
## 2023-02-20
num_days=365*3
start_index = num_days * 60 * 4
print(start_index)
#
with api.connect('119.147.212.81', 7709):
    data = api.get_security_bars(category=TDXParams.KLINE_TYPE_1MIN, market=0, code='000001', start=22320, count=240)  # 返回普通list
    print(data)