from CouriersPro.Commands.ICommand import ICommand
from CouriersPro.Order.OrderManager import OrderManager

cmd = "AddOrder"


class AddOrder(ICommand):
    def execute_command(command):
        if  command == cmd:
            OrderManager.create_order()

    @staticmethod
    def get_command_name():
        return cmd
