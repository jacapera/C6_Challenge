def es_primo(num):
    """
    Determina si un número es primo.

    Args:
        num: Un número entero

    Returns:
        bool: True si el número es primo, False en caso contrario

    Raises:
        TypeError: Si el argumento no es un entero
    """
    # Verificar que el input sea un entero
    if isinstance(num, bool):
        raise TypeError("El argumento debe ser un número entero")

    if not isinstance(num, int):
        # Permitir float que son enteros exactos o muy cercanos a enteros
        if isinstance(num, float):
            # Verificar si es un número como 19.000000000000004
            if abs(num - round(num)) < 1e-10:
                num = int(round(num))
            else:
                raise TypeError("El argumento debe ser un número entero")
        else:
            raise TypeError("El argumento debe ser un número entero")

    # 1 no es primo por definición
    if num <= 1:
        return False
    # 2 es primo
    if num == 2:
        return True
    # Verificar divisibilidad desde 2 hasta la raíz cuadrada de num
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    print(es_primo(5))
