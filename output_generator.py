from numpy import sign


def get_difference_sign(short, long):
    difference = []

    for i in range(0, len(long)):
        if short[i] is None or long[i] is None:
            difference.append(None)
            continue

        item_difference = short[i] - long[i]
        difference_sign = sign(item_difference)
        difference.append(difference_sign)

    return difference


def trend(difference):
    trend_list = []

    for i in range(1, len(difference)):

        if difference[i] is None or difference[i - 1] is None:
            trend_list.append(None)
            continue

        last_sign = sign(difference[i])
        actual_sign = sign(difference[i - 1])

        same_sign = last_sign == actual_sign

        if same_sign:
            trend_list.append('Constante')
        else:
            if last_sign < actual_sign:
                trend_list.append('Alta')
            else:
                trend_list.append('Queda')

    return trend_list


def moving_average(price, day):
    if day <= 0 or day > len(price):
        return None

    total = 0

    for i in range(0, day):
        total += price[i]

    value = total / day

    return value


def average_in_period(price_value, average_day):
    average_calculated = []
    for i in range(len(price_value)):
        average_item = moving_average(price_value[i:], average_day)
        average_calculated.append(average_item)

    return average_calculated


def make_same_size(long_list, short_list):
    size_short = len(short_list)
    size_long = len(long_list)

    spaces_to_fill = size_long - size_short

    for i in range(1, spaces_to_fill):
        short_list.insert(0, None)

    return short_list

