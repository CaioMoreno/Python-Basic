# Write your solution here:
class Task:
    id = 0
    def __init__(self, description: str, programmer: str, workload: int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.status = "NOT FINISHED"
        Task.id+=1
        self.id = Task.id

    def is_finished(self):
        return self.status == "FINISHED"
    
    def mark_finished(self):
        self.status = "FINISHED"
    
    def __repr__(self):
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {self.status}"
    
class OrderBook:
    def __init__(self):
        self.orders = []
    
    def add_order(self, description: str, programmer: str, workload: int):
        self.orders.append(Task(description, programmer, workload))

    def all_orders(self):
        return self.orders

    def programmers(self):
        return sorted(set(name.programmer for name in self.orders))
    
    def mark_finished(self, id: int):
        found=0
        for order in self.orders:
            if id == order.id:
                found=1 
                order.mark_finished()
        if found == 0:
            raise ValueError

    def finished_orders(self):
        return [order for order in self.orders if order.is_finished()]

    def unfinished_orders(self):
        return [order for order in self.orders if not order.is_finished()]
    
    def status_of_programmer(self, programmer: str):
        finished = [order for order in self.orders if order.is_finished() and order.programmer == programmer]
        unifinished = [order for order in self.orders if not order.is_finished() and order.programmer == programmer]
        fin_orders = 0
        unf_orders = 0
        found = 0
        for order in self.orders:
            if order.programmer == programmer:
                found = 1
                if order.is_finished():
                    fin_orders += order.workload
                else:
                    unf_orders += order.workload
        if found == 0:
            raise ValueError
            
        return (len(finished), len(unifinished), fin_orders, unf_orders)


