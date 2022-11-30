from CouriersPro.Company.Manager.CompanyManager import company
from CouriersPro.Courier.TypeOfCouriers.Courier import Courier
from CouriersPro.InputManager.InputManager import InputManager


class CourierManager:
    @staticmethod
    def add_courier():
        print("Введите координаты начала через пробел(x y).")
        coordinates = InputManager.get_input()
        coordinates_array = coordinates.split()
        x_coord = coordinates_array[0]
        y_coord = coordinates_array[1]
        if InputManager.is_number(coordinates_array):
            print("Введите вместимость рюкзака")
            weight = InputManager.get_input()
            if InputManager.is_number(weight):
                courier = Courier(x_coord, y_coord, weight)
                company.add_courier(courier)
        else:
            print("Введены неправильные данные")
            return

    @staticmethod
    def destroy_courier():
        print("Введите айди нужного курьера")
        print(company.get_couriers_count())
        courier_id = InputManager.get_input()
        if InputManager.is_number(courier_id):
            company.try_to_destroy_courier(courier_id)
        else:
            print("Введен неправильный формат id")
            return

    @staticmethod
    def get_courier_info():
        couriers = company.get_couriers()
        for i in range(len(couriers)):
            print(couriers[i].id)

        id_courier = InputManager.get_input()
        for courier in couriers:
            if str(courier.id) == id_courier:
                print("Курьер найден")
                print("Местоположение курьера: " + str(courier.x_coord) + "," + str(courier.y_coord))
                print("Вместимость рюкзака: " + str(courier.maxWeight))
                return
        else:
            print("Курьер не найден")


courier_manager = CourierManager()
