
n = int(input("Введите возраст"))
last_dig = n % 10 # остаток от деления
if 10 <n< 20:
    print("Мне", n, "лет")
elif 1 <last_dig<5:
    print("Мне", n, "года")