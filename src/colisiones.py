def detectar_colision(rect_1,rect_2) -> bool:
    # print(punto_en_rectangulo(rect_1["rect"].topright,rect_2))
    if punto_en_rectangulo(rect_1.topright,rect_2) or \
        punto_en_rectangulo(rect_1.topleft,rect_2) or \
        punto_en_rectangulo(rect_1.bottomright,rect_2) or \
        punto_en_rectangulo(rect_1.bottomleft,rect_2) or \
        punto_en_rectangulo(rect_2.topright,rect_1) or \
        punto_en_rectangulo(rect_2.topleft,rect_1) or \
        punto_en_rectangulo(rect_2.bottomright,rect_1) or \
        punto_en_rectangulo(rect_2.bottomleft,rect_1):
        return True
    else:
        return False

def punto_en_rectangulo(punto, rect):
    x , y = punto[0], punto[1]
    return (x >= rect.left and x <= rect.right and y
                        >= rect.top and y <= rect.bottom)

def calcular_distancia_dos_puntos(pto_1: tuple [int,int], pto_2: tuple [int,int]):
    return ((pto_1[0] - pto_2[0])**2 + (pto_1[1] - pto_2[1])**2)** 0.5

def distancia_entre_puntos(pto_1: tuple [int,int], pto_2: tuple [int,int]):
    ca = pto_1[0] - pto_2[0]
    co = pto_1[1] - pto_2[1]
    distancia = (ca ** 2 + co ** 2) ** 0.5
    return distancia

def colision_circulos(rect_1:tuple, rect_2:tuple)->bool:
    r1 = rect_1.width // 2 
    r2 = rect_2.width // 2
    distancia = distancia_entre_puntos(rect_1.center ,rect_2.center)
    return distancia <= r1 + r2