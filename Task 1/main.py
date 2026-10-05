import garage_utils as gu

clients = [
    [1, "Иван Петров", "Toyota", 2015, 250],
    [2, "Анна Смирнова", "BMW", 2018, 480],
    [3, "Сергей Ковалев", "Audi", 2012, 390],
    [4, "Мария Иванова", "Volkswagen", 2010, 210],
    [5, "Дмитрий Орлов", "Mercedes", 2019, 520],
    [6, "Ольга Сидорова", "Toyota", 2016, 300],
    [7, "Алексей Жуков", "Ford", 2013, 180],
    [8, "Елена Кравцова", "Kia", 2020, 260],
    [9, "Павел Лебедев", "Hyundai", 2017, 240],
    [10, "Ирина Фролова", "BMW", 2014, 450],
    [11, "Николай Громов", "Renault", 2011, 170],
    [12, "Татьяна Белова", "Audi", 2019, 510]
]

# def logger(fn):
#     del_count = 0
#     def wrapper(lst, idx):
#         fn(lst, idx)
#         nonlocal del_count
#         del_count += 1
#         print(del_count)
#     return wrapper


def show_menu():
    print("""
1 — вывести всех клиентов
2 — вывести клиентов заданной марки
3 — изменить сумму обслуживания
4 — удалить клиента
5 — найти самую дорогую машину
6 — удалить машины старше n лет
7 — сгруппировать клиентов по марке
0 — выход
""")
    
    
def main():
    # Ваш код здесь
    while True:
        show_menu()
        choice = input("Выберите нужный пункт ")
        if choice not in "12345670":
               return

        choice = int(choice)

        match choice:
            case 1:
                gu.show_all(clients)
            case 2:
                car_brand = input("Введите марку авто ")
                gu.filter_by_brand(clients, car_brand)
            case 3:
                car_idx = int(input("Введите индекс авто "))
                car_amount = float(input("Введите на сколько увеличиваем обслуживание "))
                gu.add_service_cost(clients, car_idx, car_amount)
            case 4:
                car_idx = int(input("Введите индекс авто "))
                gu.delete_by_index(clients, car_idx)
            case 5:
                gu.get_most_expensive(clients)
            case 6:
                car_year = int(input("Введите возраст авто "))
                gu.delete_older_than(clients, car_year)
            case _:
              return


if __name__ == "__main__":
    main()