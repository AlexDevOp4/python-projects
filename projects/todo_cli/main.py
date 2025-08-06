import json


# def add_task(task, status):
#     data = {'task'}

#     json_str = json.dumps(data, indent=4)
#     with open("requirements.txt", "w") as f:
#         f.write(json_str)

with open("requirements.json") as f:
    data = json.load(f)
print(len(data))
