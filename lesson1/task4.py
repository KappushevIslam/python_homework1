user_answer = int(input("Введите число"))
n = user_answer % 10
user_answer = user_answer // 10
while user_answer > 0:
    if user_answer % 10 > n:
        n = user_answer % 10
    user_answer = user_answer // 10
print(n)