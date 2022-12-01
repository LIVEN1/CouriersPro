from CouriersPro.Commands.ICommand import ICommand
from CouriersPro.Order.Manager.OrderManager import order_manager

cmd = "GetOrderInfo"


class GetOrderInfo(ICommand):
    def execute_command(self, command):
        if command.casefold() == cmd.casefold():
            order_manager.get_order_info()
            return

    @staticmethod
    def get_command_name():
        return cmd
