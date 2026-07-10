# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        if self.__cents>=10:
            return f"{self.__euros}.{self.__cents} eur" 
        else:
            return f"{self.__euros}.0{self.__cents} eur"
        
    def __eq__(self, value):
        return self.__cents == value.__cents and self.__euros == value.__euros
    
    def __ne__(self, value):
        return self.__cents != value.__cents or self.__euros != value.__euros
    
    def __lt__(self, other):
        if self.__euros == other.__euros:
            return self.__cents < other.__cents
        return self.__euros < other.__euros

    def __gt__(self, other):
        if self.__euros == other.__euros:
            return self.__cents > other.__cents
        return self.__euros > other.__euros
    
    def __add__(self, other):
        total = Money(0, 0)
        total.__euros = self.__euros+other.__euros
        total.__cents = self.__cents+other.__cents

        if total.__cents>=100:
            total.__euros+=1
            total.__cents-=100

        return total
    
    def __sub__(self, other):
        total = Money(0, 0)
        total.__euros = self.__euros-other.__euros
        total.__cents = self.__cents-other.__cents 
        if total.__euros<0 or total.__euros==0 and total.__cents<0:
            raise ValueError(f"a negative result is not allowed")
        if total.__cents<0:
            total.__euros-=1
            total.__cents+=100

        return total       


