from validations import *


### ------------------------- MENUS ------------------------ ###

def price_menu(value, first):
    if int(value) == 0:
        return None, None

    if int(value) == 1:
        if first:
            print_price_message()

        item_day, item_price = input_valid_price()
        return item_day, item_price

    elif int(value) == 2:
        ##id = price_remove_item()
        # id = 0
        # print_price_items()
        return id, None
    else:
        return None, None


def average_menu(value):
    if int(value) == 1:
        short_average = input_valid_avrage('short')
        return short_average, None

    elif int(value) == 2:
        long_average = input_valid_avrage('long')
        return None, long_average

    else:
        return None, None


price_day = []
price_value = []

short_average_day = None
short_average_calculated = []

long_average_day = None
long_average_calculated = []

trend_calculated = []

while True:
    start_option = wait_valid_option('start')

    if int(start_option) == 1:
        price_option = wait_valid_option('price')

        first = True
        while True:
            item_day, item_price = price_menu(price_option, first)

            if item_day == None or item_price == None:
                break

            price_day.append(item_day)
            price_value.append(item_price)

            first = False

        print_price_items(price_day, price_value)

    elif int(start_option) == 2:
        while True:
            average_option = wait_valid_option('average')
            short, long = average_menu(average_option)
            if short is not None:
                short_average_day = int(short)

            if long is not None:
                long_average = int(long)

            if short is None and long is None:
                break

    elif int(start_option) == 3:

        print("saida")

    else:
        break
