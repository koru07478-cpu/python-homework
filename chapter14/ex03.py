#Программа для учёта расходов в базе данных shelve

import shelve

def shelve_money(filename: str = 'expenses', key: str = 'total') -> None:
    db = None

    try:
        db = shelve.open(filename)
        if key not in db:
            db[key] = 0

        print(f"Текущие расходы: {db[key]} руб.")

        while True:
            try:
                user_input = input("Введите потраченную сумму в рублях: ")
                summa = int(user_input)
                db[key] = db[key] + summa
                print(f"Текущие расходы ({key}): {db[key]} руб.")

            except ValueError:
                print("Вы ввели неправильное значение")

    except KeyboardInterrupt:
        #Ctrl+C или кнопка Stop. Но Ctrl+C - это копировать тут)
        pass

    finally:
        if db is not None:
            db.close()


shelve_money(filename='money', key='products')
