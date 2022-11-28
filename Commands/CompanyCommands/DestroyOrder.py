from CouriersPro.Commands.CompanyCommands.ICommand import ICommand
from CouriersPro.Managers.OrderManager import OrderManager

cmd = "DestroyOrder"

class DestroyOrder(ICommand):
    def execute_command(self, command):
        if command == cmd:
            OrderManager.destroy_order()

    @staticmethod
    def get_command_name():
        return cmd