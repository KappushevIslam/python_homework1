revenue = int(input("Введите выручку компании"))
costs = int(input("Введите издержки компании"))
if revenue > costs:
    employees = int(input("Введите количество сотрудников в компании"))
    print("Сумма вашей выручки - ", revenue - costs)
    print("Коэффицент рентабельности вашей компании - ", revenue / costs)
    print("Прибыль компании на одного сотрудника - ", (revenue - costs) // employees)
if revenue < costs:
    print("Сумма вашего убытка - ", costs - revenue)
if revenue == costs:
    print("У вас нет ни выручки, ни убытка. Компания работает в ноль")