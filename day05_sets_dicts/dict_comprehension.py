math_dict = {"A": 1, "B": 2, "C": 3, "D": 4}

for keys, values in math_dict.items():
    math_dict[keys] = values * 2


animal_speeds = {
    "cheetah": 120,
    "turtle": 1,
    "horse": 88,
    "rabbit": 40,
    "sloth": 0.3,
    "kangaroo": 71,
}


under_fifty = {key: value for key, value in animal_speeds.items() if value < 50}
print(under_fifty)
