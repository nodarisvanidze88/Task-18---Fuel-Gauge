print("Use only division")

while True:
    user = input("Fraction: ").strip()
    try:
        res = eval(user) * 100
        if res <= 1:
            print("E")
            break
        elif res >= 99:
            print("F")
            break
        else:
            print(f"{round(res)}%")
            break
    except:
        pass
