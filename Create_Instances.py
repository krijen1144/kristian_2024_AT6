from UserInputValidator import UserInputValidator

val1 = UserInputValidator()
val2 = UserInputValidator()

input_1 = ["12", "20", "testing", "98", "not_a_int"]
input_2 = [12, 20, "testing", 91, "not_a_int", 21, 23,45]

valid_num_1 = val1.validate_positive_integers(input_1)
valid_num_2 = val2.validate_positive_integers(input_2)

print("Valid numbers in list 1: ", valid_num_1)
print("Valid numbers in list 2: ", valid_num_2)