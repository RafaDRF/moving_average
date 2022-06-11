
from os import remove


class Rawdata():
    def __init__(self):
        self.price = Price()
        self.short_avrage = Moving_avrage()
        self.long_avrage = Moving_avrage()
        self.trend = []
    
    ''' 
    def add_price(self, price):
        self.price.append(price)

    def remove_price(self, day):
        i = self.day.index(day)
        del self.price[i]
        del self.day[i]
    '''

    def set_avrages_days(self, short, long):
        if short > long:
            tmp = short
            short = long
            long = tmp
        self.short_avrage.set_day(short)
        self.longt_avrage.set_day(long)

    def calculate_all_avrage(self):
        self.short_avrage.calculate(self.price)
        self.long_avrage.calculate(self.price)
    
    def calculate_trend(self):
        ## se o sinal da diferenca entre o valor da media curte e a media londa eh o mesmo
        ## temos uma tendencia constante
        ## caso contrario temos uma tendencia de alta ou baixa
        pass

class Price():
    def __init__(self):
        self.day = []
        self.value = []
    
    def add(self, day, value):
        pass
    
    def remove():
        pass
class Moving_avrage():
    def __init__(self):
        self.day = 0
        self.value = []

    def set_day(self, day):
        self.day = day
    
    def get_value(self):
        return self.value

    def calculate(self, price):
        ## dias maiores que valores
        if self.day <= 0 or len(self.day) > len(price):
            return None

        total = 0

        for i in range(self.day):
            total += price[i]

        self.value = total/self.day
  
'''
def media_movel_simples(valor, dias):
    dias = int(dias)
    
    if dias <= 0:
        return None
    
    total = 0

    for i in range(dias):
        total += valor[i]

    media = total/dias

    return media
'''