from CouriersPro.Commands.ICommand import ICommand
from CouriersPro.Order.Manager.OrderManager import order_manager

cmd = "AddOrder"


class AddOrder(ICommand):
    def execute_command(self, command):
        if command.casefold() == cmd.casefold():
            order_manager.create_order()
            return

    @staticmethod
    def get_command_name():
        return cmd
