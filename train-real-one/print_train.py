filepath = r"M:\python-newbie\train-real-one\trains.txt"
trains_list = []
train_dict = {}

with open(filepath, "r") as file:
    content = file.read()
    trains = content.split("\n")
    for attr in trains:
        trains_list.append(attr.split("_"))

for train in trains_list:
    train_dict[train[0]] = train[1:]

for train in train_dict:
    temp = train_dict[train]
    train_dict[train] = {
        "name": temp[0],
        "source": temp[1],
        "destination": temp[2]
    }

for train in train_dict:
    print(f"{train}: {train_dict[train]}")