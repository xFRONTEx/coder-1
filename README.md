# coder-1

CODER-1-MAIN/
├── .venv/                      # Entorno virtual
├── coder-1/
│   │   ├── accounts/               # Aplicación principal / Home / Blóg de duendess
│   │   │   ├── migrations/
│   │   │   ├── templates/accounts/
│   │   │   │   └── login.html
│   │   │   │   └── password_change.html
│   │   │   │   └── profile_edit.html
│   │   │   │   └── profile.html
│   │   │   │   └── registro.html
│   │   │   ├── forms.py
│   │   │   ├── models.py
│   │   │   ├── views.py   
│   │   │   └── urls.py
│   │   │   └── views.py
│   │   │  
│   │   ├── config/             # Configuración principal del proyecto (Django)
│   │   │   ├── settings.py
│   │   │   ├── urls.py         # URLs globales
│   │   │   └── wsgi.py / asgi.py
│   │   │
│   │   ├── core/               # Aplicación principal / Home / Blóg de duendess
│   │   │   ├── migrations/
│   │   │   ├── templates/core/
│   │   │   │   └── acercade-mi.html
│   │   │   │   └── base.html
│   │   │   │   └── blog_duendes.html
│   │   │   │
│   │   │   ├── admin.py
│   │   │   ├── forms.py
│   │   │   ├── models.py
│   │   │   ├── views.py   
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   │   
│   │   ├── producto/           # Aplicación de gestión de productos
│   │   │   ├── migrations/
│   │   │   ├── templates/producto/
│   │   │   │   ├── producto_confirm_delete.html
│   │   │   │   ├── producto_crear.html
│   │   │   │   ├── producto_editar.html
│   │   │   │   └── producto_list.html
│   │   │   ├── admin.py
│   │   │   ├── models.py
│   │   │   ├── views.py
│   │   │   └── urls.py
│   │   │
│   │   ├── static/             # Archivos CSS, e Imágenes
│   │   ├── db.sqlite3          # Base de datos local
│   │   └── manage.py           # CLI de Django
│   │
│   ├── .gitignore
│   └── README.md

# Requerimientos pedidos para esta entrega final fueron los siguientes:
# Tener al menos 3 clases que heradan de modelos                                                             (Completado)✅
# Barra de busqueda                                                                                          (Completado)✅

# Contar con algún acceso visible a la vista de "Acerca de mí" donde se contará,       
# acerca del dueño de la página manejado en el route about/.                                                  (Completado)✅

# Contar con algún acceso visible a la vista de blogs que debe alojarse en el route pages/.                   (Completado)✅

# Para editar o borrar pages debes estar logueado.                                                            (Completado)✅

# Te recomendamos incluir:

# NavBar                                                                                                      (Incompleto)❌
# En vez de la implementacion del navbar quise realizar algo mas limpio con la implementacion, de un menu desplegable con su logica donde contuviera todas las rutas pages y se viera mas limpia la pagina. (Esta logica de menu desplegables esta asentada en styles.css). 

# Home                                                                                                        (Completado)✅

# About                                                                                                       (Completado)✅

# Pages                                                                                                       (Incompleto)❌
# Nose implemento la carpetas que contendria todas la pages y fue destinada al archivo base donde conviven todas las rutas. 

# Login                                                                                                       (Completado)✅

# Signup                                                                                                      (Completado)✅

# Messages                                                                                                    (Incompleto)❌
# Es a criterio del alumno y en este proyecto no fue implementado.

# Profile                                                                                                     (Completado)✅

# Logout                                                                                                      (Completado)✅

# Get pages                                                                                                   (Incompleto)❌
# El get pages en mi proyecto, serian todas las rutas que trae mi menu desplegable. 

# Get page                                                                                                    (Completado)✅

# Create page                                                                                                 (Completado)✅

# Update Page                                                                                                 (Completado)✅

# Delete page                                                                                                 (Completado)✅

# Get profile                                                                                                 (Completado)✅

# Update profile                                                                                              (Completado)✅

# No agregar la Base de datos (el archivo db.sqlite3) en la entrega. Debería estar en el .gitignore           (Completado)✅


# Exista gitignore con:

# pycache                                                                                                     (Completado)✅

# db.sqlite3                                                                                                  (Completado)✅

# media                                                                                                       (Completado)✅


# Existencia del archivo requirements.txt actualizado.                                                        (Completado)✅

# Tener en cuenta al manejar forms con imágenes hay que adaptar el template, y la vista...no solo el modelo y el formulario. (Completado)✅

# Uso de mínimo 2 clases basadas en vista.                                                                    (Completado)✅

# Uso de mínimo un mixin en una CBV y un decorador en una view común.                                         (Completado)✅

# Una vista de inicio/home.                                                                                   (Incompleto)❌
# Solo esta la vista de home en este proyecto. 

# Acceso a una vista "Acerca de mí"/"About"                                                                   (Completado)✅

# Crear un modelo principal (Blog/Post/Auto/Vendedor/Docente/etc) que contenga los siguiente campos como mínimo: 2 Charfield, 1 de texto enriquecido (usando ckeditor), 1 campo de imagen, 1 de fecha         (Models.py-producto)     (Completado)✅ 


# Vista de listado de los objetos del modelo principal (modelo a elección). En la cual cada objeto mostrará solo algunos de sus datos. (product-list)  (Completado)✅ 

# Mensaje que da aviso en caso de no haber ningún objeto creado o al utilizar el buscador no encontrar tampoco algún objeto.(Completado)✅

Desde el listado:

# poder acceder a una vista que muestre el detalle de el objeto seleccionado                         (Completado)✅


# poder acceder a una vista de creación, una de edición y una de borrado de objetos.                 (Completado)✅


# Registrar en el apartado de admin todos los modelos creados.                                       (Completado)✅

# Tener una app (accounts/cuentas/etc) para el manejo de todas las vistas relacionadas al usuario/autenticación. (Completado)✅

# Desarrollar las vistas para un login, un logout y un registro para usuarios. En este último se debe solicitar: username, email, password.                                                        (Completado)✅

# Crear una vista de perfil donde se muestran los datos del usuario:          (Completado)✅


# nombre


# apellido


# email


# avatar


# biografia/link/fecha de cumpleanios/etc.


# Desde el perfil, crear un acceso a una vista de edición de estos datos. Agregar el cambio de password.


#Cuales fueron los datos adicionales opcionales que decidi hacer por cuenta propia, y para estar encaminado, para la entrega final?.

# Se implemento las vistas basadas en clases (CBV), que son:
* ProductoListView 
* ProductoCreateView
* ProductoUpdateView 
* ProductoDeleteView
# Que permitieron hacer las vistas basadas en clases (CBV)? 
* Nos permitieron ser muchos más limpio dentro del codigo 
* No tuve que escribir como buscar un objeto o como renderizar un archivo HTML, ya que las siguientes saben hacerlo por defecto y estan albergadas en views.py dentro del archivo producto:
# (ListView, CreateView, UpdateView y DeleteView) 


# Además se implemento un crud de manera correcta para gestionar la lista de productos:
* Crear
* Editar
* Actualizar
* Eliminar


#Opté para este proyecto hacerlo que se trate de una tienda de venta de duendes en el mismo, contiene cuatro formularios:

# Agreegar   ---> Podrán aquí agregar un nuevo duende.
# Editar     ---> Aquí podran editar uno ya exsistente.
# Busqueda   ---> Aquí podran ingresar un nombre y funcionara la lupita por defecto.
# Feedback   ---> Aqui donde podran dejar sus opiniones.

Tema del Feedback: 
-Usted Esteban para que lo pueda comprobar de que funciona, debera ingresa por url en la pagina en curso, (/admin/) con permisos y son: 

# usuario: Moro
# password: DuendeMagico2026!


En cuanto algunas funcionalidades rebuscadas (Por gusto propio): 

# En el menú desplegable: Debi de aplicar en el archivo (CSS), Un checkbox que cuando esté marcado el menú se abra y así alli muestre (Lista de Productos) - (Feedback).

Dato Acotador: Cada vez que realizaba un cambio habia veces que no bastaba con guardar con un ctrl + s,  sino que tenia que ejecutar e poner a prueba en la terminal,  las migraciones para que se actualizara nuestra Base de Datos.

## Aclaración-estructura: La diferencia entre el archivo chimuelito.html y producto.
* Para acalarar nuestro archivo apodado chimuelito.html es nuestro home donde esta el inicio y está alli situado el blog muy necesario para dar una parte informativa que forma parte de la venta, mientras que en producto es donde gestionamos las mercaderias. 


## El CSS: 
-Estilo personalizado mediante el archivo `style.css` y un poco de **Bootstrap 5** para elementos interactivos como Modales antes mencionado y grillas.

## 🛠️ Tecnologías Utilizadas

* **Backend**: Python 3.13 + Django 6.0.2.
* **Frontend**: HTML5,  CSS3, JS ,  (Bootstrap 5)
* **Base de Datos**: SQLite3.


## Como Levantar el proyecto:

- python -m venv .venv

- source .venv/Scripts/activate

- cd src

- python manage.py runserver







