from CouriersPro.Commands.CompanyCommands.ICommand import ICommand
from CouriersPro.FolderOfSetting.DebugModeController import debug_mode_controller

cmd = "Debug"




class DebugCommand(ICommand):

    def execute_command(self, command):
        if command.casefold() == cmd.casefold():
            print("Debug mode on")
            debug_mode_controller.set_debug_mode(True)
            return


    @staticmethod
    def get_command_name():
        return cmd


