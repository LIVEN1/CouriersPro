from CouriersPro.Commands.ICommand import ICommand
from CouriersPro.Courier.Manager.CourierManager import courier_manager

cmd = "AddCourier"


class AddCourier(ICommand):
    def execute_command(self, command):
        if command.casefold() == cmd.casefold():
            courier_manager.add_courier()
            return


    @staticmethod
    def get_command_name():
        return cmd
