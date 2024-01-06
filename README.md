# Selector

· Para usar el programa se debe instalar el ejecutor de archivos "serve" desde la consola de node.

- Pasos para instalar "serve"

1. Instalar Node.js
2. Ejecutar el comando "node --version" para confirmar la instalación, de lo contrario se deberá abrir una consola (preferentemente de bash) nueva para cargar los cambios.
3. Ejecutar el comando npm install --global serve
4. Pocicionarse en la carpeta "Vista" del proyecto
5. Ejecutar el programa con el comando "serve ."

· Para iniciar el Backend de la aplicación se debe tener Python instalado y seguir los siguientes pasos.

1. Pocisionarse en la carpeta "Controlador" del proyecto.
2. Instalar el entorno virtual con el siguiente comando: "python -m virtualenv venv".
3. Instalar las dependencias: {
    - Ejecuta el comando: "pip install -r requirements.txt".
}r
3.1. Expotar dependencias: {
    - Ejecuta el comando: "pip freeze > requirements.txt".
}
4. Iniciar el servidor con el siguiente comando: "pyhton setup.py".
