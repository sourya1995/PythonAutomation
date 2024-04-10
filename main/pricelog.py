import delorean
from decimal import Decimal
import parse

class PriceLog(object):
    def __init__(self, timestamp, product_id, price):
        self.timestamp = timestamp
        self.product_id = product_id
        self.price = price
    def __repr__(self):
        return '<PriceLog({}, {}, {})>'.format(self.timestamp, self.product_id, self.price) #like toString in Java
    
    @classmethod
    def parse(cls, text_log):

        def price(string):
            return Decimal(string)
        def isodate(string):
            return delorean.parse(string)
        FORMAT = ('[{timestamp:isodate}] - SALE - PRODUCT: {product:d}- ''PRICE: ${price:price}')
        formats = { 'price': price, 'isodate': isodate}
        result = parse.parse(FORMAT, text_log, formats=formats)
        return cls(timestamp=result['timestamp'], product_id=result['product'], price=result['price'])