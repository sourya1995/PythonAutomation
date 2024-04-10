import delorean
from decimal import Decimal

class PriceLog(object):
    def __init__(self, timestamp, product_id, price):
        self.timestamp = timestamp
        self.product_id = product_id
        self.price = price
    def __repr__(self):
        return '<PriceLog({}, {}, {})>'.format(self.timestamp, self.product_id, self.price) #like toString in Java
    
    @classmethod
    def parse(cls, text_log):
        divide_it = text_log.split(' - ')
        tmp_string, _, product_string, price_string = divide_it
        timestamp = delorean.parse(tmp_string.strip('[]'))
        product_id = int(product_string.split(':')[-1])
        price = Decimal(price_string.split('$')[-1])
        return cls(timestamp=timestamp, product_id=product_id, price=price)