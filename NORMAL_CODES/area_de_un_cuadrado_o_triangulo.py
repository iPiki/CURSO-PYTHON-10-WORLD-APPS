def area(base_y_altura):
    if len(base_y_altura)==1:
        area_cuadrado=base_y_altura[0]*base_y_altura[0]
        return area_cuadrado
    elif len(base_y_altura)==2:
        area_triangulo=(base_y_altura[0]*base_y_altura[1])/2    
        return area_triangulo
    else: len(base_y_altura)>2
    return "NO ES NI UN TRIANGULO NI UN CUADRADO"

valores= [5]
print(area(valores))