def foo(si):
    enteros_nuevo=[]
    enteros_nuevo_nuevo=[enteros_nuevo.append(si) for si in enteros if isinstance(si,int)]
    return (enteros_nuevo)
enteros=[99,"no data",95,94,"no data"]
print(foo(enteros))