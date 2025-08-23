# API de Gestión de Marcas

Una API REST desarrollada con FastAPI para la gestión de usuarios y marcas, con autenticación JWT y base de datos SQLite.

## 🚀 Características

- **Autenticación JWT**: Sistema de login seguro con tokens
- **Gestión de Usuarios**: CRUD completo para usuarios
- **Gestión de Marcas**: CRUD completo para marcas asociadas a usuarios
- **Base de datos SQLite**: Almacenamiento local
- **Documentación automática**: Swagger UI integrado
- **CORS habilitado**: Listo para frontend

## 🛠️ Tecnologías

- **FastAPI**: Framework web moderno y rápido
- **SQLAlchemy**: ORM para base de datos
- **Pydantic**: Validación de datos
- **PyJWT**: Manejo de tokens JWT
- **Passlib**: Hashing de contraseñas
- **SQLite**: Base de datos embebida

## 📋 Prerequisitos

- Python 3.7+
- pip (gestor de paquetes de Python)

## ⚙️ Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/Juliandos/backend.git
cd backend
```

2. **Crear entorno virtual**
```bash
python -m venv venv
```

3. **Activar entorno virtual**
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

## 🚀 Uso

### Ejecutar el servidor

```bash
uvicorn main:app --reload
fastapi dev main.py
```

La API estará disponible en: `http://localhost:8000`

### Documentación interactiva

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 📚 Endpoints

### Autenticación

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/auth/token` | Login y obtención de token |
| GET | `/auth/me` | Información del usuario actual |

### Usuarios

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/usuarios/` | Crear usuario |
| POST | `/usuarios/registro` | Registro de nuevo usuario |
| GET | `/usuarios/` | Listar todos los usuarios |
| GET | `/usuarios/{id}` | Obtener usuario por ID |
| PUT | `/usuarios/{id}` | Actualizar usuario |
| DELETE | `/usuarios/{id}` | Eliminar usuario |

### Marcas

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/marcas/` | Crear marca |
| GET | `/marcas/` | Listar todas las marcas |
| GET | `/marcas/{id}` | Obtener marca por ID |
| PUT | `/marcas/{id}` | Actualizar marca |
| DELETE | `/marcas/{id}` | Eliminar marca |

## 🔐 Autenticación

### 1. Registrar usuario

```bash
curl -X POST "http://localhost:8000/usuarios/registro" \
-H "Content-Type: application/json" \
-d '{
  "nombre": "Juan Pérez",
  "correo": "juan@email.com",
  "password": "mi_password_seguro"
}'
```

### 2. Obtener token

```bash
curl -X POST "http://localhost:8000/auth/token" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "username=juan@email.com&password=mi_password_seguro"
```

### 3. Usar token en requests

```bash
curl -X GET "http://localhost:8000/marcas/" \
-H "Authorization: Bearer tu_token_aqui"
```

## 📊 Modelos de Datos

### Usuario
```json
{
  "id": 1,
  "nombre": "Juan Pérez",
  "correo": "juan@email.com",
  "created_at": "2024-01-01T00:00:00",
  "updated_at": "2024-01-01T00:00:00",
  "marcas": []
}
```

### Marca
```json
{
  "id": 1,
  "nombre": "Mi Marca",
  "titular": "Juan Pérez",
  "estado": true,
  "usuarios_id": 1,
  "created_at": "2024-01-01T00:00:00",
  "updated_at": "2024-01-01T00:00:00"
}
```

## 🗂️ Estructura del Proyecto

```
.
├── auth/                   # Módulo de autenticación
│   ├── __init__.py
│   └── security.py        # JWT y funciones de seguridad
├── models/                # Modelos SQLAlchemy
│   ├── __init__.py
│   ├── usuario.py
│   └── marca.py
├── routes/                # Endpoints de la API
│   ├── __init__.py
│   ├── auth.py
│   ├── usuario.py
│   └── marca.py
├── schemas/               # Schemas Pydantic
│   ├── __init__.py
│   ├── usuario.py
│   └── marca.py
├── database.py           # Configuración de base de datos
├── main.py              # Punto de entrada
├── requirements.txt     # Dependencias
├── .gitignore
└── README.md
```

## ⚙️ Configuración

### Variables de entorno

El proyecto usa las siguientes configuraciones (en `auth/security.py`):

- `SECRET_KEY`: Clave para firmar JWT tokens
- `ALGORITHM`: Algoritmo de encriptación (HS256)
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Tiempo de expiración del token (30 min)

### Base de datos

La aplicación usa SQLite por defecto (`app.db`). Las tablas se crean automáticamente al iniciar.

## 🧪 Testing

Para probar los endpoints, puedes usar:

- **Swagger UI**: `http://localhost:8000/docs`
- **curl**: Ver ejemplos en la sección de autenticación
- **Postman**: Importa los endpoints desde Swagger
- **httpx** o **requests**: Para testing automatizado

## 🤝 Contribuir

1. Fork el proyecto
2. Crea tu rama de feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver `LICENSE` para más detalles.

## 👤 Autor

**Tu Nombre**
- GitHub: [@Juliandos](https://github.com/Juliandos)
- Email: 95juliandos@gmail.com

## 🙏 Agradecimientos

- FastAPI por el excelente framework
- SQLAlchemy por el ORM
- Comunidad de Python por las librerías