user_time = int(input("Введите время в секундах"))
seconds = user_time % (24 * 3600)
hours = user_time // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
print(hours, minutes, seconds, sep=':')