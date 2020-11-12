# Talana Challenge

Este proyecto hace parte del Challenge propuesto por Talana como parte del proceso de selección como backend developer

## Ejecución

Ejecutar la configuracion en el archivo 'docker-compose.yml' con el comando
```
docker-compose up
```
Una vez se encuentren corriendo los contenedores, realizar las migraciones a la base de datos ejecutando los siguientes comandos en otra consola

```
$ docker-compose exec raffle_api bash
$ ./manage.py makemigrations
$ ./manage.py migrate
```
## Endpoint
Para crear un nuevo usuario enviar una peticion tipo **HTTP POST** a la URI ```/api/v1/usuario/``` con el siguiente JSON en el cuerpo
```
{
    "email": "{{email}}",
    "first_name": "{{primer_nombre}}",
    "last_name": "{{apellido}}",
    "phone_number": "{{numero_telefono}}"
}
```
El registro de un nuevo usuario ejecutará la tarea del envío de correo de confirmación al usuario mediante celery, dejando la configuración de la contraseña del usuario una vez se haya confirmado la cuenta. Como respuesta a esta peticion, el servidor entregara el siguiente JSON
```
{
    "id": 42,
    "last_login": null,
    "is_superuser": false,
    "first_name": "{{primer_nombre}}",
    "last_name": "{{apellido}}",
    "is_staff": false,
    "is_active": false,
    "date_joined": "2020-11-12T05:25:55.028463Z",
    "password": null,
    "email": "{{email}}",
    "phone_number": "{{numero_telefono}}",
    "groups": [],
    "user_permissions": []
}
```