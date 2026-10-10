def calcular_envio(pais, peso, tipo, premium):
    costo = 0
    if pais == "AR":
        if tipo == "standard":
            if peso <= 1:
                costo = 500
            elif peso <= 5:
                costo = 900
            else:
                costo = 1500
        elif tipo == "express":
            if peso <= 1:
                costo = 900
            elif peso <= 5:
                costo = 1600
            else:
                costo = 2500
        else:
            raise ValueError("tipo inválido")
        if premium:
            costo = costo * 0.9
    elif pais == "UY":
        if tipo == "standard":
            if peso <= 1:
                costo = 700
            elif peso <= 5:
                costo = 1200
            else:
                costo = 2000
        elif tipo == "express":
            if peso <= 1:
                costo = 1200
            elif peso <= 5:
                costo = 2100
            else:
                costo = 3200
        else:
            raise ValueError("tipo inválido")
        if premium:
            costo = costo * 0.9
    elif pais == "CL":
        if tipo == "standard":
            if peso <= 1:
                costo = 900
            elif peso <= 5:
                costo = 1500
            else:
                costo = 2400
        elif tipo == "express":
            if peso <= 1:
                costo = 1500
            elif peso <= 5:
                costo = 2600
            else:
                costo = 3900
        else:
            raise ValueError("tipo inválido")
        if premium:
            costo = costo * 0.9
    else:
        raise ValueError("país no soportado")
    return costo
