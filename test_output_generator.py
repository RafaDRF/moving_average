import output_generator


def test_avrage_in_period():

    price_value = [4.1293, 4.1097, 4.1095, 4.1104, 4.0954, 4.1071, 4.0556, 4.0841, 4.1293, 4.159]
    
    short_avrage_day = 3
    long_avrage_day = 5

    short = output_generator.average_in_period(price_value, short_avrage_day)

    print(short)

    long = output_generator.average_in_period(price_value, long_avrage_day)

    print(long)


def test_trend():
    
    d = [0.0, 0.0, 0.0, 1.0, 1.0, 1.0, -1.0, -1.0, None, None]
    print(d)
    print(output_generator.trend(d))


def test_get_diference_sign():

    mm3 = [4.116166666666667, 4.109866666666667, 4.105099999999999, 4.104299999999999, 4.086033333333334, 4.0822666666666665, 4.089666666666667, 4.124133333333333, None, None]
    mm5 = [4.11086, 4.10642, 4.0956, 4.09052, 4.0943000000000005, 4.10702, None, None, None, None]

    print(mm3)
    print(mm5)
 
    print(output_generator.get_difference_sign(mm3, mm5))


def test_moving_average():
    price = [1, 2, 3, 2, 1, 1, 2, 3]
    price = price[::-1]
    print(output_generator.moving_average(price, 3))

    short = output_generator.average_in_period(price, 3)
    long = output_generator.average_in_period(price, 5)

    print(short)
    print(long)

    d = output_generator.get_difference_sign(short, long)
    print(d)

    print(output_generator.trend(d))


if __name__ == "__main__":
    test_moving_average()


