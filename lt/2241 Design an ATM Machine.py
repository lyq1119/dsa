def add(list1,list2):
    return [list1[i]+list2[i] for i in range(5)]
def fan(list1):
    return [-list1[i] for i in range(5)]
class ATM:
    def __init__(self):
        self.atm = [0 for _ in range(5)]
    def deposit(self, banknotesCount) -> None:
        self.atm = add(self.atm,banknotesCount)
    def withdraw(self, amount: int):
        origin = self.atm.copy()
        t = 1
        while t and amount:
            if amount >= 500 and self.atm[-1]:
                t = min(amount//500,self.atm[-1])
                amount -= 500*t
                self.atm[-1] -= t
            elif amount >= 200 and self.atm[-2]:
                t = min(amount//200,self.atm[-2])
                amount -= 200*t
                self.atm[-2] -= t
            elif amount >= 100 and self.atm[2]:
                t = min(amount//100,self.atm[2])
                amount -= 100*t
                self.atm[2] -= t
            elif amount >= 50 and self.atm[1]:
                t = min(amount//50,self.atm[1])
                amount -= 50*t
                self.atm[1] -= t
            elif amount >= 20 and self.atm[0]:
                t = min(amount//20,self.atm[0])
                amount -= 20*t
                self.atm[0] -= t
            else:
                self.atm = origin
                return [-1]
        if amount:
            self.atm = origin
            return [-1]
        return add(origin,fan(self.atm))
engine = ATM()
engine.deposit([0,10,0,3,0])
print(engine.withdraw(500))
