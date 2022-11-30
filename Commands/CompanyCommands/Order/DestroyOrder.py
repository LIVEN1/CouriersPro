from CouriersPro.Commands.CompanyCommands.ICommand import ICommand
from CouriersPro.Order.Manager.OrderManager import order_manager

cmd = "DestroyOrder"


class DestroyOrder(ICommand):
    def execute_command(self, command):
        if command == cmd:
            order_manager.destroy_order()
            return

    @staticmethod
    def get_command_name():
        return cmd
