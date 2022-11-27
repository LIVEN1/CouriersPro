f = open('couriers.txt')
M = [int(r) for r in f]
f = open('orders.txt')
N = [int(t) for t in f]
CouriersMaxSizeOrders = []
CouriersArray = []
OrdersSizeArray = []


def GetMaxSize():
    CouriersMaxSizeOrders.append(GetArray(3, len(M), 4, M))
    print(CouriersMaxSizeOrders)


def GetIdCourier():
    CouriersArray.append(GetArray(0, len(M), 4, M))
    print(CouriersArray)


def GetArray(start, length, step, startarray):
    array = []
    for i in range(start, length, step):
        array.append(startarray[i])
    return array


def SizeOfOrder():
    OrdersSizeArray.append(GetArray(3, len(N), 4, N))
    print(OrdersSizeArray)

SizeOfOrder()
GetMaxSize()
GetIdCourier()