from CouriersPro.Company.Manager.DeliveryManager import company
from CouriersPro.InputManager.InputManager import InputManager
from CouriersPro.Order.Order import Order


class OrderManager:
    @staticmethod
    def create_order():
        print("Введите координаты начала через пробел(x y).")
        coordinates = InputManager.get_input()
        coordinates_array = coordinates.split()
        if InputManager.is_number(coordinates_array):
            if len(coordinates_array) < 2:
                print("Error")
                return

            x_coord = int(coordinates_array[0])
            y_coord = int(coordinates_array[1])
            print("Введите Вес Груза")
            weight = InputManager.get_input()
            if InputManager.is_number(weight) and int(weight) > 0:
                order = Order(x_coord, y_coord, int(weight))
                company.add_order(order)
            





    @staticmethod
    def get_order_info():
        orders = company.get_orders()
        for order in orders:
            print(order.id)

        id = InputManager.get_input()
        for order in orders:
            if str(order.id) == id:
                print("Заказ найден")
                print("Координаты заказа: " + str(order.x_coord) + ", " + str(order.y_coord))
                print("Масса заказа: " + str(order.weight))
                return
        else:
            print("Заказ не найден")


order_manager = OrderManager()
