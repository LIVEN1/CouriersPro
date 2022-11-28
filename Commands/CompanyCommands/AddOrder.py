from CouriersPro.Commands.CompanyCommands.ICommand import ICommand
from CouriersPro.Managers.OrderManager import OrderManager

cmd = "AddOrder"


class AddOrder(ICommand):
    def execute_command(self, command):
        if  command == cmd:
            OrderManager.create_order()

    @staticmethod
    def get_command_name():
        return cmd
