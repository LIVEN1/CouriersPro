from CouriersPro.Commands.CompanyCommands.ICommand import ICommand
from CouriersPro.Company.Manager.CompanyManager import company_manager

cmd = "Run"


class StartProgram(ICommand):
    def execute_command(self, command):
        if command.casefold() == cmd.casefold():
            company_manager.start_program()
            return

    @staticmethod
    def get_command_name():
        return cmd
