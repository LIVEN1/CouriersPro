from CouriersPro.Commands.CompanyCommands.Run import StartProgram
from CouriersPro.Commands.CompanyCommands.AddCourier import AddCourierCommand
from CouriersPro.Commands.CompanyCommands.AddOrder import AddOrder
from CouriersPro.Commands.OtherCommands.DebugCommand import DebugCommand
from CouriersPro.Commands.CompanyCommands.DestroyOrder import DestroyOrder
from CouriersPro.Commands.OtherCommands.HelpCommand import HelpCommand
from CouriersPro.Commands.OtherCommands.StopCommand import StopCommand
from CouriersPro.Commands.OtherCommands.TestCommand import TestCommand
from CouriersPro.Commands.CompanyCommands.DestroyCourier import DestroyCourier
from CouriersPro.FolderOfSetting.DebugModeController import DebugModeController
from CouriersPro.InputManager.InputManager import InputManager
from CouriersPro.Tests.CreateCouriers import CourierCreator
from CouriersPro.Tests.CreateOrders import OrderCreator


ListOfCommands = [DebugCommand, AddCourierCommand, TestCommand, HelpCommand, StopCommand, DestroyOrder, AddOrder,
                  DestroyCourier, StartProgram, OrderCreator, CourierCreator]


def find_command():
    for i in range(len(ListOfCommands)):
        ListOfCommands[i].execute_command(ListOfCommands[i], inputUser)


while True:
    inputUser = InputManager.get_input()
    find_command()
