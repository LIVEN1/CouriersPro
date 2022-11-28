from CouriersPro.Company.Company import Company
from CouriersPro.Courier.Courier import Courier

company = Company

def is_number(array):
    if len(array) > 1:
        first_value = array[0]
        second_value = array[1]
        if first_value.isdigit() & second_value.isdigit():
            return True
        else:
            return False
    else:
        value = array[0]
        if value.isdigit():
            return True
        else:
            return False


class CourierManager(Courier):
    @staticmethod
    def add_courier():
        print("Введите координаты начала через пробел(x y).")
        coordinates = input()
        coordinates_array = coordinates.split()
        x_coord = coordinates_array[0]
        y_coord = coordinates_array[1]
        if (is_number(coordinates_array)):
            print("Введите вместимость рюкзака")
            weight = input()
            if is_number(weight):
                courier = Courier(1, x_coord, y_coord, weight)
                company.add_courier(company, courier)
        else:
            print("Введены неправильные данные")
            return

    @staticmethod
    def destroy_courier():
        print("Введите айди нужного курьера")
        print(company.get_couriers_count(company))
        user_input = input()
        if (is_number(user_input)):
            company.try_to_destroy_courier(company, user_input)
        else:
            print("Введен неправильный формат id")
            return