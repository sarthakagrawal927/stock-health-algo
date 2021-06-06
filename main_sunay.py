import all_imports as ai
import TechStrategies as TS

time_horizon_of_investment = int(input("Enter 1 for long term, 2 for medium term, 3 for short terms: "))

rsi_factor = 1


if(time_horizon_of_investment == 1):
    rsi_days_factor = 400

elif(time_horizon_of_investment == 2):
    rsi_days_factor = 100

elif(time_horizon_of_investment == 3):
    rsi_days_factor = 21

number_of_stocks_in_portfolio = int(input('Enter total number of stocks in portfolio: '))

weight_of_all_stock = 0
total_amount_invested = 0

for nosip in range(number_of_stocks_in_portfolio):

    stock = input('Enter name of stock: ').strip()
    stock = stock + '.NS'

    df = ai.get_data(stock)
    df.index.name = 'date'

    stock_qty = int(input('Script Quantity: '))
    print(stock, stock_qty)

    stock_live_price = ai.get_live_price(stock)
    volume_traded_till_now = (ai.get_quote_data(stock)['regularMarketVolume'])
    count = 0
    df = df[df.close > 0]
    df = df.reset_index()

    dates = df.loc[:, 'date']
    opening_prices = df.loc[:, 'open']
    high_daily = df.loc[:, 'high']
    low_daily = df.loc[:, 'low']
    closing_prices = df.loc[:, 'close']
    volume_daily = df.loc[:, 'volume']
    ticker = df.loc[:, 'ticker']


    opening_prices_array = ai.np.array([1])
    opening_prices_array = ai.np.append(opening_prices_array, opening_prices)
    opening_prices_array = ai.np.delete(opening_prices_array, 0)

    high_daily_array = ai.np.array([1])
    high_daily_array = ai.np.append(high_daily_array, high_daily)
    high_daily_array = ai.np.delete(high_daily_array, 0)

    low_daily_array = ai.np.array([1])
    low_daily_array = ai.np.append(low_daily_array, low_daily)
    low_daily_array = ai.np.delete(low_daily_array, 0)

    volume_daily_array = ai.np.array([1])
    volume_daily_array = ai.np.append(volume_daily_array, volume_daily)
    volume_daily_array = ai.np.delete(volume_daily_array, 0)
    current_datetime = ai.datetime.now()
    mins_at_915 = (9 * 60) + 15
    mins_at_now = (current_datetime.hour * 60) + current_datetime.minute
    if (mins_at_now > 930):
        difference = 930 - mins_at_915
    else:
        difference = mins_at_now - mins_at_915

    rationalized_volume = (volume_traded_till_now / difference) * 375

    closing_prices_array= ai.np.array([1])
    closing_prices_array = ai.np.append(closing_prices_array, closing_prices)
    closing_prices_array = ai.np.delete(closing_prices_array, 0)
    if (closing_prices_array[-1] != stock_live_price):
        closing_prices_array = ai.np.append(closing_prices_array, stock_live_price)
        volume_daily_array = ai.np.append(volume_daily_array, (round((rationalized_volume), 2)))
    else:
        pass

    invested_value = stock_qty*closing_prices_array[-1]


    rsi_health = (rsi_factor*(TS.RSI_RATIONALIZED(rsi_days_factor, closing_prices_array)))
    health_of_stock = rsi_health
    health_of_stock = round(health_of_stock, 2)


    weight_of_all_stock = weight_of_all_stock + health_of_stock*invested_value
    total_amount_invested = total_amount_invested + invested_value


portfolio_health = round((weight_of_all_stock/total_amount_invested), 2)
print('Your portfolio health is: ' + str(portfolio_health) + '%')
