from CouriersPro.Commands.CompanyCommands.ICommand import ICommand

cmd = "Stop"


class StopCommand(ICommand):
    def execute_command(self, command):
        if command == cmd:
            exit()

    @staticmethod
    def get_command_name():
        return cmd