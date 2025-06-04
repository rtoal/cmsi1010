import locale
locale.setlocale(locale.LC_ALL, 'ru_RU')

def investment_value(start, interest_rate, years, tax_rate, deposit):
    balance = start
    for _ in range(1, years + 1):
        interest_earned = balance * interest_rate
        taxes = interest_earned * tax_rate
        balance += (interest_earned - taxes + deposit)
    return balance


def years_to_reach_goal(start, interest_rate, tax_rate, deposit, goal):
    years = 0
    balance = start
    while balance < goal:
        interest_earned = balance * interest_rate
        taxes = interest_earned * tax_rate
        balance += (interest_earned - taxes + deposit)
        years += 1
    return years

funds = investment_value(start=10000,
                       tax_rate=0.13,
                       years=25,
                       interest_rate=0.07,
                       deposit=500)

print(locale.currency(funds, grouping=True))

print(years_to_reach_goal(start=10000,
                          tax_rate=0.25,
                          interest_rate=0.13,
                          deposit=1000,
                          goal=1000000))
