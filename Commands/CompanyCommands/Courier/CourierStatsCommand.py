from CouriersPro.Commands.CompanyCommands.ICommand import ICommand
from CouriersPro.Courier.Manager.CourierManager import CourierManager


cmd = "Get Courier Info"
courier_manager = CourierManager


class CourierStatsCommand(ICommand):
    def execute_command(self, command):
        if command == cmd:
            print("Введите id нужного курьера")
            courier_manager.get_courier_info()

    @staticmethod
    def get_command_name():
        return cmd
