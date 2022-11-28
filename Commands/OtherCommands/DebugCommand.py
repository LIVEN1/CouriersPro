from CouriersPro.Commands.CompanyCommands.ICommand import ICommand
from CouriersPro.FolderOfSetting import DebugModeController

cmd = "Debug"
debug_mode = DebugModeController



class DebugCommand(ICommand):

    def execute_command(self, command):
        if command == cmd:
            print("Debug mode on")
            debug_mode.DebugModeControoler.set_debug_mode(debug_mode, True)


    @staticmethod
    def get_command_name():
        return cmd


