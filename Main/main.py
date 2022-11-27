from CouriersPro.Commands.AddCourier import AddCourierCommand
from CouriersPro.Commands.DebugCommand import DebugCommand
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
add_courier_command = AddCourierCommand
ListOfCommands = [debug_Command, test_command, add_courier_command]
inputUser = input()


def get_array(start, length, step, startarray):
    array = []
    for i in range(start, length, step):
        array.append(startarray[i])
    return array

class Main():

    def find_command(self):
        for i in range(len(ListOfCommands)):
            ListOfCommands[i].execute_command(inputUser)

    def get_max_size(self):
        CouriersMaxSizeOrders.append(get_array(3, len(M), 4, M))

    def get_id_courier(self):
        CouriersArray.append(get_array(0, len(M), 4, M))

    def size_of_order(self):
        OrdersSizeArray.append(get_array(3, len(N), 4, N))

    size_of_order()
    get_max_size()
    get_id_courier()
    find_command()
