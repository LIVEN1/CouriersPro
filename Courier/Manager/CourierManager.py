from CouriersPro.Company.Delivery.DeliveryManager import company
from CouriersPro.Courier.TypeOfCouriers.Courier import Courier
from CouriersPro.InputManager.InputManager import InputManager


class CourierManager:
    @staticmethod
    def add_courier():
        print("Введите координаты начала через пробел(x y).")
        coordinates = InputManager.get_input()
        if InputManager.is_number(coordinates) and InputManager.check_length_array(coordinates, 2):
            coordinates_array = coordinates.split(" ")
            x_coord = int(coordinates_array[0])
            y_coord = int(coordinates_array[1])
            print("Введите вместимость рюкзака")
            weight = InputManager.get_input()
            if InputManager.is_number(weight) and InputManager.check_length_array(weight, 1):
                if int(weight) > 0:
                    courier = Courier(x_coord, y_coord, int(weight))
                    company.add_courier(courier)
                    print("Курьер создан")



    @staticmethod
    def get_courier_info():
        couriers = company.get_couriers()
        if len(couriers) < 1:
            print("Недостаточно курьеров")
            return

        print("Введите id нужного курьера")

        for courier in couriers:
            print(courier.id)

        id_courier = InputManager.get_input()
        for courier in couriers:
            if str(courier.id) == id_courier:
                print("Курьер найден")
                print("Местоположение курьера: " + str(courier.x_coord) + "," + str(courier.y_coord))
                print("Вместимость рюкзака: " + str(courier.backpack_weight))
                return
        else:
            print("Курьер не найден")


courier_manager = CourierManager()
