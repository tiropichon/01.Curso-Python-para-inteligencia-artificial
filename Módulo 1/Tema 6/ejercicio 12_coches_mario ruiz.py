lista=["A","A","A","A","A","A","A","A","A","A","A","A","B","B","B","B","A","A","A","A","A","A","B"]
word = ""
lista_dec=[]
count = 0

def recursiva(lista):
    if len(lista) == 0:
        lista_dec.append()
        lista_dec.append(count)
        return
    else:
        if lista[0] == "":
            count += 1
            lista=lista[1:]
            return recursiva(lista)
        else:
            lista_dec.append(word)
            lista_dec.append(count)
            word = lista[0]
            count = 1
            lista = lista[1:]
            return recursiva(lista)
        
lista_dec = recursiva(lista)
print(lista_dec)