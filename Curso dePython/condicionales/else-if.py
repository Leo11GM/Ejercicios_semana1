ingreso_mensual = 100000
gasto_mensual = 98000

#if anidado y else if (elif)

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0 :
        print("Estás en déficit")
    elif ingreso_mensual - gasto_mensual > 3000 :
        print("Estás bien")
    else:
        print("estás gastando un montón, ahorra")
        
elif ingreso_mensual > 1000:
    print("estás bien en latinoamérica") 
    
elif ingreso_mensual > 500:
    print("estás bien en Argentina")
    
elif ingreso_mensual > 200:
    print("estás bien en Venezuela")
    
else:
    print("estás jodido")       
     