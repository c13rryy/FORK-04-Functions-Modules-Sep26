""" Модуль для работы со списком клиентов СТО"""

def show_all(clients):
    """Выводит всех клиентов в удобном формате."""

    for el in clients:
        print(el)


def filter_by_brand(clients, brand):
    """Возвращает список клиентов указанной марки автомобиля."""

    result = filter(lambda x: x[2] == brand, clients)
    print(list(result))
    return list(result)


def add_service_cost(clients, index, amount):
    """Добавляет сумму к стоимости обслуживания клиента по номеру в списке."""

    if not isinstance(amount, (int, float)): return

    client = clients[index]
    client[4] += amount
    print(clients)



# Сделал декоратор для подсчета сколько раз мы удаляли
# Но нужно сделать что то подобное для main
def logger(fn):
    del_count = 0
    def wrapper(lst, idx):
        fn(lst, idx)
        nonlocal del_count
        del_count += 1
        print(del_count)
    return wrapper

@logger
def delete_by_index(clients, index):
    """Удаляет клиента по номеру в списке."""

    if not isinstance(index, int): return

    del clients[index]
    print(clients)


def get_most_expensive(clients):
    """Возвращает клиента с максимальной стоимостью обслуживания."""

    max_amount = max(clients, key=lambda value: value[4])[4]
    return [el for el in clients if el[4] == max_amount]


def delete_older_than(clients, years):
    """Удаляет всех клиентов, чьи машины старше указанного количества лет."""

    current_year = 2026
    lst = [client for client in clients if current_year - client[3] > years]

    for el in lst:
        clients.remove(el)


def group_by_brand(clients):
    """Группирует клиентов по марке с использованием itertools.groupby."""
    pass

