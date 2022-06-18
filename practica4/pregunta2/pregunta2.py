import requests
def bitcoin():
    try:
        
        n=int(input("Ingrese el numero de bitcoins: "))
        url='https://api.coindesk.com/v1/bpi/currentprice.json'
        respuesta = requests.get(url)
        dato=respuesta.json()
        precio_dolar=dato['bpi']['USD']['rate_float']
        amount=float(precio_dolar)*n
        print(f"el costo actual de {n} bitcoins es :  {amount:,.4f}")
    except requests.RequestException:
        print("Ocurrio un error")
        bitcoin()
    except ValueError:
        print("Vuelva a intentarlo")
        bitcoin()
bitcoin()