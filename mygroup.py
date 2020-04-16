# массив данных
groupmates = [
    {
        'id' : "1",
        'firstname' : "Александр",
        'lastname' : "Мальцев",
        'subject' : ["ВМ", "Философия", "ИиКГ", "Физ-ра", "Физика", "ИЯ", "ТWП", "ВвП"],
        'score' : [5, 4, 5, 4, 5, 4, 5, 3]
    },
    {
        'id' : "2",
        'firstname' : "Анастасия",
        'lastname' : "Щербакова",
        'subject' : ["ВМ", "Философия", "ИиКГ", "Физ-ра", "Физика", "ИЯ", "ТWП", "ВвП"],
        'score' : [4, 5, 3, 4, 5, 5, 4, 5]
    },
    {
        'id' : "3",
        'firstname' : "Владлен",
        'lastname' : "Бурлака",
        'subject' : ["ВМ", "Философия", "ИиКГ", "Физ-ра", "Физика", "ИЯ", "ТWП", "ВвП"],
        'score' : [3, 4, 5, 3, 5, 5, 3, 5]
    },
    {
        'id' : "4",
        'firstname' : "Владимир",
        'lastname' : "Локатенко",
        'subject' : ["ВМ", "Философия", "ИиКГ", "Физ-ра", "Физика", "ИЯ", "ТWП", "ВвП"],
        'score' : [3, 4, 5, 4, 3, 5, 4, 4]
    },
    {
        'id' : "5",
        'firstname' : "Алексей",
        'lastname' : "Николаев",
        'subject' : ["ВМ", "Философия", "ИиКГ", "Физ-ра", "Физика", "ИЯ", "ТWП", "ВвП"],
        'score' : [5, 4, 5, 5, 4, 5, 5, 5]
    }
]

# ширина колонок
column0 = 5
column1 = 15
column2 = 15
column3 = 70
column4 = 50

# общий список сотрудников
def view_workers(workers): 
    print(u"id".ljust(column0), u"Имя".ljust(column1), u"Фамилия".ljust(column2), u"Предметы".ljust(column3), u"Оценки".ljust(column4))

    for worker in workers:
        print(worker["id"].ljust(column0), worker["firstname"].ljust(column1), worker["lastname"].ljust(column2), str(worker["subject"]).ljust(column3), str(worker["score"]).ljust(column4))

# сортировка по среднему значению
def average(value, workers):
    print(u"id".ljust(column0), u"Имя".ljust(column1), u"Фамилия".ljust(column2), u"Среднее значение".ljust(column4))
    for worker in workers:
        avr = sum(worker["score"]) / len(worker["score"])
        if value < avr:
            print(worker["id"].ljust(column0), worker["firstname"].ljust(column1), worker["lastname"].ljust(column2), avr)

# ввод
def checkinput():
    for i in range(10):
        value = input()
        if value.isdigit():
            return int(value)
        else:
            try:
                return float(value)
            except:
                print("Введено неверное значение, повторите ввод. Используйте целые (1, 2, 3, ...) или дробные (1.1, 2.2, 3.3, ...) числа.")
                if i == 4:
                    print("!Это уже 5-ая попытка!")
                if i == 9:
                    print("!Это уже 10-ая попытка и это конец! Начните снова!")
                    return exit(0)

print()
print("Список студентов с оценками за экзамены")

view_workers(groupmates)

print()
print("Вывод студентов со средним балом выше чем (от 1 до 5, включая дробные):")
input_value = checkinput()

print()
average(input_value, groupmates)