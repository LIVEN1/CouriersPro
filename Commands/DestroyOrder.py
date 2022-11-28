from CouriersPro.Commands.ICommand import ICommand
from CouriersPro.Order.OrderManager import OrderManager

cmd = "DestroyOrder"

class DestroyOrder(ICommand):
    def execute_command(command):
        if command == cmd:
            OrderManager.destroy_order()

    @staticmethod
    def get_command_name():
        return cmd