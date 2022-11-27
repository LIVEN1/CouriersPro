from CouriersPro.Commands.ICommand import ICommand

cmd = "Stop"


class StopCommand(ICommand):
    def execute_command(self):
        if self == cmd:
            exit()

    def get_command_name(self):
        return cmd