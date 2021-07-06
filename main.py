from functions import compute

# taking input
# time_horizon_of_investment = int(input("Enter 1 for long term, 2 for medium term, 3 for short terms: "))
# number_of_stocks_in_portfolio = int(input('Enter total number of stocks in portfolio: '))

# stocks=[]
# stocks_qty=[]

# for i in range(number_of_stocks_in_portfolio):
#      stocks.append( input('Enter name of stock: ').strip())
#      stocks_qty.append(int(input('Script Quantity: ')))

def makeData(stock_data, timeframe = 1):
    stocks=[]
    stocks_qty=[]
    for item in stock_data:
        # print(item)
        stocks.append(item['id'])
        stocks_qty.append(int(item['quantity']))
    # print(stocks)
    return compute(stocks,stocks_qty,timeframe)

# stocks,stock_qty = makeData(data)
# portfolio_health, send_data  = compute(stocks, stocks_qty, time_horizon_of_investment )
# print(portfolio_health)
# print(send_data)

