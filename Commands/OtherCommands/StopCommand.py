from CouriersPro.Commands.ICommand import ICommand

cmd = "Stop"


class StopCommand(ICommand):
    def execute_command(self, command):
        if command.casefold() == cmd.casefold():
            exit()

    @staticmethod
    def get_command_name():
        return cmd