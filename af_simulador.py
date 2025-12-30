# SIMULADOR DE CREDITO AUTOFINANCIERA / FONBIENES
print("---- COTIZADOR AUTOMATICO DE PLANES AUTOFINANCIERA / FONBIENES ----")
print("---- COMPARADOR DE PLANES ----")
tipo = input("El vehículo es nuevo o usado:").strip().upper()
monto = float(input("Indique valor del vehiculo (Ej. 100000000):"))

# LISTA PARA GUARDAR PLANES QUE COINCIDAN
opciones = []

# EVALUACION DE COINCIDENCIAS
# OPCIONES AUTOFINANCIERA NUEVO 90MM - 500MM
if tipo == "NUEVO" and monto >= 90000000:
    opciones.append({"nombre": "AUTOFINANCIERA (90MM - 500MM)", "plazo": 72, "admon": 0.208, "insc": 3.60})

# OPCION AUTOFINANCIERA NUEVO 65MM - 89MM
if tipo == "NUEVO" and 65000000 <= monto <= 89000000:
    opciones.append({"nombre": "AUTOFINANCIERA (65MM - 89MM)", "plazo": 90, "admon": 0.222222, "insc": 3.60})

# OPCION AUTOFINANCIERA USADO
if tipo == "NUEVO" and 65000000 <= monto <= 87000000:
    opciones.append({"nombre": "Fonbienes (Nuevo 65MM - 87MM)", "plazo": 78, "admon": 0.1923070, "insc": 3.60})

# OPCION FONBIENES USADO
if tipo == "USADO" and 47000000 <= monto <=87000000:
    opciones.append({"nombre": "Fonbienes (Usado 47MM - 87MM)", "plazo": 78, "admon": 0.2564102, "insc": 4.00})

# MOSTRAR RESULTADOS
if not opciones:
    print("No se encontraron opciones planes para este monto y tipo de vehículo")
else:
    print:(f"\nSe encontraron {len(opciones)} posibles planes para su perfil:")

    for i , plan in enumerate(opciones):
        # CALCULOS PARA CADA OPCION
        c_capital = monto / plan['plazo']
        c_admon = ((monto * (plan['admon'] / 100))*1.19)
        v_insc = ((monto * (plan['insc'] / 100))*1.19)
        total = c_capital + c_admon

        print(f"[{i+1}] {plan['nombre']}")
        print(f" - Plazo: {plan['plazo']} meses")
        print(f" - Inscripción: $ {v_insc:,.0f}")
        print(f" - Cuota Mensual: $ {total:,.2f} (Capital: ${c_capital:,.0f} + Admon: ${c_admon:,.0f})")

    seleccion = int(input("\nSeleccione el numero del plan que desea profundizar (o 0 para salir):"))
    if seleccion > 0:
        print(f"\nHa seleccionado:{opciones[seleccion-1]['nombre']}.¡EXCELENTE OPCION!")
