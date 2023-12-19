import math
import matplotlib.pyplot as plt

 
t0 = float(input("Введите t0 "))
print(t0)

x0 = float(input("Введите x0 "))
print(x0)

T = float(input("Введите T "))
print(T)

e = float(input("Введите ε "))
print(e) 

h = float(input("Введите h "))
print(h)

N = int((T - t0) / h)

def f(t,x):
    return -(t - 1) * x + t * math.sin(t) * math.exp(-((t - 1)**2))

def runge(h):

    x=[]
    t=[]
    S=[]
    x2=[]
    t2=[]
    S2=[]
    x.append(x0)
    t.append(t0)
    x2.append(x0)
    t2.append(t0)
    h2=h


    for i in range(0,N):
        k1=h*f(t[i],x[i])
        k2=h*f(t[i]+(h/2),x[i]+(k1/2))
        k3=h*f(t[i]+(h/2),x[i]+(k2/2))
        k4=h*f(t[i]+h,x[i]+k3)
        S.append((k1+2*k2+2*k3+k4)/6)
        x.append(x[i]+S[i])
        t.append(t[i]+i*h)

        k1h=h/2*f(t[i],x[i])
        k2h=h/2*f(t[i]+(h),x[i]+(k1h/2))
        k3h=h/2*f(t[i]+(h),x[i]+(k2h/2))
        k4h=h/2*f(t[i]+(h/2),x[i]+k3h)
        Sh=((k1h+2*k2h+2*k3h+k4h)/6)
        xh=x[i]+Sh

        k1hcap=h/2*f(t[i]+h/2,xh)
        k2hcap=h/2*f(t[i]+h+(h/2),xh+(k1hcap/2))
        k3hcap=h/2*f(t[i]+(h)+(h/2),xh+(k2hcap/2))
        k4hcap=h/2*f(t[i]+(h/2)+(h/2),xh+k3hcap)
        Shcap=((k1hcap+2*k2hcap+2*k3hcap+k4hcap)/6)
        xcap=xh+Shcap
        delta=abs(xcap-xh)/((2**4)-1)

        if delta>abs(xcap-(x[i]*t[i+1])):
            while delta>e:
             h= h/2
        

    for i2 in range(0,N):
        k12=h2*f(t2[i2],x2[i2])
        k22=h2*f(t2[i2]+(h2/2),x2[i2]+(k12/2))
        k32=h2*f(t2[i2]+(h2/2),x2[i2]+(k22/2))
        k42=h2*f(t2[i2]+h2,x2[i2]+k32)
        S2.append((k12+2*k22+2*k32+k42)/6)
        x2.append(x2[i2]+S2[i2])
        t2.append(t2[i2]+i2*h2)    


    plt.plot(x2, t2,color="r")
    plt.plot(x, t)
    plt.legend(['график 1', 'график 2'])
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid()
    plt.show()


def eyler(h):
    x=[]
    t=[]
    S=[]
    x2=[]
    t2=[]
    S2=[]
    x.append(x0)
    t.append(t0)
    x2.append(x0)
    t2.append(t0)
    h2=h
    for i in range(0,N):
        S.append(h*f(t[i],x[i]))
        x.append(x[i]+S[i])
        t.append(t[i]+i*h)

        Sh=(h/2*f(t[i],x[i]))
        xh=x[i]+Sh
        Shcap=(h/2*f(t[i]+h/2,xh))
        xcap=xh+Shcap
        delta=abs(xcap-xh)/((2**2)-1)

        if delta>abs(xcap-(x[i]*t[i+1])):
            while delta>e:
             print(h)
             h= h/2
             
    for i2 in range(0,N):
        S2.append(h2*f(t2[i2],x2[i2]))
        x2.append(x2[i2]+S2[i2])
        t2.append(t2[i2]+i2*h2)

    plt.plot(x2, t2,color="r")
    plt.plot(x, t)
    plt.legend(['график 1', 'график 2'])
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid()
    plt.show()



method = input("выбирите медод Эйлера: 1 или Рунге-Кутты: 2  ")
match method:
    case "1":
        eyler(h)
    case "2":
        runge(h)
    case _:
        print("Метод выбран неверно")


