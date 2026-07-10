# Write your solution here:
class Item:
    def __init__(self, name: str, weight: float):
        self.__weight=weight
        self.__name=name

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight
    
    def __str__(self):
        return f"{self.name()} ({self.weight()} kg)"
    
class Suitcase:
    def __init__(self, max_weight: float):
        self.max_weight=max_weight
        self.case_weight=0
        self.items=[]
    
    def add_item(self, item: Item):
        self.case_weight+=item.weight()
        if self.case_weight<=self.max_weight:
            self.items.append(item)
        else:
            self.case_weight-=item.weight()

    def print_items(self):
        for i in self.items:
            print(i)

    def weight(self):
        total_w=0

        for i in self.items:
            total_w+=i.weight()
        
        return int(total_w)
    
    def heaviest_item(self):
        heavy=0

        if self.items==[]:
            return None
        
        for i in self.items:
            if i.weight()>heavy:
                heavy=i.weight()
                heaviest=i

        return heaviest

    def __str__(self):
        if len(self.items)==1:
            return f"{len(self.items)} item ({self.case_weight} kg)"
        return f"{len(self.items)} items ({self.case_weight} kg)"
    
class CargoHold:
    def __init__(self, max_weight: float):
        self.max_weight=max_weight
        self.total=[]

    def add_suitcase(self, suitcase: Suitcase):
        self.max_weight-=suitcase.weight()
        if self.max_weight>=0:
            self.total.append(suitcase)
        else:
            self.max_weight+=suitcase.weight()

    def print_items(self):
        for suitcases in self.total:
            suitcases.print_items()

    def __str__(self):
        if len(self.total)==1:
            return f"{len(self.total)} suitcase, space for {self.max_weight} kg"
        return f"{len(self.total)} suitcases, space for {self.max_weight} kg"

