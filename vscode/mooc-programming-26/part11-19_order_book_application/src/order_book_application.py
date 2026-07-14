# Write your solution here
# If you use the classes made in the previous exercise, copy them here
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

class OrderBookApplication():
    def __init__(self):
        self.__OrderBook = OrderBook()

    def help(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")
     
    def add_order(self):
        description = input("description: ")
        try:
            programmer, workload = input("programmer and workload estimate: ").split()     
            workload = int(workload)
        except ValueError:
            print("erroneous input")
            return
        self.__OrderBook.add_order(description, programmer, workload)
        print("added!")

    def list_finished_tasks(self):
        finished = self.__OrderBook.finished_orders()
        if finished:
            for order in finished:
                print(order)
        else:
            print("no finished tasks")

    def list_unfinished_tasks(self):
        unfinished = self.__OrderBook.unfinished_orders()
        for order in unfinished:
            print(order)

    def mark_finished(self):
        try:
            id = int(input("id: "))
            self.__OrderBook.mark_finished(id)
            print("marked as finished")
        except ValueError:
            print("erroneous input")

    def programmers(self):
        programmers = self.__OrderBook.programmers()
        for order in programmers:
            print(order)

    def status_of_programmer(self):
        programmer = input("programmer: ")
        try:
            tasks = self.__OrderBook.status_of_programmer(programmer)
        except ValueError:
            print("erroneous input")
            return
        print(f"tasks: finished {tasks[0]} not finished {tasks[1]}, hours: done {tasks[2]} scheduled {tasks[3]}")

    def execute(self):
        self.help()
        while True:
            print("")
            command = int(input("command: "))
            if command == 0:
                break
            elif command == 1:
                self.add_order()
            elif command == 2:
                self.list_finished_tasks()
            elif command == 3:
                self.list_unfinished_tasks()
            elif command == 4:
                self.mark_finished()
            elif command == 5:
                self.programmers()
            elif command == 6:
                self.status_of_programmer()
            else:
                self.help()
               
application = OrderBookApplication()
application.execute()       

