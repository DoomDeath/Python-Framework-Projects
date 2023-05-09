API REST básica con endpoints correspondientes a un CRUD y los requisitos fueron:

Base de datos H2.
Framework Spring boot.
Java 11.
Gradle.
Swagger.
JWT.
Pasos para correr el proyecto y realizar pruebas
Una vez clonado y corriendo es necesario abrir postman, ya que por medio de este programa se realizarán las pruebas.


Buscar todos (GET) http://localhost:8080/prueba/users
Buscar un usurio (GET) http://localhost:8080/prueba/user/{id}
Guardar usuario (POST) http://localhost:8080/prueba/create
Modificar Usuario http://localhost:8080/prueba/update/{id}
Eliminar usuario http://localhost:8080/prueba/delete/{id

estructura json 
{
    "name": "Gustavo Burgos",
    "email": "gusta@g.com2",
    "password": "Password122",
    "phones": [
        {
            "number": "1111111"
        },
        {
            "number": "2222222"
        },
        {
            "number": "33333333"
        }
    ]
}
