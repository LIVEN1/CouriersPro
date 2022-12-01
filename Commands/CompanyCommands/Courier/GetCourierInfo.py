from CouriersPro.Commands.ICommand import ICommand
from CouriersPro.Courier.Manager.CourierManager import courier_manager


cmd = "GetCourierInfo"


class GetCourierInfo(ICommand):
    def execute_command(self, command):
        if command.casefold() == cmd.casefold():
            courier_manager.get_courier_info()
            return

    @staticmethod
    def get_command_name():
        return cmd
