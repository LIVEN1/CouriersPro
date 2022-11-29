from CouriersPro.Commands.CompanyCommands.ICommand import ICommand
from CouriersPro.Order.Manager.OrderManager import OrderManager

cmd = "AddOrder"


class AddOrder(ICommand):
    def execute_command(self, command):
        if command == cmd:
            OrderManager.create_order()
            return

    @staticmethod
    def get_command_name():
        return cmd
