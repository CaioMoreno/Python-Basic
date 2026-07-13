# Write your solution here:
class Task:
    id = 0
    def __init__(self, description, programmer, workload):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.status = "NOT FINISHED"
        Task.id += 1

    def is_finished(self):
        return self.status == "FINISHED"
    
    def mark_finished(self):
        self.status = "FINISHED"
    
    def __repr__(self):
        return f"{Task.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {self.status}"
    

t1 = Task("program hello world", "Eric", 3)
print(t1.id, t1.description, t1.programmer, t1.workload)
print(t1)
print(t1.is_finished())
t1.mark_finished()
print(t1)
print(t1.is_finished())
t2 = Task("program webstore", "Adele", 10)
t3 = Task("program mobile app for workload accounting", "Eric", 25)
print(t2)
print(t3)