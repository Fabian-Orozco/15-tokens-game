import random

def mostrarInstrucciones():
	print('\nDescripción:')
	print('El juego 15 en fichas consiste en una banda numérica que va de 1 a 9 donde cada jugador dispone de 3 fichas, el usuario deberá poner sus fichas de manera inteligente para que la suma de sus fichas sea exactamente 15, deberá también considerar que la computadora(su rival) juega de manera estratégica por lo que debe predecir sus posibles movimientos y prevenir que ella gane y por ende, él pierda.') 
	print('\nObjetivo:')
	print('El ganador será el que la suma de sus fichas sea 15, ni más, ni menos.') 
	print('\nReglas:')
	print('1. Cada jugador debe mover una ficha cada turno, es decir, no puede saltar su turno.\n2. Los jugadores podrán mover la posición de una ficha solamente si tiene las 3 en la cinta numérica.') 
	print('\nControles:')
	print('El juego se controla simplemente con números y algunos caracteres que darán opciones, los pasos y posibilidades los otorga el juego conforme avance.\n1. Para ver de nuevo las instrucciones presiona la tecla [i]. \n2. Para salir del juego presiona la tecla [q].\n\n')

def mostrarTablero(tablero):
	print(" ___ ___ ___ ___ ___ ___ ___ ___ ___")
	print("| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |")
	mensaje = ''
	for i in range(0,9):
		mensaje += "|_"
		if tablero[i] != '':
			mensaje += tablero[i] + '_'
		else: 
			mensaje += "__"
	mensaje += "|"
	print(mensaje)
	

def calcularCasosFavorables(jugador,tablero,turno): #jugador en esta función puede ser el usuario o la computadora
	posicionesOcupadasJugador = []
	casosFavorables = [] 
	#Los indices pares de casosFavorables son las posiciones ocupadas de las que se quiere salir, mientras que los impares son a las que se quiere llegar. 
	#Si está en la fase de poner las primeras fichas, el indice 0 tendrá la ficha ganadora.
	#Si "jugador" no ha colocado todas sus fichas, tanto los indices pares como impares indican en dónde se puede colocar la última ficha para ganar.
	sumaFichas = 0
	for i in range(0,9):
		if tablero[i] == jugador:
			sumaFichas += i+1
			posicionesOcupadasJugador.append(i+1)
	distanciaDeVictoria = 15 - sumaFichas
	if distanciaDeVictoria < 9 and distanciaDeVictoria > -9 and distanciaDeVictoria != 0:
		if len(posicionesOcupadasJugador) > 2: #"jugador" ya colocó todas sus fichas
			for i in range(0,3):
				if posicionesOcupadasJugador[i] + distanciaDeVictoria <= 9 and posicionesOcupadasJugador[i] + distanciaDeVictoria >= -9: #jugador tiene potencial para ganar					
					if tablero[posicionesOcupadasJugador[i]+distanciaDeVictoria-1] == '' and posicionesOcupadasJugador[i]+distanciaDeVictoria != 0:
						casosFavorables.append(posicionesOcupadasJugador[i]) #indica el origen
						casosFavorables.append(posicionesOcupadasJugador[i]+distanciaDeVictoria)#indica el destino
		elif len(posicionesOcupadasJugador) == 2: #"jugador" no ha colocado todas sus fichas
			if distanciaDeVictoria <= 9 and tablero[distanciaDeVictoria-1] == '':
					casosFavorables.append(distanciaDeVictoria)
	return casosFavorables


def colocarFichasIniciales(turnoActual,primerTurno,tablero):
	if (primerTurno == 1 and turnoActual%2 != 0) or (primerTurno == 2 and turnoActual%2 == 0): #Pone el usuario
		valido = 0
		while valido == 0:
			mostrarTablero(tablero)
			eleccion = input("Escriba el numero del espacio en el que quiere poner su ficha: ")
			try:
				if eleccion.lower() == 'q':
					return 1
				elif eleccion.lower() == 'i':
					mostrarInstrucciones()
				elif int(eleccion) in range(1,10):
					destinoFicha = int(eleccion)
					if tablero[destinoFicha-1] == '':
						tablero[destinoFicha-1] = 'u'
						valido = 1;
					else:
						print("Ese espacio esta ocupado, pruebe de nuevo.")
				else:
					print("Comando no reconocido, pruebe de nuevo")
			except:
				print("Comando no reconocido, pruebe de nuevo")
	else: #Pone la computadora
		if calcularCasosFavorables('c',tablero,turnoActual):
			victoriaAsegurada = calcularCasosFavorables('c',tablero,turnoActual)
			tablero[victoriaAsegurada[0]-1] = 'c'
			print("La computadora pone en ", victoriaAsegurada[0])
		elif calcularCasosFavorables('u',tablero,turnoActual):
			evitarDerrota = calcularCasosFavorables('u',tablero,turnoActual)
			for i in range(0,len(evitarDerrota)):
				if tablero[evitarDerrota[i]-1] == '':
					tablero[evitarDerrota[i]-1] = 'c'
					print("La computadora pone en ", evitarDerrota[i])
					break
		else:
			fichaPuesta = False
			while fichaPuesta == False:
				if turnoActual <= 2:
					destinoFicha = random.randint(7,9)
				else:
					destinoFicha = random.randint(1,4)
				if tablero[destinoFicha-1] == '':
					tablero[destinoFicha-1] = 'c'
					print("La computadora pone en", destinoFicha)
					fichaPuesta = True
	return 0

def moverFichas(turnoActual,primerTurno,tablero):
	if (primerTurno == 1 and turnoActual%2 != 0) or (primerTurno == 2 and turnoActual%2 == 0): #Mueve el usuario
		valido = 0
		while valido == 0:
			mostrarTablero(tablero)
			eleccion = input("Escriba el numero del espacio del cual quiere mover su ficha: ")
			try:
				if eleccion.lower() == 'q':
					return 1
				elif eleccion.lower() == 'i':
					mostrarInstrucciones()
				elif int(eleccion) in range(1,10):
					origenFicha = int(eleccion)
					if tablero[origenFicha-1] == 'u':
						valido = 1
					else:
						print("No hay fichas del jugador en ese espacio, intente de nuevo")
				else:
					print("Comando no reconocido, pruebe de nuevo")
			except:
				print("Comando no reconocido, pruebe de nuevo")
		valido = 0
		while valido == 0:
			mostrarTablero(tablero)
			eleccion = input("Escriba el numero del espacio al cual quiere mover su ficha: ")
			try:	
				if eleccion.lower() == 'q':
					return 1
				elif eleccion.lower() == 'i':
					mostrarInstrucciones()
				elif int(eleccion) in range(1,10):
					destinoFicha = int(eleccion)
					if tablero[destinoFicha-1] == '':
						tablero[origenFicha-1] = ''
						tablero[destinoFicha-1] = 'u'
						valido = 1
					else:
						print("Ese espacio está ocupado, pruebe de nuevo")
				else:
					print("Comando no reconocido, pruebe de nuevo")
			except:
				print("Comando no reconocido, pruebe de nuevo")
	else: 
		#Mueve la computadora
		if calcularCasosFavorables('c',tablero,turnoActual): #Si la computadora puede ganar este turno
			victoriaAsegurada = calcularCasosFavorables('c',tablero,turnoActual)
			print("La computadora mueve de",victoriaAsegurada[0]," a ",victoriaAsegurada[1])
			tablero[victoriaAsegurada[0]-1] = ''
			tablero[victoriaAsegurada[1]-1] = 'c'
		elif calcularCasosFavorables('u',tablero,turnoActual): #Para bloquear victorias en un movimiento del jugador
			evitarDerrota = calcularCasosFavorables('u',tablero,turnoActual)
			destino = evitarDerrota[1]
			candidatosOrigen = []
			for i in range(0,9):
				if tablero[i] == 'c':
					candidatosOrigen.append(i+1)
			origen = candidatosOrigen[random.randint(0,2)]
			print("La computadora mueve de", origen , " a ", destino)
			tablero[origen-1] = ''
			tablero[destino-1] = 'c'
		else: #Si no existen victorias en un solo movimiento, hace el primer movimiento que ve que la acerca a la victoria. Aquí es donde hay más jugadas subóptimas
			espaciosOcupadosComputadora = []
			for i in range(0,len(tablero)):
				sumaPuntosCompu = 0
				if tablero[i] == 'c':
					espaciosOcupadosComputadora.append(i+1)
					sumaPuntosCompu += i+1
			fichaMovida = 0
			imposibleMoverDerecha = False
			while fichaMovida == 0:
				for espacioOcupadoComputadora in range(0,3):
					if sumaPuntosCompu > 15 or imposibleMoverDerecha: # si se pasa de 15 intenta mover una de sus fichas a la izquierda
						for espacioEvaluado in range(0, espaciosOcupadosComputadora[espacioOcupadoComputadora]):
							if tablero[espacioEvaluado] == '':
								tablero[espaciosOcupadosComputadora[espacioOcupadoComputadora]-1] = ''
								tablero[espacioEvaluado] = 'c'
								print("La computadora mueve de ", espaciosOcupadosComputadora[espacioOcupadoComputadora], " a ", espacioEvaluado+1)
								fichaMovida = 1
								break
					else:
						for espacioEvaluado in range(espaciosOcupadosComputadora[espacioOcupadoComputadora], 10):
							if tablero[espacioEvaluado] == '':
								tablero[espaciosOcupadosComputadora[espacioOcupadoComputadora]-1] = ''
								tablero[espacioEvaluado] = 'c'
								fichaMovida = 1
								print("La computadora mueve de ", espaciosOcupadosComputadora[espacioOcupadoComputadora], " a ", espacioEvaluado+1)
								break
						imposibleMoverDerecha = True
	return 0

def pusoTodasSusFichas(jugador, tablero): #Comprueba que un posible ganador ya colocó sus tres fichas
	fichasPuestas = 0
	for i in range(0,9):
		if tablero[i] == jugador:
			fichasPuestas += 1
	if fichasPuestas == 3:
		return True
	else:
		return False
	

def comprobarVictoria(tablero,turnoActual):
	ganador = 0
	if turnoActual > 5:
		sumaPuntosUsuario = 0
		sumaPuntosComputadora = 0
		for i in range(0,9):
			if tablero[i] == 'u':
				sumaPuntosUsuario += i+1
			elif tablero[i] == 'c':
				sumaPuntosComputadora += i+1 
		if sumaPuntosUsuario == 15 and pusoTodasSusFichas('u',tablero):
			ganador = 1
		elif sumaPuntosComputadora == 15 and pusoTodasSusFichas('c',tablero):
			ganador = 2
	return ganador

print("Bienvenido a 15 en fichas.")
mensajeBienvenida = "1. Jugar"
mensajeBienvenida += "\n2. Ver Instrucciones"
mensajeBienvenida += "\n3. Salir "
mensajeBienvenida += "\nElección: "
vecesJugadas = 0
victoriasUsuario = 0
victoriasComputadora = 0
salir = 0
while salir != 1:
	if vecesJugadas > 0 and mostrarVictorias == True:
		print("Victorias:")
		print("Usuario: ", victoriasUsuario)
		print("Computadora: ", victoriasComputadora, "\n")
	opcionValida = False
	while opcionValida == False:
		try:
			eleccionMenu = int(input(mensajeBienvenida))
			opcionValida = True
			mostrarVictorias = True
		except:
			print("\nOpción inválida, pruebe de nuevo\n")
			mostrarVictorias = False
	turnoActual = 1	
	if eleccionMenu == 1:
		primerTurno = 0
		while primerTurno not in range(1,3):		
			primerTurno = input("\nEscriba 1 para ir de primero o 2 para ir de segundo: ")
			try:
				if int(primerTurno) not in range(1,3):
					print("\nOpción inválida, pruebe de nuevo")
				else:
					primerTurno=int(primerTurno)
			except:
				print("\nOpción inválida, pruebe de nuevo")
		tablero = ['','','','','','','','','','']
		juegoTerminado = 0
		while juegoTerminado == 0:
			if turnoActual % 4 == 0 or turnoActual==1:
				print("\nRecuerde que puede escribir q en cualquier momento para salir o i para volver a ver las instrucciones")
			print("\nTurno: ",turnoActual)
			if turnoActual <= 6:
				juegoTerminado = colocarFichasIniciales(turnoActual,primerTurno,tablero)
				turnoActual += 1
			else:
				juegoTerminado = moverFichas(turnoActual,primerTurno,tablero)
				turnoActual+=1
			if comprobarVictoria(tablero,turnoActual) != 0:
				mostrarTablero(tablero)
				if comprobarVictoria(tablero,turnoActual) == 1:
					print("Gana el usuario")
					victoriasUsuario += 1
				else:
					print("Gana la computadora")
					victoriasComputadora += 1
				vecesJugadas += 1
				juegoTerminado = 1
	elif eleccionMenu == 2:
		mostrarInstrucciones()
	elif eleccionMenu == 3:
		salir = 1
	else:
		print("\nOpción inválida, pruebe de nuevo\n")

