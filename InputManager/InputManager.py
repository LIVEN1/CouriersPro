class InputManager:
    @staticmethod
    def get_input():
        input_value = input()
        return input_value

    @staticmethod
    def is_number(array):
        if len(array) == 0:
            print("Error")
            return


        if len(array) > 1:
            first_value = array[0]
            second_value = array[1]
            if first_value.isdigit() & second_value.isdigit():
                return True
            else:
                print("Error")
                return False
        else:
            value = array[0]
            if value.isdigit():
                return True
            else:
                print("Error")
                return False