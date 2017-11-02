import csv

ids=[]

with open('taxon_list.txt','r') as f:
    for x in f:
        ids.append(x.strip().split('\t'))
print(ids)