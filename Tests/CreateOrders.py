import random
from CouriersPro.Commands.CompanyCommands.ICommand import ICommand
from CouriersPro.Company.Manager.CompanyManager import company
from CouriersPro.FolderOfSetting.DebugModeController import debug_mode_controller
from CouriersPro.InputManager.InputManager import InputManager
from CouriersPro.Order.Order import Order

cmd = "CO"



class OrderCreator(ICommand):
    def execute_command(self, command):
        if command.casefold() == cmd.casefold():
            if debug_mode_controller.is_debug_mode():
                self.create_orders(self)

    def create_orders(self):
        print("Введите количетсво нужных заказов")
        value = InputManager.get_input()
        if InputManager.is_number(value) and int(value) > 0:
            for i in range(int(value)):
                order = Order(self.__get_random_coordinates__(), self.__get_random_coordinates__(),
                              self.__get_random_weight())
                company.add_order(order)

    @staticmethod
    def __get_random_coordinates__():
        return random.randint(1, 15)

    @staticmethod
    def __get_random_weight():
        return random.randint(1, 3)
