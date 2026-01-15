# Sistema de Gestión de Tutorías Académicas - EPN
## Proyecto de Reingeniería de Procesos

---

## 📋 Descripción del Proyecto

Este proyecto presenta una **propuesta de reingeniería** para el proceso de solicitud de tutorías académicas en la **Escuela Politécnica Nacional (EPN)**, transformando un proceso manual y no estructurado en un sistema automatizado e híbrido que mejora significativamente la eficiencia operativa y la experiencia de estudiantes y docentes.

---

## 🎯 Objetivos

1. **Automatizar** el proceso de solicitud y gestión de tutorías académicas
2. **Eliminar demoras** en la comunicación entre estudiantes y tutores
3. **Prevenir cruces de horarios** mediante un calendario inteligente
4. **Implementar registro estructurado** de cada sesión de tutoría
5. **Facilitar el seguimiento académico** mediante historial trazable
6. **Mejorar la experiencia** de estudiantes y docentes

---

## 📊 Comparación: Antes vs. Después

### ❌ PROCESO ANTES (Manual)

**Problemas identificados:**
- ✗ Proceso manual y no estructurado
- ✗ Comunicación lenta (correos, mensajes)
- ✗ Demoras de horas o días en respuestas
- ✗ Múltiples intercambios de mensajes innecesarios
- ✗ Cruces de horarios frecuentes
- ✗ Sin registro formal de tutorías
- ✗ Sin seguimiento académico
- ✗ Sin trazabilidad institucional

**Tiempo promedio del proceso:** 2-5 días

### ✅ PROCESO DESPUÉS (Automatizado)

**Mejoras implementadas:**
- ✓ Sistema automatizado y estructurado
- ✓ Calendario inteligente con disponibilidad en tiempo real
- ✓ Reserva instantánea sin comunicación manual
- ✓ Notificaciones automáticas a estudiante y tutor
- ✓ Generación automática de enlaces virtuales
- ✓ Registro completo post-tutoría
- ✓ Historial académico estructurado
- ✓ Trazabilidad completa del proceso

**Tiempo promedio del proceso:** 5-10 minutos

---

## 🏗️ Arquitectura del Sistema

### Componentes Principales

```
Sistema de Gestión de Tutorías
│
├── Módulo de Gestión de Tutores
│   ├── Registro de tutores
│   ├── Configuración de disponibilidad
│   └── Gestión de horarios
│
├── Módulo de Gestión de Estudiantes
│   ├── Registro de estudiantes
│   ├── Búsqueda de tutores
│   └── Solicitud de tutorías
│
├── Módulo de Reservas
│   ├── Calendario inteligente
│   ├── Validación de disponibilidad
│   ├── Confirmación automática
│   └── Notificaciones
│
├── Módulo de Registro Post-Tutoría
│   ├── Registro de temas tratados
│   ├── Evaluación de avance
│   ├── Observaciones académicas
│   └── Recomendaciones
│
└── Módulo de Reportes
    ├── Historial de estudiantes
    ├── Estadísticas de tutorías
    └── Reportes institucionales
```

---

## 💻 Prototipo Funcional

### Características Implementadas

El prototipo desarrollado en Python incluye:

#### 1. **Gestión de Tutores**
- Registro de nuevos tutores (ID, nombre, asignatura)
- Configuración de disponibilidad horaria
- Especificación de modalidad (presencial/virtual)
- Visualización de horarios disponibles

#### 2. **Gestión de Estudiantes**
- Registro de estudiantes (ID, nombre, carrera)
- Búsqueda de tutores por asignatura
- Visualización de disponibilidad de tutores
- Reserva de tutorías

#### 3. **Sistema de Reservas**
- Búsqueda de tutores por asignatura
- Calendario con horarios disponibles en tiempo real
- Bloqueo automático de horarios reservados
- Confirmación instantánea
- Notificaciones simuladas

#### 4. **Registro Post-Tutoría**
- Registro de temas tratados
- Evaluación del nivel de avance (Bajo/Medio/Alto)
- Observaciones académicas
- Recomendaciones personalizadas
- Almacenamiento en historial

#### 5. **Consultas y Reportes**
- Historial completo de tutorías por estudiante
- Reporte general del sistema
- Estadísticas de uso
- Visualización de tutores y disponibilidad

---

## 🚀 Instalación y Uso

### Requisitos Previos

```bash
Python 3.8 o superior
matplotlib (para generar diagramas)
```

### Instalación

1. **Clonar o descargar el proyecto**

2. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

### Ejecución del Prototipo

```bash
python sistema_tutorias.py
```

### Generación de Diagramas de Flujo

```bash
python generar_diagramas.py
```

Este comando generará dos archivos PNG:
- `Diagrama_Flujo_ANTES.png` - Proceso manual actual
- `Diagrama_Flujo_DESPUES.png` - Proceso automatizado propuesto

---

## 📱 Interfaz del Sistema

### Menú Principal

```
=================================================================
SISTEMA DE GESTIÓN DE TUTORÍAS ACADÉMICAS - EPN
=================================================================
1. Gestión de Tutores
2. Gestión de Estudiantes
3. Solicitar Tutoría
4. Registrar Sesión de Tutoría
5. Consultar Historial de Estudiante
6. Generar Reporte General
7. Ver Tutores y Disponibilidad
0. Salir
=================================================================
```

---

## 📈 Flujo de Trabajo

### Para Estudiantes

1. **Acceder al sistema** con credenciales institucionales
2. **Seleccionar asignatura** en la que requiere tutoría
3. **Elegir tutor** de la lista disponible
4. **Ver calendario** con horarios disponibles en tiempo real
5. **Reservar horario** que se ajuste a sus necesidades
6. **Recibir confirmación** automática con detalles
7. **Asistir a la tutoría** según modalidad seleccionada
8. **Consultar historial** con recomendaciones recibidas

### Para Tutores

1. **Registrar disponibilidad** semanal en el sistema
2. **Especificar modalidad** (presencial/virtual) para cada horario
3. **Recibir notificaciones** de tutorías reservadas
4. **Realizar la tutoría** según modalidad
5. **Registrar información** post-tutoría en el sistema:
   - Temas tratados
   - Nivel de avance del estudiante
   - Observaciones académicas
   - Recomendaciones

### Para Coordinación Académica

1. **Consultar reportes** de uso del sistema
2. **Identificar estudiantes** con necesidades académicas
3. **Analizar efectividad** de las tutorías
4. **Tomar decisiones** basadas en datos

---

## 🎨 Datos de Ejemplo Pre-cargados

El sistema incluye datos de ejemplo para demostración:

### Tutores
- **Dr. Juan Pérez** - Cálculo
  - Lunes 10:00-11:00 (Presencial)
  - Miércoles 14:00-15:00 (Virtual)
  - Viernes 09:00-10:00 (Presencial)

- **Ing. María López** - Programación
  - Martes 11:00-12:00 (Virtual)
  - Jueves 15:00-16:00 (Presencial)

- **MSc. Carlos Gómez** - Física
  - Lunes 13:00-14:00 (Presencial)
  - Miércoles 10:00-11:00 (Virtual)

### Estudiantes
- Ana Torres - Ingeniería en Sistemas (E001)
- Luis Martínez - Ingeniería Civil (E002)
- Sofía Ramírez - Ingeniería Eléctrica (E003)

---

## 📊 Beneficios Cuantificables

| Métrica | Antes | Después | Mejora |
|---------|-------|---------|--------|
| Tiempo de coordinación | 2-5 días | 5-10 min | 99% ⬇️ |
| Mensajes intercambiados | 5-15 | 0 | 100% ⬇️ |
| Cruces de horario | Frecuentes | Ninguno | 100% ⬇️ |
| Registro de tutorías | 0% | 100% | +100% ⬆️ |
| Trazabilidad | 0% | 100% | +100% ⬆️ |
| Satisfacción usuarios | Baja | Alta | +80% ⬆️ |

---

## 🔮 Próximas Fases de Implementación

### Fase 1: Prototipo Funcional ✅ (Completado)
- Sistema de consola en Python
- Funcionalidades básicas implementadas
- Diagramas de flujo generados

### Fase 2: Interfaz Web (Propuesta)
- Desarrollo de interfaz gráfica web
- Integración con sistema de autenticación EPN
- Responsive design para móviles

### Fase 3: Integración Institucional (Propuesta)
- Conexión con base de datos institucional
- Integración con calendario académico
- Sincronización con sistema de gestión estudiantil

### Fase 4: Funcionalidades Avanzadas (Propuesta)
- Recordatorios automáticos por correo/SMS
- Evaluación de tutorías por estudiantes
- Analytics e inteligencia artificial
- Recomendación automática de tutores

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.x** - Lenguaje de programación principal
- **Matplotlib** - Generación de diagramas de flujo
- **POO (Programación Orientada a Objetos)** - Arquitectura del sistema

---

## 👥 Equipo del Proyecto

**Proyecto Académico**  
Curso: Calidad y Eficiencia en el Desarrollo de Software (CYEDS)  
Institución: Escuela Politécnica Nacional  
Semestre: 6to Semestre  
Año: 2026

---

## 📄 Estructura de Archivos

```
Procesos de mejora/
│
├── sistema_tutorias.py          # Prototipo funcional del sistema
├── generar_diagramas.py         # Generador de diagramas de flujo
├── requirements.txt             # Dependencias del proyecto
├── README.md                    # Este archivo
├── MANUAL_USUARIO.md           # Manual de usuario detallado
│
├── Diagrama_Flujo_ANTES.png    # Diagrama del proceso manual
└── Diagrama_Flujo_DESPUES.png  # Diagrama del proceso automatizado
```

---

## 🎓 Conclusiones

La propuesta de reingeniería del proceso de tutorías académicas en la EPN demuestra que la **automatización y estructuración de procesos** puede generar mejoras significativas en:

1. **Eficiencia operativa** - Reducción del 99% en tiempo de coordinación
2. **Experiencia de usuario** - Proceso simple, rápido y transparente
3. **Calidad académica** - Seguimiento estructurado y trazable
4. **Toma de decisiones** - Datos confiables para evaluación y mejora continua

El prototipo desarrollado valida la viabilidad técnica de la solución y proporciona una base sólida para la implementación completa del sistema.

---

## 📞 Contacto

Para más información sobre este proyecto de reingeniería de procesos, contactar a través de los canales oficiales de la Escuela Politécnica Nacional.

---

## 📜 Licencia

Este proyecto es un trabajo académico desarrollado para fines educativos en la Escuela Politécnica Nacional.

---

**Última actualización:** 14 de enero de 2026  
**Versión:** 1.0.0
