import sys

import AShareData as asd
from update_routine import daily_routine

if __name__ == '__main__':
    # config_loc = sys.argv[1]
    config_loc = '../config.json'
    asd.set_global_config(config_loc)
    db_interface = asd.generate_db_interface_from_config(config_loc, init=True) ### 这里创建表
    print('ljj initing 00000')
    with asd.TushareData() as tushare_data:
        tushare_data.init_db()
    # print('ljj initing daily_routine')
    daily_routine(config_loc)
    # print('ljj initing SMBandHMLCompositor')
    # asd.model.SMBandHMLCompositor(asd.FamaFrench3FactorModel()).update()
    # print('ljj initing UMDCompositor')
    # asd.model.UMDCompositor(asd.FamaFrenchCarhart4FactorModel()).update()
    #
    ## 使用tushare 缺失 "CLAUSE_CONVERSION2_BONDLOT": "未转股余额" 字段
    # "可转债日行情": {
    #     "DateTime": "date",
    #     "ID": "varchar",
    #     "开盘价": "float",
    #     "最高价": "float",
    #     "最低价": "float",
    #     "收盘价": "float",
    #     "成交量": "float",
    #     "成交额": "double",
    #     "未转股余额": "double"
    # },
    ## 缺失可转债转股价表的数据
    #
    # "期货日行情": {
    #     "DateTime": "date",
    #     "ID": "varchar",
    #     "开盘价": "float",
    #     "最高价": "float",
    #     "最低价": "float",
    #     "收盘价": "float",
    #     "结算价": "float",
    #     "成交量": "float",
    #     "成交额": "double",
    #     "持仓量": "double"
    # },
    #
    # 	"期权日行情": {
	# 	"DateTime": "date",
	# 	"ID": "varchar",
	# 	"成交额": "double",
	# 	"开盘价": "float",
	# 	"最高价": "float",
	# 	"最低价": "float",
	# 	"收盘价": "float",
	# 	"成交量": "float",
	# 	"持仓量": "float",
	# 	"Delta": "float",
	# 	"Gamma": "float",
	# 	"Vega": "float",
	# 	"Theta": "float",
	# 	"Rho": "float"
	# },
    # "基金列表": {
    #     "ID": "varchar",
    #     "证券名称": "str",
    #     "全名": "str",
    #     "管理人": "varchar",
    #     "封闭式": "boolean",
    #     "投资类型": "varchar",
    #     "初始基金": "boolean",
    #     "分级基金": "boolean",
    #     "债券型": "boolean",
    #     "ETF": "boolean",
    #     "定开": "boolean",
    #     "定开时长(月)": "bigint",
    #     "封闭运作转LOF时长(月)": "bigint",
    #     "管理费率": "float",
    #     "浮动管理费": "boolean",
    #     "浮动管理费说明": "str",
    #     "托管费率": "float",
    #     "销售服务费率": "float",
    #     "前端申购费": "str",
    #     "后端申购费": "str",
    #     "最高申购费": "float",
    #     "赎回费": "str",
    #     "免赎回费持有期(日)": "bigint"
    # },