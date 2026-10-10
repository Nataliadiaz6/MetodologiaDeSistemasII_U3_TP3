import pytest
from envios import calcular_envio


@pytest.mark.parametrize(
    "pais, tipo, peso, esperado",
    [
        ("AR", "standard", 0.5, 500),
        ("AR", "standard", 1, 500),  # borde: límite del primer tramo
        ("AR", "standard", 1.01, 900),
        ("AR", "standard", 5, 900),  # borde: límite del segundo tramo
        ("AR", "standard", 9, 1500),
        ("AR", "express", 0.5, 900),
        ("AR", "express", 3, 1600),
        ("AR", "express", 9, 2500),
        ("UY", "standard", 3, 1200),
        ("UY", "express", 3, 2100),
        ("CL", "standard", 3, 1500),
        ("CL", "express", 9, 3900),
    ],
)
def test_tarifa_sin_descuento(pais, tipo, peso, esperado):
    # Arrange: parámetros de la tabla
    # Act
    resultado = calcular_envio(pais, peso, tipo, premium=False)
    # Assert
    assert resultado == esperado


def test_cliente_premium_recibe_10_por_ciento():
    # Arrange + Act
    resultado = calcular_envio("UY", 9, "express", premium=True)
    # Assert
    assert resultado == pytest.approx(2880)


def test_pais_no_soportado_lanza_error():
    with pytest.raises(ValueError, match="país no soportado"):
        calcular_envio("XX", 1, "standard", premium=False)


def test_tipo_invalido_lanza_error():
    with pytest.raises(ValueError, match="tipo inválido"):
        calcular_envio("AR", 1, "drone", premium=False)
