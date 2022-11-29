import random
from CouriersPro.Commands.CompanyCommands.ICommand import ICommand
from CouriersPro.Company.Manager.CompanyManager import CompanyManager
from CouriersPro.FolderOfSetting.DebugModeController import DebugModeController
from CouriersPro.InputManager.InputManager import InputManager
from CouriersPro.Order.Order import Order

cmd = "CO"
company = CompanyManager
debug_controller = DebugModeController


class OrderCreator(ICommand):
    def execute_command(self, command):
        if command == cmd:
            if debug_controller.is_debug_mode(DebugModeController):
                self.create_orders(self)

    def create_orders(self):
        print("Введите количетсво нужных заказов")
        value = InputManager.get_input()
        if int(value) > 0:
            for i in range(int(value)):
                get_id = company.get_orders_count() + 1
                order = Order(get_id, self.__get_random_coordinates__(), self.__get_random_coordinates__(),
                              self.__get_random_weight())
                company.add_order(company, order)

    @staticmethod
    def __get_random_coordinates__():
        return random.randint(1, 15)

    @staticmethod
    def __get_random_weight():
        return random.randint(1, 3)
