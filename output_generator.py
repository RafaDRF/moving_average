from numpy import sign

def get_diference_sign(short, long):
    diference = []
    
    for i in range(0,len(long)):
        if short[i] == None or long[i] == None:
            diference.append(None)
            continue
        
        item_diference =  short[i] - long[i]
        diference_sign = sign(item_diference)
        diference.append(diference_sign)
    
    return diference

def trend(diference):
    trend_list = []
    
    for i in range(1,len(diference)):
        
        if diference[i] == None or diference[i-1] == None:
            trend_list.append(None)
            continue

        last_sign = sign(diference[i])
        actual_sign = sign(diference[i-1])

        same_sign = last_sign == actual_sign

        if same_sign:
            trend_list.append('Constante')
        else:
            if last_sign < actual_sign:
                trend_list.append('Alta')
            else:
                trend_list.append('Queda')

    return trend_list


def moving_avrage(price, day):
   
    if day <= 0 or day > len(price):
        return None

    total = 0

    for i in range(0,day):
        total += price[i]
    
    value = total/day
    
    return value

def avrage_in_period(price_value, avrage_day):
    avrage_calculated = []
    for i in range(len(price_value)):
        avrage_item = moving_avrage(price_value[i:], avrage_day)
        avrage_calculated.append(avrage_item)
    
    return avrage_calculated

def make_same_size(long_list, short_list):
    size_short = len(short_list)
    size_long = len(long_list)

    spaces_to_fill = size_long - size_short

    for i in range(1, spaces_to_fill):
        short_list.insert(0, None)

    return short_list





