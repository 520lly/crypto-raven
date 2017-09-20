from ._kkex import KKEX
from ._bittrex import Bittrex
from ._bitfinex import Bitfinex
from ._binance import Binance

import logging
import config

def create_markets(exchangeNames):
    markets = {}
    for name in exchangeNames:
        if (name == 'KKEX_BCH_BTC'):
            xchg = KKEX('BCCBTC')
        elif (name == 'KKEX_ETH_BTC'):
            xchg = KKEX('ETHBTC')
        elif (name == 'Bitfinex_BCH_BTC'):
            xchg = Bitfinex('bchbtc')
        elif (name == 'Bittrex_BCH_BTC'):
            xchg = Bittrex('BTC-BCC')
        elif (name == 'Binance_ETH_BTC'):
            xchg = Binance('ETHBTC')
        elif (name == 'Binance_BNB_BTC'):
            xchg = Binance('BNBBTC')
        elif (name == 'Binance_BNB_ETH'):
            xchg = Binance('BNBETH')
        elif (name == 'Binance_MCO_BTC'):
            xchg = Binance('MCOBTC')
        elif (name == 'Binance_MCO_ETH'):
            xchg = Binance('MCOETH')
        elif (name == 'Binance_QTUM_BTC'):
            xchg = Binance('QTUMBTC')
        elif (name == 'Binance_QTUM_ETH'):
            xchg = Binance('QTUMETH')
        elif (name == 'Binance_WTC_BTC'):
            xchg = Binance('WTCBTC')
        elif (name == 'Binance_WTC_ETH'):
            xchg = Binance('WTCETH')

        else:
            logging.warn('Exchange ' + name + ' not supported!')
            assert(False)
        
        xchg.name = name

        logging.info('%s market initialized' % (xchg.name))
        
        ticker = xchg.get_ticker()

        markets[name]= xchg
    return markets