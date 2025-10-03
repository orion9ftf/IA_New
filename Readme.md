## GitHub Copilot

Para el uso de GitHub Copilot se siguieron seguir los siguientes pasos:

Escoger Copilot:

![Escoger Copilot](/img/plan_copilot.png)

1.- Crear el Repositorio en Github, en este caso ya contaba con una cuenta activa en Github, esto significa que las configuraciones básicas de ssh ya se encontraba configurado.

2.- En lo personal el repositorio se creó de manera local con CLI sin interfaz gráfica, para mayor comodidad, luego se inicalizó con los siguientes comandos:

```sh
$ mkdir ia_new
$ cd ia_new
$ touch recommendation_system.py .gitignore Readme.md
$ code .
$ git init
$ git add .
$ git commit -m 'Starting the project with Github + Copilot'
$ git push origin developer
```

Ver imagen de la evidencia de los pasos a seguir:

![terminal](/img/terminal.png)

Crear Repositorio:

![Crear Repositorio](/img/crear_repositorio.png)

Repositorio Creado:

![Repositorio creado](/img/repositorio.png)

3.- Iniciar Copilot

![Iniciar Copilot](/img/iniciar_copilot.png)

4.- Crear un propmt específico:

![crear promp](/img/promp_especifico.png)

5.- Respuesta de la IA con código específico:

![codigo](/img/la_ia_responde_con_el_codigo.png)

6.- Mantener código entregado por la IA:

![mantener código](/img/mantener_codigo.png)

7.- Probar código:
![probar codigo](/img/probar_codigo.png)

```sh
$ python recommendation_system.py 
Introduce IP o URL: 127.0.0.1
```

***El código evalúa los puertos más utilizados***
