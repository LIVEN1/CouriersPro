class InputManager:
    @staticmethod
    def get_input():
        input_value = input()
        return input_value

    @staticmethod
    def is_number(array):

        values = array.split(" ")

        if len(values) == 0:
            print("Ошибка")
            return

        if len(values) > 1:
            first_value = values[0]
            second_value = values[1]
            if first_value.isdigit() & second_value.isdigit():
                return True
            else:
                print("Ошибка")
                return False
        else:
            value = values[0]
            if value.isdigit():
                return True
            else:
                print("Ошибка")
                return False

    @staticmethod
    def check_length_array(value, length):
        array = value.split(" ")
        if len(array) != length:
            print("Ошибка")
            return False
        return True


