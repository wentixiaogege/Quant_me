import sys
import AShareData as asd


def daily_routine(config_loc: str):
    asd.set_global_config(config_loc)

    with asd.TushareData() as tushare_crawler:
        tushare_crawler.update_base_info() ### 各种维度的表和日期
        # tushare_crawler.get_shibor() # 2006-10-08    | 2024-04-11
        # tushare_crawler.get_ipo_info() # 2008-01-16    | 2024-04-08
        # tushare_crawler.get_company_info()
        # tushare_crawler.update_hs_holding() # 沪深港股通持股明细,2hour
        # tushare_crawler.get_hs_constitute() # 沪深股通成份股， tushare 已经不更新了
        #
        ### tushare_crawler.update_stock_names() ###数据来源港交所。update_base_info里面有了
        # tushare_crawler.update_dividend() # 1991-03-17    | 2024-03-08
        #
        # tushare_crawler.update_index_daily() #指数日行情
        ### tushare_crawler.update_stock_list_date() #### update_base_info 里面有了
        # 5张表 股票日行情+复权因子+总股本+流通股本+自由流通股本 --- 使用tushare的日线 wind的没有权限
        # tushare_crawler.update_hq_daily()

        # print('update_pause_stock_info')
        # tushare_crawler.update_pause_stock_info()# 股票停牌--- 使用tushare的日线 wind的没有权限

        print('update_hk_stock_daily')
        # tushare_crawler.update_hk_stock_daily() # 港股日行情
        # 更新基金列表--- 使用tushare的 wind的没有权限
        print('update_financial_data')
        # tushare_crawler.update_financial_data() ### 7张表
        # 合并资产负债表,财务指标
        # 母公司资产负债表, 母公司现金流量表 和 母公司利润表
        # 合并资产负债表, 合并现金流量表 和 合并利润表
        print('update_industry') ###### 使用爬虫吧，目前拿到的不全
        # tushare_crawler.update_industry() # ['中信', '申万', '中证', 'Wind'] 行业表 ---》 目前只有wind有 ？？？？？

        print('update_fund_list_date') ###
        # tushare_crawler.update_fund_list_date() #### update_base_info 里面有了
        # tushare_crawler.update_fund_portfolio() ### 公募基金持仓数据
        # tushare_crawler.update_fund_daily()
        # tushare_crawler.update_fund_dividend()

        # 可转债日行情--- 使用tushare的日线 wind的没有权限
        print('update_convertible_bond_daily_data')
        # tushare_crawler.update_convertible_bond_list_date()  # 可转债信息#### update_base_info 里面有了
        # tushare_crawler.update_convertible_bond_daily_data()  # 可转债日行情

        # # 期货日行情--- 使用tushare的日线 wind的没有权限
        print('update_future_daily_data')
        # tushare_crawler.update_future_daily_data() # 期货日行情,单次2000个，可能少数据；
        # # 期权日行情--- 使用tushare的日线 wind的没有权限
        print('update_stock_option_daily_data')
        # tushare_crawler.update_stock_option_daily_data()  # 期权日行情

    # with asd.WindData() as wind_data: #### 这个数据没有，可能需要其他的来解决了
        # wind_data.update_stock_daily_data() # 股票日行情 done
        # wind_data.update_stock_adj_factor() # 复权因子 done
        # wind_data.update_stock_units() # A股总股本、A股流通股本 done
        # wind_data.update_industry() # ['中信', '申万', '中证', 'Wind'] 行业表 ---》 目前只有wind有 ？？？？？
        # wind_data.update_pause_stock_info() # 股票停牌 done

        # wind_data.update_convertible_bond_daily_data() # 可转债日行情 ---》 分钟行情不在这里。done
        # wind_data.update_cb_convertible_price() # 可转债转股价 ？？？？？？
        # wind_data.update_future_daily_data() # 期货日行情
        # wind_data.update_fund_info() # 基金列表
        # wind_data.update_stock_option_daily_data() # 期权日行情

    # with asd.JQData() as jq_data:#### 需要花钱才行
        # jq_data.update_stock_morning_auction_data() # 【股票集合竞价数据】 属于付费模块，如果您有购买需求，请联系JQData管理员：
        # jq_data.update_stock_daily()# 股票日行情
        # jq_data.update_stock_minute()# 股票分钟行情
        # jq_data.update_future_daily()#期货日行情
        # jq_data.update_stock_option_daily()#期权日行情
        # jq_data.update_convertible_bond_list()#可转债信息

     # with asd.TDXData() as tdx_data:#### 通达信
        # tdx_data.update_stock_minute() #### 免费只能用 3个月左右的数据；，这里还依赖了JQ的集合竞价数据，做了一些调整；
        # tdx_data.update_convertible_bond_minute() # 可转债分钟行情

    # 计算指标相关
    # 标记是否 一字涨跌停，并写入【一字涨跌停】
    # asd.ConstLimitStockFactorCompositor().update() ###  20 min
    # 标识负净资产股票 并写入【负净资产股票】
    # asd.NegativeBookEquityListingCompositor().update() ### 删除然后重建
    # 指数更新器 ``./data/自编指数配置.xlsx`` ### 这里选了108个指标，一个指标4小时
    asd.IndexUpdater().update() ## 写入表 【自合成指数】
    #
    # asd.MarketSummaryCompositor().update() ### 要3天
    #
    # # model data
    # asd.model.SMBandHMLCompositor().update() # 2天
    # asd.model.UMDCompositor().update() # 2天
    #

if __name__ == '__main__':
    daily_routine(sys.argv[1])
