import imports as ai


def EMA(ema, closing_prices_array):
    ema_array = ai.np.array([ai.np.average(closing_prices_array[0:ema])])
    for i in range(1, len(closing_prices_array) - ema + 1):
        ema_array = ai.np.append(ema_array, (2/(ema+1))*(closing_prices_array[ema+i-1]-ema_array[i-1]) + ema_array[i-1])
    return ema_array


def RSI(number_of_days, closing_prices_array):
    last_n_days_closing_array = closing_prices_array[(-1*number_of_days):]
    change_array = ai.np.array([0])
    for i in range(len(last_n_days_closing_array)-1):
        change_array = ai.np.append(change_array, (last_n_days_closing_array[i+1]-last_n_days_closing_array[i]))
    change_array = ai.np.delete(change_array, 0)
    gain_array = ai.np.array([0])
    loss_array = ai.np.array([0])
    for i in change_array:
        if(i>=0):
            gain_array = ai.np.append(gain_array, i)
        else:
            loss_array = ai.np.append(loss_array, i)
    gain_array = ai.np.delete(gain_array, 0)
    loss_array = ai.np.delete(loss_array, 0)
    avg_gain = EMA(len(gain_array), gain_array)
    avg_loss = (-1*EMA(len(loss_array), loss_array))
    X = float(100-(100/(1+(avg_gain/avg_loss))))
    return X

def RSI_RATIONALIZED(number_of_days, closing_prices_array):
    X= RSI(number_of_days, closing_prices_array)
    X = X-100
    if(X>=0):
        return X
    else:
        return (-1*X)


