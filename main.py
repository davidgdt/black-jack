import random
jugadorIn = True
casaIn = True
jugador = []
casa = []
baraja = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'j', 'k', 'Q', 'A',  'j', 'k', 'Q', 'A','j', 'k', 'Q', 'A', 'j', 'k', 'Q', 'A'] 

def sacarcartas (turno):
  carta = random.choice(baraja)
  turno.append(carta)
  baraja.remove(carta)

def total(turno):
  total = 0
  cara = ['j', 'k', 'Q']
  for carta in turno:
    if carta in range(1, 11):
      total += carta
    elif carta in cara:
      total += 10
    else: 
      if total> 11:
        total += 1
      else:
        total += 11
        return total

#ganador

def revelarcartadelacasa ():
  if len (casa) == 2:
    return casa[0]
  elif len(casa) > 2:
    return casa[0], casa[1]

#bucle
for _ in range(2):
  sacarcartas(jugador)
  sacarcartas(casa)
print(jugador)
print(casa)

while jugadorIn or casaIn:
  print("tu tienes {sacacartas(jugador)} and X")
  print("tu tienes{jugador} un total de {total(jugador)}")
  if jugadorIn:
    siOno = input("1: me quedo\n2: carta \n")
  if total(casa) > 17:
    casaIn = False
  else:
    sacarcartas(casa)
    if siOno == '1':
      jugadorIn = False
    else:
      sacarcartas(jugador)
    if total(jugador) >= 21:
      break
    elif total(casa) >= 21:
      break 

if total(jugador) == 21:
   print("tienes {jugador} {total(jugador)} en total y la casa {casa}tiene en total {total(casa)}")
print("blackjack")
if total(casa) == 21:
   print("tienes {jugador} {total(jugador)} en total y la casa {casa}tiene en total {total(casa)}")
   print("blackjack, gana la casa")
elif total(casa) > 21:
   print("tienes {jugador} {total(jugador)} en total y la casa {casa}tiene en total {total(casa)}")
   print("has perdido, gana la casa")
elif total(jugador) > 21:
   print("tienes {jugador} {total(jugador)} en total y la casa {casa}tiene en total {total(casa)}")
   print("pierde la casa , has ganado")
elif 21 - total(casa) < 21 - total(jugador):
    print("tienes {jugador} {total(jugador)} en total y la casa {casa}tiene en total {total(casa)}")
    print("gana la casa")
elif 21 - total(casa) > 21 - total(jugador):
   print("tienes {jugador} {total(jugador)} en total y la casa {casa}tiene en total {total(casa)}")
   print("ganas tu ")



