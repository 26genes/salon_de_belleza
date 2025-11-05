# Proyecto Salon de belleza

Los pasos mencionados en este README se recomienda que se realicen en la terminal de tu editor de código preferido, como Visual Studio Code, para una experiencia más fluida y eficiente.

###### 1. Crear un entorno virtual, hay muchas formas

    Opción 1: Crear un entorno virtual con el paquete que ya viene por defecto en las ultimas versiones de Python
    python -m venv env 

###### 2. Activar ambiente virtual

    . env/Script/activate #Activar ambiente desde Windows
    . env/bin/activate  #Activar desde la Mac

###### 3. Instalar las dependencia del archivo requirements.txt

    pip install -r requirements.txt

###### 4. Ejecutar las migraciones de la base de datos

    python manage.py migrate

###### 5. Corriendo el proyecto

    python3 manage.py runserver # Corriendo el proyecto

    Si quieres tener otro cliente ejecutalo de esta forma:
    python3 manage.py runserver 8500 #Corriendo el proyecto en un puerto diferente

