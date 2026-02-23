def gcd(a,b):
    a,b = max(a,b),min(a,b)
    while a and b:
        a,b = b,a%b
    return a
class Fraction:
    def __init__(self,fenzi,fenmu):
        if fenmu < 0:
            fenzi = -fenzi
            fenmu = -fenmu
        self.fenzi = fenzi
        self.fenmu = fenmu
    
    def show(self):
        print(str(self.fenzi)+"/"+str(self.fenmu))
    
    def huajian(self):
        a,b = self.fenzi,self.fenmu
        if a == 0:
            return Fraction(0,1)
        t = gcd(abs(a),abs(b))
        return Fraction(a//t,b//t)

    def __add__(self,Fraction1):
        qitafenzi = Fraction1.fenzi
        qitafenmu = Fraction1.fenmu
        newfenmu = qitafenmu*self.fenmu
        newfenzi = (qitafenzi*self.fenmu)+(self.fenzi*qitafenmu)
        return Fraction(newfenzi,newfenmu).huajian()
a,b,c,d = map(int,input().split())
f1 = Fraction(a,b)
f2 = Fraction(c,d)
f = f1+f2
f.show()