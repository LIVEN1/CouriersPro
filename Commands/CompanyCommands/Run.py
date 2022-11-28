from CouriersPro.Commands.CompanyCommands.ICommand import ICommand
from CouriersPro.Managers.CompanyManager import CompanyManager

cmd = "Run"
companyManager = CompanyManager


class StartProgram(ICommand):
    def execute_command(self, command):
        if command == cmd:
            if companyManager.get_couriers_count() <= 0 | companyManager.get_orders_count() <= 0:
                print("Недостаточно курьеров/заказаов")
                return

            else:
                companyManager.start_program(companyManager)

    @staticmethod
    def get_command_name():
        return cmd