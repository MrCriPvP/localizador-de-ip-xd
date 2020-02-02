# -*- coding: utf-8 -*-





#*********************************************************************************
#*********************************************************************************
#*********************************************************************************
#Creado por yacel
#TeamSmashing
#No falle 3000 veces, aprendi 3000 formas de que no funciona <3
#*********************************************************************************
#*********************************************************************************
#*********************************************************************************


try:
    import argparse
    import mechanize
    from bs4 import BeautifulSoup
    import time
    print("**************")
    print("#TeamSmashing")
    print("**************")
    print("Iniciando...")
    banderas = argparse.ArgumentParser(description="Este script sirve para obtener datos sobre una ip")
    banderas.add_argument("-i","--ip",help="Esta bandera es para pasar la ip UwU")
    banderas = banderas.parse_args()

    por = mechanize.Browser()
    por.set_handle_robots(False)
    por.set_handle_equiv(False)
    por.open("https://www.cual-es-mi-ip.net/geolocalizar-ip-mapa")
    por.select_form(nr=0)
    por["direccion-ip"] = banderas.ip
    por.set_header("User-agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0")
    por.submit()
    sopa = BeautifulSoup(por.response().read(),"html5lib")

    print("Localizando ip...")
    time.sleep(2)

    print sopa.find_all("td")[0].string+": ",sopa.find_all("td")[1].string
    print sopa.find_all("td")[2].string+": ",sopa.find_all("td")[3].string
    print sopa.find_all("td")[4].string+": ",sopa.find_all("td")[5].string
    print sopa.find_all("td")[6].string+": ",sopa.find_all("td")[7].string
    print sopa.find_all("td")[8].string+": ",sopa.find_all("td")[9].string

    print("Si la lista aparece vacio porfavor revisa la ip UwU")
    print("El juan rulfo es el mejor esclavo <3")
except:
    print("Ocurrio un error porfavor revisa tu conexion o que tengas importado todo")


