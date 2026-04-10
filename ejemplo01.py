def presentar_datos(contenido):
	for fila in contenido:
		print(fila.rstrip('\n').split(';'))
		pass
	pass

def leer_datos(): 
	print("Leer y presentar datos")
	with open("informacion.txt", "r", encoding="utf-8") as info:
		contenido = info.readlines()
		presentar_datos(contenido)
		pass
	pass

if __name__ == '__main__':
	print("Iniciar proceos")
	leer_datos()