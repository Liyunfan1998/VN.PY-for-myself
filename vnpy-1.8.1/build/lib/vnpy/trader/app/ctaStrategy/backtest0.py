# encoding: UTF-8
# from __future__ import division

from vnpy.trader.vtConstant import *
from vnpy.trader.app.ctaStrategy.ctaBacktesting import BacktestingEngine, MINUTE_DB_NAME, TICK_DB_NAME #ctaBase.py

print TICK_DB_NAME
from vnpy.trader.app.ctaStrategy.ctaTemplate import *

# if __name__ == '__main__':
# from vnpy.trader.app.ctaStrategy.strategy.TickOneStrategy import *
from vnpy.trader.app.ctaStrategy.strategy.BitcoinZhou import *

# 创建回测引擎
engine = BacktestingEngine()

# 设置引擎的回测模式为K线
engine.setBacktestingMode(engine.TICK_MODE)

# 设置回测用的数据起始日期
engine.setStartDate('20180101')
engine.setEndDate('20180106')

# 设置产品相关参数
engine.setCapital(100000)
engine.setSize(10)
engine.setSlippage(1)  # 股指1跳
engine.setRate(3 / 10000)  # 万0.3
engine.setPriceTick(1)  # 股指最小价格变动

# 设置使用的历史数据库
engine.setDatabase(TICK_DB_NAME, 'bitcoin')
# 在引擎中创建策略对象
d = {}
# engine.initStrategy(TickOneStrategy)
engine.initStrategy(BitCoinStrategy)

# 开始跑回测
engine.runBacktesting()

# 显示回测结果
engine.showBacktestingResult()