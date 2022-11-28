from CouriersPro.Commands.AddCourier import AddCourierCommand
from CouriersPro.Commands.DebugCommand import DebugCommand
from CouriersPro.Commands.ICommand import ICommand
from CouriersPro.Commands.StopCommand import StopCommand
from CouriersPro.Commands.TestCommand import TestCommand

cmd = "Help"
debug_command_cmd = DebugCommand.get_command_name(0)
test_command_name = TestCommand.get_command_name(0)
add_courier_name = AddCourierCommand.get_command_name(0)
stop_command_name = StopCommand.get_command_name(0)


class HelpCommand(ICommand):
    def execute_command(self):
        if cmd == self:
            print(cmd, add_courier_name, stop_command_name)

    def get_command_name(self):
        return cmd
