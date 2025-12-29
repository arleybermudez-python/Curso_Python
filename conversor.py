import requests
# 1. COnfiguracion de la API
url = "https://open.er-api.com/v6/latest/USD"
print(" CONVERSOR MULTIMONEDA")
try:
    #traemos los datos de internet
    print("Actualizando tasas de cambio...")
    respuesta = requests.get(url)
    datos = respuesta.json()
    tasas = datos['rates'] #Aqui estan todas las monedas del mundo

    while True:
        print("\nOpciones de conversión disponibles: COP, MXN, EUR, GBP, JPY")
        moneda_destino = input("¿A que moneda desea convertir? (o escribe 'salir':").upper()

        if moneda_destino == "SALIR":
            break

        if moneda_destino in tasas:
            cantidad = float(input(f"¿Cuantos dolares (USD) quieres convertir a {moneda_destino}?:"))

            tasa = tasas[moneda_destino]
            resultado = cantidad * tasa

            print(f"RESULTADO")
            print(f"{cantidad:,} USD equivalen a {resultado:,.2f} {moneda_destino}")
            print(f"Tasa del día: 1 USD = {tasa:,.2f} {moneda_destino}")
            break
        else:
            print("Esa moneda no es valida o no está en nuestra lista. Intenta de nuevo.")
except Exception as e:
    print(f"Hubo un error al conectar:{e}")
print("Gracias por usar el conversor")    
