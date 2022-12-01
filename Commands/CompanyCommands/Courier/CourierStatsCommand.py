from CouriersPro.Commands.CompanyCommands.ICommand import ICommand
from CouriersPro.Courier.Manager.CourierManager import courier_manager


cmd = "GetCourierInfo"


class CourierStatsCommand(ICommand):
    def execute_command(self, command):
        if command.casefold() == cmd.casefold():
            print("Введите id нужного курьера")
            courier_manager.get_courier_info()

    @staticmethod
    def get_command_name():
        return cmd
