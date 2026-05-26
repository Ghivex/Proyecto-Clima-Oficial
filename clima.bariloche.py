# clima de Bariloche

clima = {
    "viernes": {"max": 10, "min": -1, "estado": "Nublado"},
    "sabado": {"max": 10, "min": 2, "estado": "Nublado"},
    "domingo": {"max": 12, "min": 3, "estado": "Fresco y nublado"},
    "lunes": {"max": 11, "min": 1, "estado": "Cielo cubierto"},
    "martes": {"max": 8, "min": 4, "estado": "Muy nublado"},
    "miercoles": {"max": 8, "min": 5, "estado": "Nuboso"},
    "jueves": {"max": 9, "min": 3, "estado": "Parcialmente nublado"}
}

# Solicitar día al usuario
dia = input("Ingrese un día de la semana: ").lower()

# Mostrar datos climáticos
if dia in clima:
    print("\nClima en Bariloche")
    print("Día:", dia.capitalize())
    print("Temperatura máxima:", clima[dia]["max"], "°C")
    print("Temperatura mínima:", clima[dia]["min"], "°C")
    print("Estado:", clima[dia]["estado"])
else:
    print("Día no válido.")