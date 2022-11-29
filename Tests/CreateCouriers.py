import random
from CouriersPro.Commands.CompanyCommands.ICommand import ICommand
from CouriersPro.Company.Manager.CompanyManager import CompanyManager
from CouriersPro.Courier.TypeOfCouriers.Courier import Courier
from CouriersPro.FolderOfSetting.DebugModeController import DebugModeController
from CouriersPro.InputManager.InputManager import InputManager

cmd = "CC"
company = CompanyManager
debug_controller = DebugModeController


class CourierCreator(ICommand):
    def execute_command(self, command):
        if command.casefold() == cmd.casefold():
            if debug_controller.is_debug_mode(DebugModeController):
                self.create_courier(self)
                return

    def create_courier(self):
        print("Введите количетсво нужных курьеров")
        value = InputManager.get_input()
        if InputManager.is_number(value) and int(value) > 0:
            for i in range(int(value)):
                get_id = company.get_couriers_count() + 1
                courier = Courier(get_id, self.__get_random_coordinates__(), self.__get_random_coordinates__(),
                                  self.__get_random_weight())
                company.add_courier(company, courier)

    @staticmethod
    def __get_random_coordinates__():
        return random.randint(1, 15)

    @staticmethod
    def __get_random_weight():
        return random.randint(1, 6)
