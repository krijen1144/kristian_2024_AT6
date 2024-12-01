class UserInputValidator:
    def __init__(self):
        pass

def validate_positive_integers(self, input_list):
    valid_int = []
    for item in input_list:
        if item.isdigit() and int(item)>0:
            valid_int.append(int(item))
    return valid_int

def display(self):
    print("Validation Complete")
