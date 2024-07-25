import multiprocessing

class WarehouseManager():
    def __init__(self):
        self.data = multiprocessing.Manager().dict()

    def process_request(self, requests):
        if requests[0] not in self.data:
            self.data[requests[0]] = requests[2]
        else:
            if requests[1] == 'receipt':
                self.data[requests[0]] += requests[2]
            elif requests[1] == 'shipment':
                self.data[requests[0]] -= requests[2]
        #print(self.data)
        return self.data


    def run(self, requests):
        self.requests = requests

        with multiprocessing.Pool(processes=2) as pool:
            res = pool.map(self.process_request, self.requests)
            #for i in res:
            #    print(i)
        return self.data


if __name__ == '__main__':
    manager = WarehouseManager()


    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]

    manager.run(requests)
    print(manager.data)

#Цель:
#{"product1": 70, "product2": 100, "product3": 200}