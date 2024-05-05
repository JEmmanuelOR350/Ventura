## Guia
1.- Descomprimir
2.- Apuntar VS Code a Ventura
3.- Abrir Docker Desktop
4.- Abrir la terminal y construir el contenedor con:
	docker build -t ventura .
5.- Correr la imagen usando:
	docker run -p 5000:5000 -d ventura
6.- Abran el navegador en localhost:5000
