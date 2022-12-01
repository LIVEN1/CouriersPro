from CouriersPro.Company.Delivery.DeliveryManager import company
from CouriersPro.InputManager.InputManager import InputManager
from CouriersPro.Order.Order import Order


class OrderManager:
    @staticmethod
    def create_order():
        print("Введите координаты начала через пробел(x y).")
        coordinates = InputManager.get_input()
        if InputManager.is_number(coordinates) and InputManager.check_length_array(coordinates, 2):
            coordinates_array = coordinates.split(" ")
            x_coord = int(coordinates_array[0])
            y_coord = int(coordinates_array[1])
            print("Введите Вес Груза")
            weight = InputManager.get_input()
            if InputManager.is_number(weight) and InputManager.check_length_array(weight, 1):
                if int(weight) > 0:
                    order = Order(x_coord, y_coord, int(weight))
                    company.add_order(order)
                    print("Заказ создан")

    @staticmethod
    def get_order_info():
        orders = company.get_orders()
        if len(orders) < 1:
            print("Недостаточно заказов")
            return

        print("Введите id нужного заказа")


        for order in orders:
            print(str(order.id))


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
