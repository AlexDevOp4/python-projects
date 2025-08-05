def fahrenheit(celsius):
    f = (celsius * 1.8) + 32
    return f"{round(f)}℉"


def celsius(f):
    c = (f - 32) * 5 / 9
    return f"{round(c, 2)}℃"


print(fahrenheit(37.78))
