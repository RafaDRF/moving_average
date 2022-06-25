from prints import *


def test_print_out():
    day = ['29/05', '28/05', '27/05', '26/05']

    price = [5.4, 8, 7, 6]

    av_short = [None, 7.000, 7.155, 6.506]

    av_long = [None, None, 7.004, 6.507]

    trend = [None, '  Alta  ', '  Baixa  ', 'Constante']

    results(day, price, av_short, av_long, trend)
