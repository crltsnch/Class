import asyncio  #para escribir codigo concurrente


async def main():    #Async convierte a la función en una subrutina.
    print('Hola...')
    await asyncio.sleep(1)   #espera 1 segundo antes de imprimir el siguiente print. Imprimirá '... Mundo!' después de 1 segundo
    print('... Mundo!')

asyncio.run(main())     
main()


#El siguiente fragmento de código imprimirá «hola» después de esperar 1 segundo
# y luego imprimirá «mundo» después de esperar otros 2 segundos

import time
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    # strftime() devuelve una cadena que representa la fecha y hora especificada, formateada según la especificación dada. 
    # Como nosotros queremos la hora, usamos %X.
    print(f"Started at {time.strftime('%X')}")
    await say_after(1, 'hello')
    await say_after(2, 'world')
    print(f"Finished at {time.strftime('%X')}")

asyncio.run(main())









