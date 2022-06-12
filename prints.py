def print_start_menu():
    menu_range = 4
    menu_message = """
        Bem vindo(a)!
        Escolha uma acao:

        [1] Cadastrar nova serie
        [2] Gerenciar Medias Moveis
        [3] Gerar Saida

        [0] Sair do Programa
        """
    print(menu_message)
    return menu_range


def print_price_menu():
    menu_range = 4
    menu_message = """
        [1] Adicionar itens
        [2] Remover item 
        [3] Ler Arquivo

        [0] Voltar para Menu 
    """
    print(menu_message)
    return menu_range


def print_average_menu():
    menu_range = 3
    menu_message = """
        Escolha uma media para detetminar:

        [1] Media Movel Curta
        [2] Media Movel Longa

        [0] Voltar para Menu
    """
    print(menu_message)
    return menu_range


def print_price_items(days, prices):

    current_price_head = """
        Valores atuais da serie:
        Dia    -    Preco"""

    print(current_price_head)

    for i, day in enumerate(days):
        if day is not None and prices[i] is not None:
            current_price_item = f"\t{day}  -    {prices[i]}"
            print(current_price_item)


def print_price_message():
    message = "Digite o dia e o preco saparados por espaco"
    exemple = """
    Exemplo:
    15/05 4.67
    """
    print(message)
    print(exemple)


def print_short_average():
    short_average = "Digite o valor da Media Movel Curta: "
    print(short_average)


def print_long_average():
    long_average = "Digite o valor da Media Movel Longa: "
    print(long_average)


def print_results(day, price, short, long, trend):

    empty_average = ' -/- '
    empty_trend = '   -/-   '
    line = '---------------------------------------------'

    print(line)

    print(' Dia  - Preco - Curta - Longa    - Tendencia')

    print(line)

    for i, _ in enumerate(day):
        if short[i] is None:
            short[i] = empty_average
        else:
            short[i] = '%.3f' % short[i]
        if long[i] is None:
            long[i] = empty_average
        else:
            long[i] = '%.3f' % long[i]

        if trend[i] is None:
            trend[i] = empty_trend

        print(f'{day[i]} - {price[i]:.3f} -  {short[i]} - {long[i]}   - {trend[i]}')
