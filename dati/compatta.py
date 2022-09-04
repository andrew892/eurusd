import os

with open('out.csv','a')  as outfile:
    l = os.listdir('11')
    l.sort()
    for csv in l:
        with open('11/'+csv,'r') as infile:
            a = infile.readlines()
            outfile.writelines(a[1:-1])
