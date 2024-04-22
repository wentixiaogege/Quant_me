import tushare as ts
pro = ts.pro_api("d689cb3c1d8c8a618e49ca0bb64f4d6de2f70e28ab5f76a867b31ac7")

#提取000001全部复权因子
# df = pro.adj_factor(ts_code='000001.SZ', trade_date='')
# df = pro.adj_factor(trade_date='20240415')

# print(df[df.ts_code=='603377.SH'])

#sina数据
df = ts.realtime_quote(ts_code='600000.SH')

print(df)