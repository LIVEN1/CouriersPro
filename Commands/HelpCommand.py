from CouriersPro.Commands.DebugCommand import DebugCommand
from CouriersPro.Commands.ICommand import ICommand
from CouriersPro.Commands.TestCommand import TestCommand

cmd = "Help"
debug_command_cmd = DebugCommand.get_command_name(0)
test_command_name = TestCommand.get_command_name(0)


class HelpCommand(ICommand):
    def execute_command(self):
        if cmd == self:
            print(cmd, debug_command_cmd, test_command_name)

    def get_command_name(self):
        return cmd
