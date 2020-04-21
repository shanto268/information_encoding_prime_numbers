import numpy as np
import math 
import matplotlib.pyplot as plt

def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac
		
def factorCounter(primes):
    return len(primes)

def infocontained(num):
    info = []
    for i in range(num):
        info.append(factorCounter(primes(i)))
    return info

def createPlots(num,info):
    plt.plot([i for i in range(num)],info)
    plt.ylabel("Number of prime factors for each number")
    plt.xlabel("Number")
    plt.title("Total Numbers: "+str(num))
    plt.grid()
    plt.show()

def showPlots(numlist,infos,j,fig):
    plt.plot([i for i in range(numlist[j])],infos[j])
    plt.title(str(numlist[j]) + " Numbers")
    plt.grid()

#main
numlist = [10,100,1000,10000,100000,1000000]
infos = []

for i in numlist:
    num = i
    info = infocontained(num)
    infos.append(info)
 #   createPlots(num,info)


fig = plt.figure()
fig.subplots_adjust(hspace=0.4, wspace=0.4)

for i in range(1, 7):
    ax = fig.add_subplot(2, 3, i)
    showPlots(numlist,infos,i-1,fig)
    num = "{:.0e}".format(numlist[i-1])
    ax.set_title(str(num)+" numbers", pad=4)

plt.suptitle("Information contanined in natural numbers", size=14, y=1.05)

   # plt.text(0.5, 0.5, str((2, 3, i)), ha='center')
    
"""


"""