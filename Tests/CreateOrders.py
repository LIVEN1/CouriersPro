import random
from CouriersPro.Commands.CompanyCommands.ICommand import ICommand
from CouriersPro.Company.Company import Company
from CouriersPro.FolderOfSetting import DebugModeController
from CouriersPro.Order.Order import Order

cmd = "CO"
company = Company
debug_mode = DebugModeController


class OrderCreator(ICommand):
    def execute_command(self, command):
        if command == cmd:
            if debug_mode.DebugModeController.is_debug_mode(debug_mode):
                self.create_orders(self)

    def create_orders(self):
        print("Debug mode is: " + str(debug_mode.DebugModeController.is_debug_mode(debug_mode)))
        print("Введите количетсво нужных заказов")
        value = input()
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
