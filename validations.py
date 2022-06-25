def is_float(value):
    try:
        float(value)

    except ValueError:
        return False

    return True


def valid_day(day):
    try:
        time.strptime(day, "%d/%m")

    except ValueError:
        return False

    return True


def valid_average(value):
    try:
        value = int(value)

        if value <= 0:
            return False

    except ValueError:
        return False

    return True


def digit_in_range(value, range_size):
    try:
        value = int(value)

        valid_range = range(0, range_size)

        if value not in valid_range:
            return False

    except ValueError:
        return False

    return True


def input_valid_price():
    try:
        day, price = input().split()

        formatted_day = valid_day(day)

        price_float = is_float(price)

        if not formatted_day or not price_float:
            day = None
            price = None

    except:
        return None, None

    return day, price


def input_valid_average(type_avrage):
    if type_avrage == 'short':
        print_short_average()
    else:
        print_long_average()

    try:
        avrage = int(input())

        if not valid_average(avrage):
            return None, None
    except:
        return None, None

    return avrage
