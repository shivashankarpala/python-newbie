import copy
import os

class TRAIN:
    train_dict = {}

    def __init__(self):
        pass        

    @staticmethod
    def update_train_dictionary(filepath = os.path.join(os.getcwd(), r"train-real-one\trains.txt")):
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
        TRAIN.train_dict = copy.deepcopy(train_dict)

    @staticmethod
    def print_train_info(train_number = ""):
        if train_number == "":
            for train_number, info in TRAIN.train_dict.items():
                print(f"{train_number}")
                print(f"\tName: {info['name']}")
                print(f"\tSource: {info['source']}")
                print(f"\tDestination: {info['destination']}")
                print()
        else:
            info = TRAIN.search_train(train_number)
            if info is None:
                print(f"-- Train {train_number} not found")
            else:
                print(f"{train_number}")
                print(f"\tName: {info['name']}")
                print(f"\tSource: {info['source']}")
                print(f"\tDestination: {info['destination']}")
            print()

    @staticmethod
    def search_train(train_number):
        return TRAIN.train_dict.get(train_number, None)
    
# DEBUGGING CALLS
def main():    
    T = TRAIN()

    T.update_train_dictionary()
    T.print_train_info()
    T.print_train_info("TR100")

if __name__ == "__main__":
    main()
