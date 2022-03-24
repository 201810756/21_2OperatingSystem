"""
@author : 201810756 kimdaehwan
@date : 2021.11
@description : process scheduling by FCFS, RR, SJF, Priority

"""

import pandas as pd

p1=pd.read_csv('./process1.csv')
p2=pd.read_csv('./process2.csv')
p3=pd.read_csv('./process3.csv')
p4=pd.read_csv('./process4.csv')
p5=pd.read_csv('./process5.csv')

# average waiting time function
def average_waiting(wait):
    sum=0
    for i in wait:
        sum+=i
    return sum/len(wait)
# First Come First Served scheduling
def fcfs(processset):
    process=processset.sort_values('Order',ascending=True)
    burst=[0]*len(process)
    wait=[0]*len(process)
    fin=[0]*len(process)
    for k in process.index:
        burst[k]=process.loc[k]['Time']
    for i in process.index:
        fin[i]=1
        for j in process.index:
            if fin[j]!=1:
                wait[j]+=burst[i]
    for i in range(len(wait)):
        print(process.loc[i]['Process'],'waiting time(by FCFS) : ', wait[i])
    print('FCFS scheduling average waiting time : ',average_waiting(wait))


# Shortest job first scheduling
def sjf(processset):
    process=processset.sort_values(['Time','Order'],ascending=[True,True])
    burst = [0] * len(process)
    wait = [0] * len(process)
    fin = [0] * len(process)
    for k in process.index:
        burst[k]=process.loc[k]['Time']
    for i in process.index:
        fin[i] = 1
        for j in process.index:
            if fin[j] != 1:
                wait[j] += burst[i]
    for i in range(len(wait)):
        print(process.loc[i]['Process'], 'waiting time(by SJF) : ', wait[i])
    print('SJF scheduling average waiting time : ', average_waiting(wait))

# Round Robing scheduling
def check_remain(remain):
    for i in range(len(remain)):
        if remain[i]!=0:
            return True
    return False
def round_robin(processset,quantum):
    process = processset.sort_values('Order', ascending=True)  
    burst=[0]*len(process)
    wait = [0] * len(process)
    fin = [0] * len(process)
    remain = [1] * len(process)
    for k in process.index:
        burst[k]=process.loc[k]['Time']
    d=1
    while check_remain(remain):
        for i in process.index:
            d+=1
            if fin[i]!=1:
                if burst[i]<=quantum:
                    remain[i]=0
                    fin[i]=1
                    for j in process.index:
                        if fin[j] != 1:
                            wait[j] += burst[i]
                else:
                    remain[i]=d
                    for j in process.index:
                        if remain[j]!=remain[i] and fin[j]!=1:
                            wait[j] += quantum
                    burst[i] = burst[i] - quantum
    for i in range(len(wait)):
        print(process.loc[i]['Process'],'waiting time(by Round Robin) : ', wait[i])
    print('Round Robing shceduling average waiting time : ',average_waiting(wait))

# Priority Scheduling
def priority(processset):
    process=processset.sort_values(['Priority','Order'],ascending=[True,True])
    #process=processset.sort_values(['Priority',Order'],ascending=[False,True])
    burst = [0] * len(process)
    wait = [0] * len(process)
    fin = [0] * len(process)
    for k in process.index:
        burst[k]=process.loc[k]['Time']
    for i in process.index:
        fin[i] = 1
        for j in process.index:
            if fin[j] != 1:
                wait[j] += burst[i]
    for i in range(len(wait)):
        print(process.loc[i]['Process'], 'waiting time(by Priority) : ', wait[i])
    print('Priority scheduling average waiting time : ', average_waiting(wait))

round_robin(p3,15)
round_robin(p3,5)
"""
print('--------FCFS scheduling----------')
print('check process set 1')
fcfs(p1)
print('check process set 2')
fcfs(p2)
print('check process set 3')
fcfs(p3)
print('check process set 4')
fcfs(p4)
print('check process set 5')
fcfs(p5)
print('---------------------------------')
print('--------Round Robin scheduling----------')
print('check process set 1')
round_robin(p1,10)
print('check process set 2')
round_robin(p2,5)
print('check process set 3')
round_robin(p3,15)
print('check process set 4')
round_robin(p4,18)
print('check process set 5')
round_robin(p5,6)
print('----------------------------------------')
print('--------SJF scheduling----------')
print('check process set 1')
sjf(p1)
print('check process set 2')
sjf(p2)
print('check process set 3')
sjf(p3)
print('check process set 4')
sjf(p4)
print('check process set 5')
sjf(p5)
print('---------------------------------')
print('--------Priority scheduling----------')
print('check process set 1')
priority(p1)
print('check process set 2')
priority(p2)
print('check process set 3')
priority(p3)
print('check process set 4')
priority(p4)
print('check process set 5')
priority(p5)
"""