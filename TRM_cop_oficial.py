import requests
import os

def consultar_precio_dolar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("==========================================")
    print("   CONSULTOR DE PRECIO DÓLAR (ESTABLE)    ")
    print("==========================================")
    
    # Esta URL no necesita API Key
    url = "https://open.er-api.com/v6/latest/USD"

    try:
        print("Obteniendo datos del mercado financiero...")
        response = requests.get(url, timeout=10)
        
        # Si hay un error de conexión, esto lo atrapará
        response.raise_for_status()
        
        datos = response.json()

        # En esta API, el precio de Colombia está en ['rates']['COP']
        tasa_cop = datos['rates']['COP']
        actualizacion = datos['time_last_update_utc']

        print(f"\n✅ DATOS OBTENIDOS CORRECTAMENTE")
        print(f"💵 1 Dólar (USD) = {tasa_cop:,.2f} Pesos (COP)")
        print(f"📅 Actualizado: {actualizacion[:16]}")
        print("==========================================")

    except Exception as e:
        print(f"\n❌ Error al conectar: {e}")
        print("Consejo: Revisa que tu firewall no esté bloqueando a Python.")

consultar_precio_dolar()
input("\nPresione ENTER para salir...")