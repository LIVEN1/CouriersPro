list_of_couriers = []


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
    def start_program(self):
        print("Program is Started")
        get_right_count_of_couriers(self)
