def leap_year(year):
    # Retorna True si es divisible por 4 y:
    # - No es divisible por 100 (year % 100 != 0 significa que el residuo no es 0, es decir, no es múltiplo de 100), o
    # - Si es divisible por 100, solo si también es divisible por 400 (year % 400 == 0 significa que el residuo es 0, es decir, es múltiplo de 400).
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
