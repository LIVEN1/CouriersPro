from CouriersPro.Commands.AddCourier import AddCourierCommand
from CouriersPro.Commands.DebugCommand import DebugCommand
from CouriersPro.Commands.HelpCommand import HelpCommand
from CouriersPro.Commands.StopCommand import StopCommand
from CouriersPro.Commands.TestCommand import TestCommand

f = open('../couriers.txt')
M = [int(r) for r in f]
f = open('../orders.txt')
N = [int(t) for t in f]
CouriersMaxSizeOrders = []
CouriersArray = []
OrdersSizeArray = []
debug_Command = DebugCommand
test_command = TestCommand
help_command = HelpCommand
add_courier_command = AddCourierCommand
exit_command = StopCommand
ListOfCommands = [debug_Command, test_command, add_courier_command, help_command, StopCommand]
a = 1


def get_array(start, length, step, startarray):
    array = []
    for i in range(start, length, step):
        array.append(startarray[i])
    return array


def find_command():
    for i in range(len(ListOfCommands)):
     ListOfCommands[i].execute_command(inputUser)


def get_max_size():
    CouriersMaxSizeOrders.append(get_array(3, len(M), 4, M))


def get_id_courier():
    CouriersArray.append(get_array(0, len(M), 4, M))


def size_of_order():
    OrdersSizeArray.append(get_array(3, len(N), 4, N))


while a == 1:
    inputUser = input()
    find_command()
