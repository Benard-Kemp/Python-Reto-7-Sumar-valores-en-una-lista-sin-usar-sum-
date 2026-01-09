def sumar_valores(lista: list | None) -> float:
    """
    Suma valores numéricos de una lista sin usar sum().

    Reglas:
    - None -> 0
    - No list -> TypeError
    - Suma solo int y float
    - Ignora valores no numéricos
    """
    if lista is None:
        return 0

    if not isinstance(lista, list):
        raise TypeError("El parámetro 'lista' debe ser una lista o None.")

    total = 0

    for valor in lista:
        if isinstance(valor, (int, float)):
            total += valor

    return total
