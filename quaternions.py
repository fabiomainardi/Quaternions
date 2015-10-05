# Simple class for Quaternions
class Q():
    import math
    def __init__(self,a,b,c,d):
        self.a=float(a)
        self.b=float(b)
        self.c=float(c)
        self.d=float(d)
    def __str__(self):
        return(str(self.a)+"+i∙"+str(self.b)+"+j∙"+str(self.c)+"+k∙"+str(self.d))
    def conjugate(self):
        return Q(self.a, -self.b, -self.c, -self.d)
    def __mul__(self,q):
        a1=self.a
        b1=self.b
        c1=self.c
        d1=self.d
        if(isinstance(q, int) or isinstance(q,float)):
            a2=q
            b2=0
            c2=0
            d2=0
        else:
            a2=q.a
            b2=q.b
            c2=q.c
            d2=q.d
        return(Q(a1*a2 - b1*b2 - c1*c2 - d1*d2,
                 a1*b2 + b1*a2 + c1*d2 - d1*c2,
                 a1*c2 - b1*d2 + c1*a2 + d1*b2,
                 a1*d2 + b1*c2 - c1*b2 + d1*a2))
    def __add__(self,q):
        a1=self.a
        b1=self.b
        c1=self.c
        d1=self.d
        if(isinstance(q, int) or isinstance(q,float)):
            a2=q
            b2=0
            c2=0
            d2=0
        else:
            a2=q.a
            b2=q.b
            c2=q.c
            d2=q.d
        return(Q(a1+a2,b1+b2,c1+c2,d1+d2))
    def __sub__(self,q):
        a1=self.a
        b1=self.b
        c1=self.c
        d1=self.d
        if(isinstance(q, int) or isinstance(q,float)):
            a2=q
            b2=0
            c2=0
            d2=0
        else:
            a2=q.a
            b2=q.b
            c2=q.c
            d2=q.d
        return(Q(a1-a2,b1-b2,c1-c2,d1-d2))
    def norm(self):
        return(math.sqrt(self.a**2+self.b**2+self.c**2+self.d**2))
    def inverse(self):
        den=self.norm()**2
        return(Q(self.a/den,-self.b/den,-self.c/den,-self.d/den))
    def __truediv__(self,other):
        return self.__mul__(other.inverse())
    def __rmul__(self, other):
        return Q.__mul__(self, other) 
    def __rtruediv__(self, other):
        return other * self.reciprocal()
    def power(self,n):
        res=1
        if(n==0):
            return res
        else:
            for i in range(1,n+1):
                res=self.__mul__(res)
            return res
    __div__, __rdiv__ = __truediv__, __rtruediv__

#Examples
q1=Q(0,2,1,0.5)
q2=Q(0,1,-2.2,0)
i=Q(0,1,0,0)
print(q1)
quotient1=q1/q2
product1=q1*q2
product2=5*q1
product3=q2*3
print(i.power(3))