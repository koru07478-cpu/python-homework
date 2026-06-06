#Программа для учёта расходов в базе данных shelve

import shelve


try:
    db = shelve.open('expenses')

    if "key" not in db:
        db["key"] = 0

    print(f"Текущие расходы: {db['key']} руб.")

    while True:
        try:
            user_input = input("Введите потраченную сумму в рублях: ")
            summa = int(user_input)
            db["key"] = db["key"] + summa
            print(f"Текущие расходы: {db['key']} руб.")

        except ValueError:
            print("Вы ввели неправильное значение")

except KeyboardInterrupt:
    #Ctrl+C или кнопка Stop. Но Ctrl+C - это копировать тут)
    pass

finally:
    db.close()
