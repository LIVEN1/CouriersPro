list_of_couriers = []
list_of_orders = []


def get_count_of_couriers():
    print(list_of_couriers)


def get_start_index():
    if len(list_of_couriers) == 0:
        return 1
    else:
        return len(list_of_couriers)


def create_list_couriers(value):
    start_index = get_start_index()
    for i in range(start_index, value + 1):
        list_of_couriers.append(i)
    get_count_of_couriers()


def get_right_count_of_couriers(value):
    value_int = int(value)
    start_index = len(list_of_couriers)
    if (len(list_of_couriers) > 0):
        for i in range(start_index + 1, start_index + value_int + 1, 1):
            list_of_couriers.append(i)
        print(list_of_couriers)
    else:
        create_list_couriers(value_int)


class Company:
    __list_of_orders = []

    def start_program(self):
        print("Program is Started")
        get_right_count_of_couriers(self)

    def add_order(self, order):
        list_of_orders.append(order)
        print(list_of_orders)

    def try_to_destroy_order(self, id):
        if int(id) <= len(list_of_orders):
            list_of_orders.pop(int(id) - 1)
            print(list_of_orders)
        else:
            print("Id Больше Максимального")

    def get_orders_count(self):
        return len(list_of_orders)

    def get_orders(self):
        return list_of_orders

    def add_courier(self, courier):
        list_of_couriers.append(courier)
        print(list_of_couriers)
    def __init__(self):
        self.__list_of_orders = list_of_orders
