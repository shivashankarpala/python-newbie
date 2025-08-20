import copy
import os

class TRAIN:
    train_dict = {}
    train_route_dict = {}
    train_coach_dict = {}

    def __init__(self):
        pass        

    @staticmethod
    def read_train_info(filepath = os.path.join(os.getcwd(), r"train-real-one\train_info.txt")):
        train_list = []
        train_dict = {}

        with open(filepath, "r") as file:
            content = file.read()
            trains = content.split("\n")
            for attr in trains:
                train_list.append(attr.split("_"))
            for train in train_list:
                train_dict[train[0]] = train[1:]
        TRAIN.train_dict = copy.deepcopy(train_dict)

    @staticmethod
    def refresh_train_dictionary():
        
        train_dict = copy.deepcopy(TRAIN.train_dict)
        TRAIN.refresh_train_route_dictionary()
        TRAIN.refresh_train_coach_dictionary()
        combined_dict = {}

        for train in train_dict:
            combined_dict[train] = {**TRAIN.train_route_dict[train], **TRAIN.train_coach_dict[train]}
            
        TRAIN.train_dict = copy.deepcopy(combined_dict)

    @staticmethod
    def refresh_train_route_dictionary():

        train_dict = copy.deepcopy(TRAIN.train_dict)
        train_route_dict = {}

        for train in train_dict:
            temp = train_dict[train]
            train_route_dict[train] = {
                "name": temp[0],
                "source": temp[1],
                "destination": temp[2]
            }
        TRAIN.train_route_dict = copy.deepcopy(train_route_dict)

    @staticmethod
    def refresh_train_coach_dictionary():
        
        train_dict = copy.deepcopy(TRAIN.train_dict)
        train_coach_dict = {}
        temp = {}

        for train in train_dict:
            train_coach_dict[train] = train_dict[train][3:]

        for train in train_coach_dict:
            train_coach_dict[train] = {
                "coaches": train_coach_dict[train][0],
                "coach-types": train_coach_dict[train][1:],
            }

        # This method will create a dictionary of dictionaries for train coaches
        for train, info in train_coach_dict.items():
            coach_type_list = info["coach-types"]
            coach_type_dict = {}
            for ct in coach_type_list:
                num, typ = ct.split('*', 1)
                coach_type_dict[typ] = int(num)
            temp[train] = coach_type_dict

            train_coach_dict[train]["coach-types"] = temp[train]
        TRAIN.train_coach_dict = copy.deepcopy(train_coach_dict)

    @staticmethod
    def print_train_info(train_number = ""):
        if train_number == "":
            for train_number, info in TRAIN.train_dict.items():
                print(f"{train_number}:")
                print(f"\tName: {info['name']}")
                print(f"\tSource: {info['source']}")
                print(f"\tDestination: {info['destination']}")
                print(f"\tCoaches: {info['coaches']}")
                print(f"\tCoach Types: ")
                for i in info['coach-types']:
                    print(f"\t\t{i}: {info['coach-types'][i]}")
                print()
        else:
            info = TRAIN.search_train(train_number)
            if info is None:
                print(f"-- Train {train_number} not found")
            else:
                print(f"{train_number}:")
                print(f"\tName: {info['name']}")
                print(f"\tSource: {info['source']}")
                print(f"\tDestination: {info['destination']}")
                print(f"\tCoaches: {info['coaches']}")
                print(f"\tCoach Types: ")
                for i in info['coach-types']:
                    print(f"\t\t{i}: {info['coach-types'][i]}")
            print()

    @staticmethod
    def search_train(train_number):
        return TRAIN.train_dict.get(train_number, None)
    
# DEBUGGING CALLS
def main():    
    T = TRAIN()

    T.read_train_info()

    T.refresh_train_dictionary()
    T.print_train_info('TR1001')

if __name__ == "__main__":
    main()
