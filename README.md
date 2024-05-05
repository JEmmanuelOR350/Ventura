## Guia
1.- Descomprimir<br>
2.- Apuntar VS Code a Ventura<br>
3.- Abrir Docker Desktop<br>
4.- Abrir la terminal y construir el contenedor con:<br>
	docker build -t ventura .<br>
5.- Correr la imagen usando:<br>
	docker run -p 5000:5000 -d ventura<br>
6.- Abran el navegador en localhost:5000<br>
