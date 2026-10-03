# Restaurante App 3.0
Nombre: Arely Betzabe Poalasin Shiguango

Aplicación de escritorio para la gestión básica de un restaurante, desarrollada en **Python** utilizando **Tkinter** para la interfaz gráfica y archivos **JSON** para la persistencia de datos.

El proyecto integra conceptos de programación orientada a objetos, separación por capas, manejo de eventos, componentes gráficos, validación de datos y operaciones CRUD para productos y usuarios.

## 1. Descripción del proyecto

**Restaurante App** permite administrar información básica de un restaurante mediante una interfaz gráfica sencilla e intuitiva.

La aplicación cuenta con:

- Inicio de sesión.
- Gestión de usuarios.
- Gestión de productos.
- Registro de ventas.
- Persistencia de información mediante archivos JSON.
- Interfaz gráfica desarrollada con Tkinter.
- Uso de eventos del mouse, teclado y selección.
- Validación de datos en la capa de servicios.
- Separación entre modelos, servicios e interfaz.

El proyecto fue desarrollado de forma progresiva, adaptando los conceptos aprendidos durante las diferentes semanas del curso hasta obtener una aplicación funcional.

---

## 2. Objetivo

Desarrollar una aplicación de escritorio para la administración básica de un restaurante, aplicando los principios de programación orientada a objetos y el desarrollo de interfaces gráficas con Tkinter.

Además, se busca implementar una estructura organizada que permita separar la lógica de negocio de la interfaz y mantener los datos almacenados de forma persistente mediante archivos JSON.

---

## 3. Tecnologías utilizadas

- **Python 3**
- **Tkinter**
- **JSON**
- **Pathlib**
- **Programación Orientada a Objetos**
- **Git y GitHub**
- **Visual Studio Code**

---

## 4. Arquitectura del proyecto

El proyecto está organizado en diferentes carpetas para separar las responsabilidades de cada parte de la aplicación.

```text
Restaurante_app__2.7/
│
├── assets/
│   ├── logo/
│   │   ├── logo.png
│   │   └── icono.png
│   │
│   └── icons/
│       ├── home.png
│       ├── users.png
│       ├── products.png
│       ├── sales.png
│       ├── logout.png
│       ├── add.png
│       ├── search.png
│       ├── edit.png
│       ├── delete.png
│       └── clean.png
│
├── datos/
│   ├── usuarios.json
│   ├── productos.json
│   └── ventas.json
│
├── modelos/
│   ├── usuario.py
│   ├── producto.py
│   └── venta.py
│
├── servicios/
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── login_view.py
│   └── main_view.py
│
└── main.py
```

---

## 5. Descripción de las carpetas

### `modelos/`

Contiene las clases que representan las entidades principales del sistema.

#### `usuario.py`

Define la clase `Usuario`.

Un usuario contiene:

- Identificador.
- Nombre.
- Nombre de usuario.
- Contraseña.
- Rol.

Los roles utilizados son:

- Administrador.
- Empleado.
- Cliente.

También se realizan validaciones para evitar valores vacíos y roles que no estén permitidos.

#### `producto.py`

Define la clase `Producto`.

Cada producto contiene:

- Código.
- Nombre.
- Precio.
- Categoría.

La clase valida que los datos obligatorios estén completos y que el precio sea un valor numérico válido.

#### `venta.py`

Define la clase `Venta`.

Una venta contiene:

- Identificador.
- Usuario que realiza la venta.
- Producto seleccionado.
- Fecha.

---

## 6. Carpeta `servicios/`

Esta carpeta contiene la lógica principal de la aplicación.

### `archivo_servicio.py`

Se encarga de trabajar con los archivos JSON.

Sus principales funciones son:

- Leer archivos JSON.
- Crear la carpeta de datos cuando sea necesario.
- Guardar información en archivos JSON.
- Mantener la persistencia de los datos.

De esta manera, la interfaz gráfica no necesita encargarse directamente de abrir o modificar archivos.

### `restaurante_servicio.py`

Contiene la lógica de negocio del restaurante.

Entre sus responsabilidades se encuentran:

- Cargar usuarios, productos y ventas.
- Validar el inicio de sesión.
- Registrar usuarios.
- Buscar usuarios.
- Actualizar usuarios.
- Eliminar usuarios.
- Registrar productos.
- Buscar productos.
- Actualizar productos.
- Eliminar productos.
- Registrar ventas.
- Guardar los cambios en archivos JSON.

La lógica de validación se mantiene principalmente en esta capa para evitar colocar reglas de negocio directamente dentro de la interfaz.

---

## 7. Carpeta `ui/`

Contiene las interfaces gráficas desarrolladas con Tkinter.

### `login_view.py`

Representa la pantalla de inicio de sesión.

El usuario debe ingresar:

- Usuario.
- Contraseña.

La información ingresada se envía al `RestauranteServicio`, que comprueba si las credenciales son correctas.

Si el acceso es válido, se muestra la interfaz principal.

### `main_view.py`

Es la ventana principal de la aplicación.

Incluye un menú lateral con las diferentes opciones:

- Inicio.
- Usuarios.
- Productos.
- Ventas.
- Cerrar sesión.

La opción **Usuarios** se muestra para el usuario con rol de Administrador.

En esta vista se implementan los formularios, botones, tablas `Treeview`, `Combobox` y diferentes eventos de Tkinter.

---

## 8. Archivo `main.py`

Es el punto de entrada de la aplicación.

Se encarga de:

1. Crear la ventana principal.
2. Configurar el tamaño de la ventana.
3. Cargar el icono de la aplicación.
4. Crear `ArchivoServicio`.
5. Crear `RestauranteServicio`.
6. Mostrar la pantalla de inicio de sesión.
7. Cambiar entre las diferentes vistas.
8. Ejecutar el ciclo principal de Tkinter.

Para iniciar la aplicación se utiliza:

```bash
python main.py
```

---

## 9. Inicio de sesión

La aplicación comienza mostrando una pantalla de autenticación.

Para realizar una prueba inicial se puede utilizar:

```text
Usuario: admin
Contraseña: 1234
```

El usuario administrador puede acceder a la gestión de usuarios, productos y ventas.

El inicio de sesión se realiza mediante el método:

```python
validar_acceso()
```

del `RestauranteServicio`.

---

## 10. Gestión de usuarios

La sección de usuarios permite realizar operaciones CRUD.

CRUD significa:

- **Create:** registrar.
- **Read:** consultar.
- **Update:** actualizar.
- **Delete:** eliminar.

Los datos mostrados en la tabla son:

- Identificador.
- Nombre.
- Usuario.
- Rol.

La contraseña no se muestra en el `Treeview` por tratarse de un dato privado dentro de la interfaz.

### Registro

El administrador puede registrar usuarios con los roles:

- Empleado.
- Cliente.

No se permite registrar nuevos administradores desde esta pantalla.

### Consulta

Los usuarios registrados aparecen en un `Treeview`.

Al seleccionar una fila se utiliza el evento:

```python
<<TreeviewSelect>>
```

Este evento permite cargar los datos del usuario seleccionado en el formulario.

### Actualización

El administrador puede modificar los datos del usuario seleccionado.

Antes de guardar los cambios, los datos son validados por el `RestauranteServicio`.

### Eliminación

El administrador puede eliminar usuarios registrados.

La aplicación evita que el administrador elimine accidentalmente la cuenta con la que se encuentra autenticado.

---

## 11. Gestión de productos

La sección de productos permite:

- Registrar productos.
- Consultar productos.
- Seleccionar productos.
- Actualizar productos.
- Eliminar productos.
- Limpiar el formulario.

Cada producto contiene:

```text
Código
Nombre
Precio
Categoría
```

Los cambios realizados se guardan en:

```text
datos/productos.json
```

---

## 12. Gestión de ventas

La sección de ventas permite registrar una venta asociando:

- Un usuario.
- Un producto.
- Una fecha.

El sistema genera automáticamente un identificador para cada venta.

Los registros se almacenan en:

```text
datos/ventas.json
```

La información permanece disponible incluso después de cerrar y volver a ejecutar la aplicación.

---

## 13. Persistencia mediante JSON

La aplicación utiliza archivos JSON como mecanismo de almacenamiento local.

Los archivos principales son:

```text
datos/usuarios.json
datos/productos.json
datos/ventas.json
```

Cuando se registra, actualiza o elimina información, el `ArchivoServicio` actualiza el archivo correspondiente.

Esto permite que los datos no se pierdan al cerrar la aplicación.

---

## 14. Manejo de eventos en Tkinter

Uno de los aspectos principales desarrollados en el proyecto es el manejo de eventos.

Los eventos permiten que la aplicación responda a las acciones realizadas por el usuario.

### Evento `<<TreeviewSelect>>`

Se utiliza para detectar cuando el usuario selecciona un registro de la tabla.

Ejemplo:

```python
self.tree_usuarios.bind(
    "<<TreeviewSelect>>",
    self.seleccionar_usuario
)
```

Al seleccionar un usuario, sus datos se cargan automáticamente en el formulario.

---

### Evento `<<ComboboxSelected>>`

Se utiliza cuando el usuario selecciona una opción del `Combobox`.

En la gestión de usuarios permite detectar el rol seleccionado.

Ejemplo:

```python
self.rol_combo.bind(
    "<<ComboboxSelected>>",
    self.cambio_rol
)
```

---

### Evento `<Return>`

Permite ejecutar el registro de un usuario presionando la tecla **Enter**.

Ejemplo:

```python
self.rol_combo.bind(
    "<Return>",
    self.registrar_usuario_evento
)
```

De esta forma, además del botón de registro, el usuario puede utilizar el teclado.

---

### Evento `<Escape>`

Permite limpiar el formulario y cancelar una selección utilizando la tecla **Esc**.

Ejemplo:

```python
self.usuario_entry.bind(
    "<Escape>",
    self.limpiar_formulario_evento
)
```

Esto facilita la interacción con la aplicación.

---

### Eventos mediante `command=`

Los botones utilizan callbacks mediante el parámetro `command`.

Por ejemplo:

```python
ttk.Button(
    ventana,
    text="Registrar",
    command=self.registrar_usuario
)
```

Cuando el usuario presiona el botón, se ejecuta la función correspondiente.

---

## 15. Separación de responsabilidades

La aplicación evita colocar toda la lógica dentro de la interfaz gráfica.

La estructura utilizada es:

```text
Interfaz gráfica
       ↓
RestauranteServicio
       ↓
Modelos
       ↓
ArchivoServicio
       ↓
Archivos JSON
```

Por ejemplo, cuando se registra un usuario:

1. El usuario completa el formulario.
2. La interfaz obtiene los datos.
3. La interfaz llama a `registrar_usuario()`.
4. `RestauranteServicio` valida los datos.
5. Se crea un objeto `Usuario`.
6. Se agrega a la colección de usuarios.
7. Se guarda la información en `usuarios.json`.
8. La interfaz actualiza la tabla.

Esta organización permite mantener el código más ordenado y facilita su mantenimiento.

---

## 16. Validaciones implementadas

El sistema realiza diferentes validaciones.

Entre ellas:

- Campos obligatorios.
- Identificadores duplicados.
- Nombres de usuario duplicados.
- Roles válidos.
- Precios válidos.
- Existencia de usuarios.
- Existencia de productos.
- Prevención de eliminación del usuario autenticado.
- Prevención del cambio de rol del administrador autenticado.

Las validaciones principales se encuentran en los modelos y en `RestauranteServicio`.

---

## 17. Recursos gráficos

La aplicación utiliza recursos almacenados dentro de la carpeta `assets`.

### Logo

El logo se encuentra en:

```text
assets/logo/logo.png
```

### Icono de la aplicación

Se encuentra en:

```text
assets/logo/icono.png
```

### Iconos de navegación

Se encuentran en:

```text
assets/icons/
```

Estos recursos son utilizados para mejorar la presentación visual de la interfaz.

---

## 18. Flujo general de la aplicación

El funcionamiento general es:

```text
Iniciar aplicación
       ↓
Pantalla de inicio de sesión
       ↓
Validación de credenciales
       ↓
Interfaz principal
       ↓
┌──────────────┬──────────────┬──────────────┐
│   Usuarios   │  Productos   │    Ventas    │
└──────────────┴──────────────┴──────────────┘
       ↓
Operaciones CRUD
       ↓
RestauranteServicio
       ↓
ArchivoServicio
       ↓
Archivos JSON
```

---

## 19. Pruebas realizadas

Para comprobar el funcionamiento de la aplicación se pueden realizar las siguientes pruebas:

### Prueba 1: Inicio de sesión

Ingresar las credenciales del administrador y comprobar que se muestre la ventana principal.

### Prueba 2: Registro de usuario

Registrar un nuevo empleado o cliente y comprobar que aparezca en el `Treeview`.

### Prueba 3: Selección de usuario

Seleccionar un registro de la tabla y verificar que sus datos aparezcan en el formulario.

### Prueba 4: Actualización

Modificar los datos de un usuario y comprobar que los cambios se reflejen en la tabla y en `usuarios.json`.

### Prueba 5: Eliminación

Seleccionar un usuario y eliminarlo. Posteriormente verificar que ya no aparezca en la tabla.

### Prueba 6: Tecla Enter

Completar los datos del formulario y utilizar la tecla **Enter** para ejecutar el registro.

### Prueba 7: Tecla Escape

Completar o seleccionar información y presionar **Esc** para limpiar el formulario.

### Prueba 8: Persistencia

Cerrar la aplicación, volver a ejecutarla y comprobar que los datos registrados anteriormente continúen disponibles.

---

## 20. Ejecución del proyecto

Para ejecutar el proyecto se debe abrir una terminal dentro de la carpeta principal:

```bash
cd Restaurante_app__2.7
```

Después ejecutar:

```bash
python main.py
```

La aplicación mostrará inicialmente la pantalla de inicio de sesión.

---

## 21. Conclusión

El proyecto **Restaurante App** integra diferentes conocimientos de programación orientada a objetos y desarrollo de interfaces gráficas con Python.

Durante su desarrollo se implementaron modelos para representar usuarios, productos y ventas; servicios para manejar la lógica de negocio y los archivos; y vistas construidas con Tkinter para permitir la interacción con el usuario.

La incorporación de eventos como `<<TreeviewSelect>>`, `<<ComboboxSelected>>`, `<Return>` y `<Escape>` permite que la aplicación responda de manera más dinámica a las acciones realizadas mediante el mouse y el teclado.

Además, el uso de archivos JSON permite mantener la información almacenada de manera persistente, mientras que la separación entre interfaz, servicios y modelos contribuye a mantener una estructura organizada y fácil de modificar.

De esta manera, el proyecto constituye una aplicación funcional que reúne los principales conceptos trabajados durante el desarrollo del curso y los aplica en un caso práctico relacionado con la gestión de un restaurante.