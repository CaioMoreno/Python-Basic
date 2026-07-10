# WRITE YOUR SOLUTION HERE:
class ListHelper:
    def __init__(self):
        pass
    
    @staticmethod
    def amount_qtt(self, my_list: list):
        amount={}
        for n in my_list:
            if n not in amount:
                amount[n]=1
            else:
                amount[n]+=1
        return amount
    
    @classmethod
    def greatest_frequency(cls, my_list: list):
        amount = cls.amount_qtt(my_list)

        quantity=0
        greatest=None
        for n in amount:
            if amount[n]>quantity:
                quantity=amount[n]
                greatest=n

        return greatest

    @classmethod
    def doubles(cls, my_list: list):
        amount=cls.amount_qtt(cls, my_list)
        quantity=0
        for n in amount:
            if amount[n]>=2:
                quantity+=1
        
        return quantity


