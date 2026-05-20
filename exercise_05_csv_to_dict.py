# Ejercicio 5 - CSV a lista de diccionarios


def csv_to_dict(filename):
    """
    Lee un archivo CSV con header "name,age,city" y retorna una lista de
    diccionarios, uno por fila.

    Reglas:
    - La primera línea es siempre el header.
    - Las claves del diccionario se toman del header.
    - El campo "age" se convierte a int. "name" y "city" quedan como str.
    - Se deben hacer strip a los valores para eliminar espacios sobrantes.
    - Si el archivo está vacío o solo tiene header, retornar [].
    - Si el archivo no existe, propagar FileNotFoundError.
    - No se permite usar el módulo csv.

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        list[dict] - lista de diccionarios por fila del CSV.

    Raises:
        FileNotFoundError: si el archivo no existe.

    Ejemplo:
        # archivo contiene:
        # name,age,city
        # Alice,30,Buenos Aires
        # Bob,25,Rosario
        csv_to_dict("people.csv") -> [
            {"name": "Alice", "age": 30, "city": "Buenos Aires"},
            {"name": "Bob", "age": 25, "city": "Rosario"},
        ]
    """
    registros = []
    with open(filename, "r", encoding="utf-8") as f:
        lineas = f.readlines()

        # Si el archivo está vacío o solo tiene header
        if len(lineas) <= 1:
            return []

        # Obtener header y claves
        header = [h.strip() for h in lineas[0].split(",")]

        # Procesar cada fila
        for linea in lineas[1:]:
            valores = [v.strip() for v in linea.split(",")]
            if not valores or len(valores) != len(header):
                continue  # ignora filas mal formateadas

            fila = {}
            for clave, valor in zip(header, valores):
                if clave == "age":
                    fila[clave] = int(valor)
                else:
                    fila[clave] = valor
            registros.append(fila)

    return registros
