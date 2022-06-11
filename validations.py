import time
from prints import *

def is_float(value):
    try:
        value = float(value)       

    except ValueError:
        return False
  
    return True

def valid_day(day):
    try:
        time.strptime(day, "%d/%m")
    
    except ValueError:
        return False
    
    return True

def valid_avrage(value):
    try:
        value = int(value)

        if value <= 0:
            return False
    except:
        return False
    
    return True

def digit_in_range(value,range_size):
    try:
        value = int(value)
        
        valid_range = range(0, range_size)

        if value not in valid_range:
            return False         

    except ValueError:
         return False
  
    return True

def wait_valid_option(menu_to_print):
    while True:
        if menu_to_print == 'start':
            valid_range = print_start_menu()
        
        elif menu_to_print == 'price':
            valid_range = print_price_menu()

        elif menu_to_print == 'avrage':
            valid_range = print_avrage_menu()

        option = input() 
        
        if digit_in_range(option, valid_range):
            break
    
    return option

def input_valid_price():
    
    try:
        day, price = input().split()
    
        formatted_day = valid_day(day)

        price_float = is_float(price)

        if not formatted_day or  not price_float:
            day = None
            price = None
    
    except:
        return None, None

    return day, price

def input_valid_avrage(type_avrage):
    if type_avrage == 'short':
        print_short_avrage()
    else:
        print_long_avrage()

    try:
        avrage = int(input())
        
        if not valid_avrage(avrage):
            return None, None
    except:
        return None, None

    return avrage

