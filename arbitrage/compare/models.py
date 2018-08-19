from django.db import models

'''
think about
- what do you need for the functionality to be operational?
- what, and in which form, can you get from the available APIs?

'''

class Exchange(models.Model):
    name = models.CharField(max_length=100)
    transfer_fee = models.FloatField()
    buy_fee = models.FloatField()
    trade_fee = models.FloatField()

    def __str__(self):
        return self.name


class Asset(models.Model):
    name = models.CharField(max_length=200)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return self.symbol


class Market(models.Model):
    # a trade pair, e.g. BTC/ETH, is called a 'market'
    trade_pair = models.ManyToManyField(Asset)

    def __str__(self):
        return self.trade_pair


class Trade(models.Model):
    trade_pair = models.ForeignKey(Market, on_delete='CASCADE')
    exchange = models.ForeignKey(Exchange, on_delete='CASCADE')
    trade_id = models.IntegerField()
    timestamp = models.DateTimeField()
    price = models.FloatField()
    amount = models.FloatField()
    # 'choices' must be an iterable containing (actual value, human readable name) tuples.
    side = models.CharField(choices=(('sell', 'sell'), ('buy', 'buy')),
                            max_length=5)

    def __str__(self):
        sum_up = '{0}\t{1}\t{2}'.format(self.trade_pair,
                                        self.side,
                                        self.exchange)
        return sum_up
