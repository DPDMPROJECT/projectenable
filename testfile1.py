import time

t1 = time.time()

for n in range(1,1100):
    print ('Value:',n)
    n = n /10
    print ('Value', n)

t2 = time.time()

print (t2-t1)