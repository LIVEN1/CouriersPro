from CouriersPro.Commands.CompanyCommands.ICommand import ICommand
from CouriersPro.Courier.Manager.CourierManager import CourierManager

cmd = "DestroyCourier"


class DestroyCourier(ICommand):
    def execute_command(self, command):
        if command.casefold() == cmd.casefold():
            CourierManager.destroy_courier()
            return

    @staticmethod
    def get_command_name():
        return cmd
