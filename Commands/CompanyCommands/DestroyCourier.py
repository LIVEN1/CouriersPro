from CouriersPro.Commands.CompanyCommands.ICommand import ICommand
from CouriersPro.Managers.CourierManager import CourierManager

cmd = "DestroyCourier"

class DestroyCourier(ICommand):
    def execute_command(self, command):
        if command == cmd:
            CourierManager.destroy_courier()

    @staticmethod
    def get_command_name():
        return cmd