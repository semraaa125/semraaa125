THIRTY_PERCENTAGE_SALARY = 0.3
LIHVA_PROCENT=0.125


salary=input("vavedete zaplatata na klineta: ")
suma=input("vavedete sumata na kredita: ")
srok_v_meseci=input("vuvedete mesecite: ")

salary=float(salary)
suma=float(suma)
srok_v_meseci=int(srok_v_meseci)


vnoska=suma/srok_v_meseci

lihva_vnoska = vnoska*LIHVA_PROCENT
vnoska=vnoska+lihva_vnoska


ostatak_ot_zaplatata = salary*THIRTY_PERCENTAGE_SALARY


if ostatak_ot_zaplatata > vnoska:
    print("kredita e pozvolen")
    total = vnoska*srok_v_meseci
    print("Mesechna Vnoska", vnoska)
    print("obshta suma ", total)
else:
    print("kredita ne e pozvolen")
