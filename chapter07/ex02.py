def eval_loop():
    while True:
        a = input("Введите выражение: ")
        if a == "готово":
            break
        x = eval(a)
        print(x)

eval_loop()
