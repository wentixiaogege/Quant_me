import sys

import AShareData as asd


def daily_routine(config_loc: str):
    asd.set_global_config(config_loc)

    with asd.TushareData() as tushare_crawler:
        # tushare_crawler.update_base_info()
        # tushare_crawler.get_shibor()
        #
        # tushare_crawler.get_ipo_info()
        # tushare_crawler.get_company_info()
        # tushare_crawler.update_hs_holding()
        # tushare_crawler.get_hs_constitute()
        #
        # tushare_crawler.update_stock_names()
        # tushare_crawler.update_dividend()

        # tushare_crawler.update_index_daily() #指数日行情
        # tushare_crawler.update_stock_list_date()
        # tushare_crawler.update_hq_daily()  # 股票日行情 + 复权因子 + 流通股本--- 使用tushare的日线 wind的没有权限
        #
        # tushare_crawler.update_hk_stock_daily() # 港股日行情

        # tushare_crawler.update_fund_daily()
        # tushare_crawler.update_fund_dividend()
        tushare_crawler.update_financial_data()

        # tushare_crawler.update_pause_stock_info# 股票停牌--- 使用tushare的日线 wind的没有权限

    # with asd.WindData() as wind_data: #### 这个数据没有，可能需要其他的来解决了
        # wind_data.update_stock_daily_data() # 股票日行情
        # wind_data.update_stock_adj_factor() # 复权因子
        # wind_data.update_stock_units() # A股总股本、A股流通股本
        # wind_data.update_industry() # ['中信', '申万', '中证', 'Wind'] 行业表 ---》 目前只有wind有
        # wind_data.update_pause_stock_info() # 股票停牌

        # wind_data.update_convertible_bond_daily_data() # 可转债日行情 ---》 分钟行情不在这里。
        # wind_data.update_cb_convertible_price() # 可转债转股价
        # wind_data.update_future_daily_data() # 期货日行情
        # wind_data.update_fund_info() # 基金列表
        # wind_data.update_stock_option_daily_data() # 期权日行情

    # with asd.JQData() as jq_data:#### 需要花钱才行
    #     jq_data.update_stock_morning_auction_data() # 股票集合竞价数据
        ####
        # 股票日行情
        # 股票分钟行情
        # 期货日行情
        # 期权日行情
        # 可转债信息

    # with asd.TDXData() as tdx_data:
    #     # tdx_data.update_stock_minute() #### 应该是数据量太大了，注释了。看readme是说还没调试完。。
    #     tdx_data.update_convertible_bond_minute()

    # compute data
    # asd.ConstLimitStockFactorCompositor().update()
    # asd.NegativeBookEquityListingCompositor().update()
    # asd.IndexUpdater().update()
    asd.MarketSummaryCompositor().update()

    # model data
    asd.model.SMBandHMLCompositor().update()
    asd.model.UMDCompositor().update()


if __name__ == '__main__':
    daily_routine(sys.argv[1])
