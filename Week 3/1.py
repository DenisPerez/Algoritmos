def intercambio(m):
    cantidad_monedas = 0
    
    while(m != 0):
        if (m / 10 >= 1):
            #Se puede tomar alguna cantidad de monedas de 10 para dar el cambio
            monedas_diez = m // 10
            cambio_diez = 10 * monedas_diez
            cantidad_monedas = cantidad_monedas + monedas_diez
            m = m - cambio_diez
        elif (m/5 >= 1):
            #se puede tomar alguna cantida de monedas de 5 para dar el cambio
            monedas_cinco = m // 5
            cambio_cinco = 5 * monedas_cinco
            cantidad_monedas = cantidad_monedas + monedas_cinco
            m = m - cambio_cinco
        elif (m / 1 >= 1 ):
            #cantidad de monedas de 1 a tomar
            monedas_uno  =  m
            cambio_uno = m 
            cantidad_monedas = cantidad_monedas + m
            m = m - cambio_uno

    return cantidad_monedas

    
if __name__ == '__main__':
    m = int(input())
    print(intercambio(m))