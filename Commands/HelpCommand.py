from CouriersPro.Commands.AddCourier import AddCourierCommand
from CouriersPro.Commands.AddOrder import AddOrder
from CouriersPro.Commands.DebugCommand import DebugCommand
from CouriersPro.Commands.DestroyOrder import DestroyOrder
from CouriersPro.Commands.ICommand import ICommand
from CouriersPro.Commands.StopCommand import StopCommand
from CouriersPro.Commands.TestCommand import TestCommand
from CouriersPro.Commands.DestroyCourier import DestroyCourier

cmd = "Help"


class HelpCommand(ICommand):
    def execute_command(command):
        if cmd == command:
            print(cmd, StopCommand.get_command_name(), AddOrder.get_command_name(), DebugCommand.get_command_name(),
                  DestroyOrder.get_command_name(), AddCourierCommand.get_command_name(), DestroyCourier.get_command_name())

    @staticmethod
    def get_command_name():
        return cmd
