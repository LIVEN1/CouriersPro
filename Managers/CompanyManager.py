from CouriersPro.Company.Company import Company

order_query = []

dictionary = dict()


class CompanyManager(Company):
    def start_program(self):
        self.check_weight()

    @staticmethod
    def check_distance():
        orders = Company.get_orders()
        couriers = Company.get_couriers()
        for i in range(len(orders)):
            order = orders[i]
            for i in range(len(couriers)):
                result = (orders[i].x_coord - couriers[i].x_coord) ** 2 + (orders[i].y_coord - couriers[i].y_coord) ** 2
                order_query.append(result)
            sorted(order_query)
            best_order_distance = order_query[0]

    @staticmethod
    def check_weight():
        orders = Company.get_orders()
        couriers = Company.get_couriers()
        for order in orders:
            order_query.append(order)
            print(order.weight)
            for courier in couriers:
                if courier.maxWeight < order.weight:
                    print(courier.maxWeight)
                    return
                order_query.append(courier)
                print(courier.maxWeight)
                print(order_query)
            if len(order_query) == 2:
                courier.attach_order(order)
