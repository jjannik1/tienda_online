# Manual de Uso del Código

Este código es parte de una aplicación que gestiona productos, clientes, pedidos y reseñas. A continuación, se explica cómo funciona cada parte del código y cómo puedes interactuar con él.

## Descripción General

El código consta de varias clases que gestionan los productos, clientes, pedidos y reseñas. Además, proporciona un menú interactivo donde el usuario puede realizar diferentes acciones como agregar productos, clientes, realizar pedidos y añadir reseñas.

## Clases Principales

### Producto

La clase `Producto` representa un producto físico. Cada producto tiene un ID, un nombre, un precio y un stock.

#### Funcionalidades:
- Añadir un producto a la lista de productos.
- Listar todos los productos disponibles.
- Actualizar el stock de un producto.

### Cliente

La clase `Cliente` representa un cliente. Cada cliente tiene un ID, un nombre, un correo electrónico y una dirección.

#### Funcionalidades:
- Crear nuevos clientes.
- Listar todos los clientes registrados.

### Producto Digital

La clase `ProductoDigital` hereda de `Producto` y representa productos digitales (como libros o software). Además de las propiedades de un producto físico, tiene un formato (PDF, EPUB, etc.) y un tamaño.

#### Funcionalidades:
- Crear productos digitales.
- Listar productos digitales.

### Pedido

La clase `Pedido` representa un pedido realizado por un cliente. Un pedido tiene un ID, un cliente asociado, una fecha de realización y una lista de productos.

#### Funcionalidades:
- Crear un nuevo pedido.
- Listar pedidos.
- Calcular el total de un pedido.
- Agregar productos a un pedido.

### Reseña

La clase `Resena` permite a un cliente dejar una reseña sobre un producto. Cada reseña tiene un ID, un producto asociado, un cliente, un comentario y una puntuación.

#### Funcionalidades:
- Añadir una reseña a un producto.
- Listar todas las reseñas.

## Interacción con el Menú

El código proporciona un menú interactivo con las siguientes opciones:

### 1. Gestionar Productos
Permite gestionar productos físicos y digitales:
- **Añadir Producto**: Crea un nuevo producto, ya sea físico o digital.
- **Listar Productos**: Muestra todos los productos disponibles.
- **Actualizar Stock**: Actualiza el stock de un producto existente.

### 2. Gestionar Clientes
Permite gestionar clientes:
- **Añadir Cliente**: Crea un nuevo cliente.
- **Listar Clientes**: Muestra todos los clientes registrados.

### 3. Gestionar Pedidos
Permite gestionar pedidos:
- **Crear Pedido**: Crea un nuevo pedido para un cliente.
- **Listar Pedidos**: Muestra todos los pedidos realizados.
- **Calcular Total**: Muestra el valor total de un pedido.
- **Agregar Productos**: Añade productos a un pedido.

### 4. Gestionar Reseñas
Permite gestionar reseñas sobre productos:
- **Añadir Reseña**: Deja una reseña sobre un producto.
- **Listar Reseñas**: Muestra todas las reseñas de productos.

### 5. Salir
Cierra la aplicación.

## Ejemplo de Uso

1. **Agregar Producto:**
   - El usuario puede elegir la opción de "Gestionar productos" y seleccionar "Añadir producto". Luego, se le pedirá que indique si el producto es físico o digital y se le solicitarán los detalles del producto (ID, nombre, precio, stock, etc.).

2. **Crear Pedido:**
   - En "Gestionar pedidos", el usuario puede elegir "Crear pedido", seleccionar un cliente existente y añadir productos al pedido. Después puede listar todos los pedidos creados.

3. **Añadir Reseña:**
   - En "Gestionar reseñas", el usuario puede añadir una reseña a un producto, proporcionando un comentario y una puntuación.

## Conclusión

Este código permite gestionar productos, clientes, pedidos y reseñas de forma interactiva. Puedes agregar productos, crear pedidos y dejar reseñas sobre productos. El menú proporciona opciones sencillas para gestionar estos aspectos de manera eficiente.
