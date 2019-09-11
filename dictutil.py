# Copyright 2013 Philip N. Klein
def dict2list(a,b): return [a[x] for x in b]

def list2dict(listA,listB): return{a:b for (a,b) in zip(listA,listB)}

#listrange2dict
#input a list L
#output a dictionary that, for i =0,1,2,...,len(L)-1, maps i to L[i]
def listrange2dict(L): return list2dict(L,range(len(L)))
