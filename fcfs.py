processes=[['p1',1,6],['p2',4,4],['p3',2,3],['p4',5,6]]
ct=[0]*len(processes)
tat=[0]*len(processes)
wt=[0]*len(processes)

for i in range(len(processes)):
    min_idx = i
    for j in range(i + 1, len(processes)):
        if processes[min_idx][1] > processes[j][1]:
            min_idx = j
    processes[i], processes[min_idx] = processes[min_idx], processes[i]

for i in range(len(processes)):
    empty=0
    if processes[i][1]>ct[i-1]:
        empty=1
    ct[i]=processes[i][2]+ct[i-1]+empty
    tat[i]=ct[i]-processes[i][1]
    wt[i]=tat[i]-processes[i][2]

print('Process','AT\t','BT\t','CT\t','TAT\t','WT\t')
for j in range(len(processes)):
    print(processes[j][0],'\t',processes[j][1],'\t',processes[j][2],'\t',ct[j],'\t',tat[j],'\t',wt[j],'\n')

print('TAT:',sum(tat)/len(processes))
print('WT:',sum(wt)/len(processes))