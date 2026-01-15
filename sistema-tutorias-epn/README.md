# Sistema de Gestión de Tutorías Académicas - EPN

## Descripción del Proyecto

Sistema web integral para la gestión automatizada de tutorías académicas en la Escuela Politécnica Nacional (EPN). Este proyecto implementa un proceso reingeniado que reemplaza el sistema manual actual, mejorando significativamente la eficiencia operativa y la experiencia tanto de estudiantes como de docentes.

## Características Principales

### Para Estudiantes
- ✅ Solicitud de tutorías en línea
- ✅ Visualización de disponibilidad en tiempo real
- ✅ Historial completo de tutorías
- ✅ Acceso a recomendaciones personalizadas
- ✅ Notificaciones automáticas

### Para Tutores
- ✅ Gestión de disponibilidad semanal
- ✅ Calendario automatizado
- ✅ Registro estructurado de tutorías
- ✅ Seguimiento académico de estudiantes
- ✅ Soporte para modalidad presencial y virtual

### Para Coordinadores
- ✅ Dashboard con estadísticas en tiempo real
- ✅ Reportes detallados por asignatura
- ✅ Identificación de estudiantes en riesgo
- ✅ Análisis de efectividad del programa
- ✅ Exportación de datos

## Tecnologías Utilizadas

- **Backend**: Python 3.x, Flask
- **Base de Datos**: SQLite (SQLAlchemy ORM)
- **Frontend**: HTML5, CSS3, JavaScript
- **Framework CSS**: Bootstrap 5.3
- **Gráficos**: Chart.js
- **Autenticación**: Flask-Login

## Estructura del Proyecto

```
sistema-tutorias-epn/
├── app/
│   ├── __init__.py          # Inicialización de la aplicación
│   ├── models.py            # Modelos de base de datos
│   ├── routes.py            # Rutas y controladores
│   └── utils.py             # Funciones utilitarias
├── static/
│   ├── css/
│   │   └── style.css        # Estilos personalizados
│   ├── js/
│   │   └── main.js          # JavaScript interactivo
│   └── img/                 # Imágenes
├── templates/               # Templates HTML
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── estudiante/
│   ├── tutor/
│   └── coordinador/
├── data/
│   └── tutorias.db          # Base de datos SQLite
├── docs/                    # Documentación
├── run.py                   # Punto de entrada
├── requirements.txt         # Dependencias
└── README.md               # Este archivo
```

## Instalación

### 1. Clonar el repositorio o descargar los archivos

### 2. Crear entorno virtual (recomendado)

```bash
python -m venv venv
```

### 3. Activar el entorno virtual

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Ejecutar la aplicación

```bash
python run.py
```

### 6. Acceder a la aplicación

Abrir el navegador y visitar: `http://localhost:5000`

## Credenciales de Prueba

El sistema viene con datos de prueba pre-cargados:

### Estudiante
- **Cédula**: 1750000001
- **Contraseña**: est123

### Tutor
- **Cédula**: 1700000002
- **Contraseña**: tutor123

### Coordinador
- **Cédula**: 1700000001
- **Contraseña**: coord123

## Flujo de Procesos

### Proceso ANTES (Manual)
1. Estudiante contacta al tutor por correo/mensaje
2. Intercambio manual de mensajes para acordar horario
3. Posibles cruces de horarios
4. Sin registro formal de tutorías
5. Sin seguimiento académico estructurado

### Proceso DESPUÉS (Automatizado)
1. **Configuración**: Tutor registra disponibilidad en el sistema
2. **Solicitud**: Estudiante selecciona asignatura y visualiza disponibilidad
3. **Reserva**: Sistema valida y confirma automáticamente
4. **Notificación**: Envío automático de confirmaciones
5. **Ejecución**: Tutoría según modalidad (presencial/virtual)
6. **Registro**: Tutor documenta resultados y recomendaciones
7. **Seguimiento**: Sistema mantiene historial y genera estadísticas

## Beneficios de la Reingeniería

### Eficiencia Operativa
- ⚡ Reducción del 80% en tiempo de coordinación
- 🎯 Eliminación de conflictos de horarios
- 📊 Automatización del registro y seguimiento

### Experiencia de Usuario
- 🚀 Proceso simplificado y rápido
- 📱 Acceso 24/7 desde cualquier dispositivo
- ✨ Interfaz intuitiva y moderna

### Gestión Académica
- 📈 Trazabilidad completa de tutorías
- 🎓 Seguimiento personalizado por estudiante
- 📋 Reportes para toma de decisiones

## Módulos del Sistema

### Módulo de Usuarios
- Gestión de estudiantes, tutores y coordinadores
- Autenticación segura
- Perfiles personalizados

### Módulo de Disponibilidad
- Configuración de horarios por tutor
- Validación automática de disponibilidad
- Gestión de modalidades (presencial/virtual)

### Módulo de Tutorías
- Solicitud y programación
- Ejecución y registro
- Historial y seguimiento

### Módulo de Reportes
- Estadísticas en tiempo real
- Gráficos interactivos
- Exportación de datos

## Diagramas de Flujo

Los diagramas de flujo del proceso ANTES y DESPUÉS están disponibles en la carpeta `docs/`:
- `proceso_antes.png`: Proceso manual actual
- `proceso_despues.png`: Proceso automatizado propuesto

Para generar los diagramas nuevamente:
```bash
python generar_diagramas.py
```

## API Endpoints

El sistema incluye una API interna para operaciones dinámicas:

- `GET /api/tutores-por-asignatura/<id>`: Obtener tutores disponibles
- `GET /api/disponibilidad-tutor/<tutor_id>/<asignatura_id>`: Ver disponibilidad
- `POST /api/cancelar-tutoria/<id>`: Cancelar tutoría
- `POST /api/eliminar-disponibilidad/<id>`: Eliminar disponibilidad

## Seguridad

- ✅ Contraseñas hasheadas con Werkzeug
- ✅ Autenticación basada en sesiones
- ✅ Protección de rutas con decoradores
- ✅ Validación de datos en cliente y servidor

## Mantenimiento

### Base de Datos
La base de datos SQLite se crea automáticamente en el primer arranque. Para reiniciar:

```bash
# Eliminar la base de datos
del data\tutorias.db  # Windows
rm data/tutorias.db   # Linux/Mac

# Reiniciar la aplicación para recrear
python run.py
```

### Logs
Los errores y actividades se muestran en la consola durante la ejecución.

## Expansiones Futuras

- 📧 Integración con correo electrónico institucional
- 📅 Sincronización con calendarios externos (Google Calendar, Outlook)
- 💬 Sistema de mensajería interna
- 📱 Aplicación móvil nativa
- 🤖 Recordatorios automáticos por SMS/WhatsApp
- 📊 Análisis predictivo con Machine Learning
- 🔔 Sistema de notificaciones push

## Soporte y Contacto

Para preguntas, sugerencias o reportar problemas:
- **Institución**: Escuela Politécnica Nacional
- **Proyecto**: Sistema de Gestión de Tutorías Académicas
- **Año**: 2026

## Licencia

Este proyecto es desarrollado para uso interno de la Escuela Politécnica Nacional.

## Autores

Proyecto desarrollado como parte del proceso de reingeniería de procesos académicos en la EPN.

---

**© 2026 Escuela Politécnica Nacional - Todos los derechos reservados**
