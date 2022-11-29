from CouriersPro.Company.Manager.CompanyManager import CompanyManager
from CouriersPro.InputManager.InputManager import InputManager
from CouriersPro.Order.Order import Order

company = CompanyManager


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


class OrderManager(Order):
    @staticmethod
    def create_order():
        print("Введите координаты начала через пробел(x y).")
        coordinates = InputManager.get_input()
        coordinates_array = coordinates.split()
        x_coord = coordinates_array[0]
        y_coord = coordinates_array[1]
        if is_number(coordinates_array):
            print("Введите Вес Груза")
            weight = InputManager.get_input()
            if is_number(weight):
                id = company.get_orders_count(company) + 1
                order = Order(id, x_coord, y_coord, weight)
                company.add_order(company, order)

        else:
            print("Получены не числа")
            return

    @staticmethod
    def destroy_order():
        print("Введите айди нужного заказа")
        print(company.get_orders_count(company))
        user_input = InputManager.get_input()
        if is_number(user_input):
            company.try_to_destroy_order(company, user_input)
        else:
            print("Введен неправильный формат id")
            return