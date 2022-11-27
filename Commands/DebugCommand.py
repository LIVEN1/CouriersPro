from CouriersPro.Commands.ICommand import ICommand

cmd = "Debug"


class DebugCommand(ICommand):
    def execute_command(self):
        if cmd == self:
            print("Debug On")

    def get_command_name(self):
        return cmd