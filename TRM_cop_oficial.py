import requests
import os

def consultar_trm_oficial_2026():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("==========================================")
    print("   CONSULTA OFICIAL TRM - DATOS ABIERTOS  ")
    print("==========================================")
    
    # Esta es la URL basada en el dataset que encontraste (32sa-8pi3)
    # Pedimos que nos lo ordene por fecha para tener la más reciente arriba
    url = "https://www.datos.gov.co/resource/32sa-8pi3.json?$order=vigenciadesde DESC&$limit=1"
    
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        print("Conectando con la base de datos del Gobierno...")
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        
        datos = response.json()

        if datos:
            # En este dataset específico, las columnas suelen ser:
            # 'valor', 'vigenciadesde', 'vigenciahasta'
            item = datos[0]
            
            # Usamos .get() con mayúsculas y minúsculas por seguridad
            valor = item.get('valor') or item.get('VALOR')
            fecha = item.get('vigenciadesde') or item.get('VIGENCIADESDE')

            if valor:
                print(f"\n✅ DATOS ACTUALIZADOS:")
                print(f"💵 Valor: ${float(valor):,.2f} COP")
                print(f"📅 Vigencia desde: {fecha[:10]}")
                print("==========================================")
            else:
                print("\n❌ Se encontró el registro pero la columna no se llama 'valor'.")
                print(f"Columnas disponibles: {list(item.keys())}")
        else:
            print("\n❌ No se encontraron datos en este conjunto.")

    except Exception as e:
        print(f"\n⚠️ Error de acceso: {e}")

consultar_trm_oficial_2026()
input("\nPresione ENTER para salir...")