"""Cálculo de costo de envío (versión refactorizada, orientada a datos)."""

TARIFAS = {
    "AR": {
        "standard": ((1, 500), (5, 900), (None, 1500)),
        "express": ((1, 900), (5, 1600), (None, 2500)),
    },
    "UY": {
        "standard": ((1, 700), (5, 1200), (None, 2000)),
        "express": ((1, 1200), (5, 2100), (None, 3200)),
    },
    "CL": {
        "standard": ((1, 900), (5, 1500), (None, 2400)),
        "express": ((1, 1500), (5, 2600), (None, 3900)),
    },
}
DESCUENTO_PREMIUM = 0.10


def _tramos(pais, tipo):
    if pais not in TARIFAS:
        raise ValueError("país no soportado")
    if tipo not in TARIFAS[pais]:
        raise ValueError("tipo inválido")
    return TARIFAS[pais][tipo]


def _precio_por_peso(tramos, peso):
    for limite, precio in tramos[:-1]:
        if peso <= limite:
            return precio
    return tramos[-1][1]


def calcular_envio(pais, peso, tipo, premium):
    costo = _precio_por_peso(_tramos(pais, tipo), peso)
    if premium:
        costo = costo * (1 - DESCUENTO_PREMIUM)
    return costo
