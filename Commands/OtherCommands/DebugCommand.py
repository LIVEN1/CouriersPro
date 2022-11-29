from CouriersPro.Commands.CompanyCommands.ICommand import ICommand
from CouriersPro.FolderOfSetting.DebugModeController import DebugModeController

cmd = "Debug"
debug_mode = DebugModeController



class DebugCommand(ICommand):

    def execute_command(self, command):
        if command.casefold() == cmd.casefold():
            print("Debug mode on")
            debug_mode.set_debug_mode(debug_mode, True)
            return


    @staticmethod
    def get_command_name():
        return cmd


