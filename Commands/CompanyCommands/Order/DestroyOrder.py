from CouriersPro.Commands.CompanyCommands.ICommand import ICommand
from CouriersPro.Order.Manager.OrderManager import OrderManager

cmd = "DestroyOrder"


class DestroyOrder(ICommand):
    def execute_command(self, command):
        if command == cmd:
            OrderManager.destroy_order()
            return

    @staticmethod
    def get_command_name():
        return cmd
