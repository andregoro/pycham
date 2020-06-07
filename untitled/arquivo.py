def arquivo(arq):
    processo=[]
    with open(arq, 'r') as ent:
        for l in ent:
            processo.append(str(l.split('\n')).replace(',','').replace("'","").replace('[',"").replace("]","").replace("'",""))
            #processo.append(l[0:len(l)-1])
    #print(processo)
    return processo