from pyswip import *

assertz = Functor("assertz", 1)
animal = Functor("animal", 6)

def insertar(raza,edad,genero,nombre,ecosistema,comida):
	#se inserta el animal
	call(assertz(animal(raza,edad,genero,nombre,ecosistema,comida)))
	print("se inserto la vara")
	
	#para hacer la consulta del insert anterior
	#X = Variable()
	#q = Query(animal(raza,edad,genero,X,ecosistema,comida))
	#while q.nextSolution():
	#	print "animal:,", X.value
	#q.closeQuery()
