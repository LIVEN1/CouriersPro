from CouriersPro.Commands.CompanyCommands.ICommand import ICommand
from CouriersPro.Company.Manager.DeliveryManager import delivery_manager

cmd = "Run"


class StartProgram(ICommand):
    def execute_command(self, command):
        if command.casefold() == cmd.casefold():
            delivery_manager.start_program()
            return

    @staticmethod
    def get_command_name():
        return cmd
