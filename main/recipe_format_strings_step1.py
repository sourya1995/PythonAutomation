data = [
    (1000, 10),
    (2000, 17),
    (2500, 170),
    (2500, -170),
]

print('REVENUE | PROFIT | PERCENT')
TEMPLATE = '{revenue:>7,} | {profit:>+6} | {percent:>7.2%}'

for revenue, profit in data:
    row = TEMPLATE.format(revenue=revenue, profit=profit, percent = profit/revenue)
    print(row)