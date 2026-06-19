import datetime


def get_age(date_of_birth: datetime.datetime, now: datetime.datetime) -> int:
    """Возвращает возраст на основе даты рождения и текущего времени."""
    age = now.year - date_of_birth.year
    if (now.month, now.day) < (date_of_birth.month, date_of_birth.day):
        age -= 1
    return age


def print_current_date() -> None:
    # 1
    """Выводит день недели и текущую дату."""
    now = datetime.datetime.now().date()
    weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    print(weekdays[now.weekday()], now)


def calculate_user_age_and_time_of_the_next_bd() -> None:
    # 2
    """Принимает в качестве ввода день рождения и выводит возраст
    пользователя и количество дней, часов, минут и секунд до следующего дня рождения."""
    while True:
        date_bd = input(f"\nВведите дату своего рождения в формате ДД.ММ.ГГГГ: ")
        try:
            date_of_birth = datetime.datetime.strptime(date_bd, "%d.%m.%Y")
            break
        except ValueError:
            print("Неверный формат даты! Попробуйте еще раз.")

    now = datetime.datetime.now()

    age = get_age(date_of_birth, now)

    next_birthday = date_of_birth.replace(year=now.year)
    if next_birthday < now:
        next_birthday = next_birthday.replace(year=now.year + 1)

    delta = next_birthday - now

    days = delta.days
    hours = delta.seconds // 3600
    minutes = (delta.seconds // 60) % 60
    seconds = delta.seconds % 60

    print(f"\nВаш возраст: {age} лет.")
    print(f"До следующего дня рождения осталось {days} дн. {hours} ч. {minutes} мин. {seconds} сек.")


def calculate_double_day() -> None:
    # 3
    """Принимает в качестве ввода два дня рождения и выводит двойной день именинников."""
    while True:
        input(f"\nПосчитаем двойной день? (тык Enter, если да)")
        date_bd1 = input("Введите дату рождения первого человека в формате ДД.ММ.ГГГГ: ")
        date_bd2 = input("Введите дату рождения второго человека в формате ДД.ММ.ГГГГ: ")
        try:
            date_of_birth1 = datetime.datetime.strptime(date_bd1, "%d.%m.%Y")
            date_of_birth2 = datetime.datetime.strptime(date_bd2, "%d.%m.%Y")
            break
        except ValueError:
            print("Неверный формат даты! Попробуйте еще раз.")

    if date_of_birth1 == date_of_birth2:
        print("\nЛюди родились в один день, двойной день невозможен!")
    else:
        if date_of_birth1 < date_of_birth2:
            older = date_of_birth1
            younger = date_of_birth2
        else:
            older = date_of_birth2
            younger = date_of_birth1

        age_difference = younger - older
        double_day = younger + age_difference

        print(f"\nДвойной день: {double_day.strftime('%d.%m.%Y')}")


if __name__ == "__main__":
    print_current_date()
    calculate_user_age_and_time_of_the_next_bd()
    calculate_double_day()
