daily_run = int(input("Введите начальное количество километров, пробегаемых спортсменом"))
purpose_run = int(input("Введите целевое количество километров"))
number_of_days = 1
while daily_run < purpose_run:
    daily_run *= 1.1
    number_of_days += 1
print(f"Спортсмен добьётся результата через {number_of_days} дней ")