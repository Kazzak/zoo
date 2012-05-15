from pyswip import *

#lista para variables a unificar
R = Variable()
ED = Variable()
G = Variable()
N = Variable()
EC = Variable()
C = Variable()
variables = [R,ED,G,N,EC,C]

assertz = Functor("assertz", 1)
animal = Functor("animal", 6)


	#para hacer la consulta del insert anterior
	#X = Variable()
	#q = Query(animal(raza,edad,genero,X,ecosistema,comida))
	#while q.nextSolution():
	#	print "animal:,", X.value
	#q.closeQuery()

def insertar(raza,edad,genero,nombre,ecosistema,comida):
	#se inserta el animal
	call(assertz(animal(raza,edad,genero,nombre,ecosistema,comida)))
	#print("se inserto el animal")
	
	
def consultar(lista, res):
	#['perro', '12', Variable(19), Variable(20), 'cartago', 'queso']
	for i in range(0, len(lista)):
		if lista[i] == "":
			lista[i]= variables[i]
	matriz = []
	q = Query(animal(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5]))
	while q.nextSolution():
		sublista = []
		for i in range(0,len(res)):
			if res[i] == "":
				##print(variables[i].value)
				sublista.append(variables[i].value)
			else:
				##print(res[i])
				sublista.append(res[i])
		matriz.append(sublista)
	q.closeQuery()
	return matriz
	
	
	
	

