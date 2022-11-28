import random
from CouriersPro.Commands.CompanyCommands.ICommand import ICommand
from CouriersPro.Company.Company import Company
from CouriersPro.Courier.TypeOfCouriers.Courier import Courier
from CouriersPro.FolderOfSetting import DebugModeController

cmd = "CC"
company = Company
debug_mode = DebugModeController


class CourierCreator(ICommand):
    def execute_command(self, command):
        if command == cmd:
            if debug_mode.DebugModeController.is_debug_mode(debug_mode):
                self.create_courier(self)

    def create_courier(self):
        print("Debug mode is: " + str(debug_mode.DebugModeController.is_debug_mode(debug_mode)))
        print("Введите количетсво нужных курьеров")
        value = input()
        if int(value) > 0:
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
