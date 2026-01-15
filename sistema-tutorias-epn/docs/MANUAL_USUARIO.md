# Manual de Usuario - Sistema de Gestión de Tutorías Académicas EPN

## Tabla de Contenidos
1. [Introducción](#introducción)
2. [Acceso al Sistema](#acceso-al-sistema)
3. [Módulo Estudiante](#módulo-estudiante)
4. [Módulo Tutor](#módulo-tutor)
5. [Módulo Coordinador](#módulo-coordinador)
6. [Preguntas Frecuentes](#preguntas-frecuentes)
7. [Solución de Problemas](#solución-de-problemas)

---

## Introducción

Bienvenido al Sistema de Gestión de Tutorías Académicas de la Escuela Politécnica Nacional. Este sistema permite gestionar de manera eficiente todas las tutorías académicas, desde la solicitud hasta el seguimiento académico.

### Objetivos del Sistema
- Facilitar la solicitud y programación de tutorías
- Automatizar la gestión de disponibilidad de tutores
- Mantener un registro estructurado de todas las sesiones
- Proporcionar seguimiento académico personalizado
- Generar reportes y estadísticas para toma de decisiones

### Tipos de Usuario
El sistema cuenta con tres perfiles de usuario:

1. **Estudiante**: Puede solicitar tutorías y ver su historial
2. **Tutor**: Gestiona disponibilidad y registra tutorías realizadas
3. **Coordinador**: Supervisa el sistema y genera reportes

---

## Acceso al Sistema

### 1. Abrir el Sistema

1. Abrir el navegador web (Chrome, Firefox, Edge, Safari)
2. Navegar a: `http://localhost:5000`
3. Se mostrará la página principal del sistema

### 2. Iniciar Sesión

1. Hacer clic en "Iniciar Sesión" en la barra de navegación
2. Ingresar su número de cédula (10 dígitos, sin guiones ni espacios)
3. Ingresar su contraseña
4. Hacer clic en "Ingresar"

### 3. Recuperar Contraseña

Si olvidó su contraseña, contacte al coordinador académico para restablecerla.

### 4. Cerrar Sesión

Para cerrar sesión de forma segura:
1. Hacer clic en su nombre en la esquina superior derecha
2. Seleccionar "Cerrar Sesión"

---

## Módulo Estudiante

### Dashboard Principal

Al iniciar sesión como estudiante, verá:

- **Estadísticas rápidas**: Número de tutorías programadas y realizadas
- **Próximas tutorías**: Lista de tutorías programadas
- **Últimas tutorías realizadas**: Historial reciente con recomendaciones

### Solicitar una Tutoría

#### Paso 1: Acceder al Formulario
1. En el dashboard, hacer clic en "Solicitar Tutoría"
2. O desde el menú principal

#### Paso 2: Seleccionar Asignatura
1. En el primer campo, seleccionar la asignatura para la cual necesita tutoría
2. El sistema cargará automáticamente los tutores disponibles

#### Paso 3: Seleccionar Tutor
1. Elegir el tutor de su preferencia de la lista desplegable
2. El sistema mostrará automáticamente la disponibilidad del tutor

#### Paso 4: Ver Disponibilidad
El sistema muestra una tabla con:
- Días de la semana disponibles
- Horarios específicos
- Modalidad (Presencial o Virtual)
- Ubicación (aula o enlace de reunión)

#### Paso 5: Seleccionar Fecha y Hora
1. Elegir una fecha dentro del rango disponible
2. Seleccionar hora de inicio
3. Seleccionar hora de fin
4. Asegurarse de que coincida con la disponibilidad mostrada

#### Paso 6: Confirmar
1. Revisar todos los datos ingresados
2. Hacer clic en "Confirmar Tutoría"
3. El sistema mostrará un mensaje de confirmación

### Ver Historial de Tutorías

1. En el dashboard, hacer clic en "Ver Historial" o el botón de Historial
2. Se mostrará una tabla con todas sus tutorías:
   - Fecha y hora
   - Asignatura
   - Tutor
   - Modalidad
   - Estado (Programada, Realizada, Cancelada)

#### Ver Detalles de una Tutoría
1. En el historial, hacer clic en el botón "Ver" junto a la tutoría
2. Se abrirá un modal con información detallada:
   - Información básica de la sesión
   - Temas tratados (si la tutoría ya se realizó)
   - Nivel de avance evaluado por el tutor
   - Observaciones del tutor
   - Recomendaciones personalizadas

### Cancelar una Tutoría

1. En el dashboard, localizar la tutoría en "Próximas Tutorías"
2. Hacer clic en el botón "Cancelar"
3. Confirmar la cancelación en el mensaje de alerta
4. La tutoría cambiará su estado a "Cancelada"

**Nota**: Solo se pueden cancelar tutorías que aún no se han realizado.

---

## Módulo Tutor

### Dashboard del Tutor

El dashboard muestra:

- **Tutorías de hoy**: Sesiones programadas para el día actual
- **Próximas tutorías**: Agenda de tutorías futuras
- **Pendientes de registro**: Tutorías pasadas que necesitan ser registradas

### Gestionar Disponibilidad

#### Agregar Nueva Disponibilidad

1. Hacer clic en "Gestionar Disponibilidad"
2. Completar el formulario:
   - **Asignatura**: Materia que puede tutorar
   - **Día de la semana**: Lunes a Sábado
   - **Hora inicio**: Hora de inicio de disponibilidad
   - **Hora fin**: Hora de finalización
   - **Modalidad**: Presencial o Virtual
   - **Ubicación/Enlace**: 
     - Para presencial: nombre del aula (ej: "Aula 201")
     - Para virtual: enlace de reunión (ej: Google Meet link)
3. Hacer clic en "Agregar Disponibilidad"

#### Ver Disponibilidades Configuradas

Las disponibilidades se organizan por asignatura en un acordeón:
1. Hacer clic en el nombre de la asignatura para expandir
2. Ver lista de todas las disponibilidades de esa materia
3. Cada entrada muestra: día, horario, modalidad y ubicación

#### Eliminar una Disponibilidad

1. Localizar la disponibilidad que desea eliminar
2. Hacer clic en el botón de basura (🗑️)
3. Confirmar la eliminación
4. La disponibilidad será desactivada

**Importante**: Eliminar una disponibilidad no cancela tutorías ya programadas.

### Registrar una Tutoría Realizada

#### Cuándo Registrar
Después de realizar cada tutoría, debe registrar los resultados para mantener el historial académico del estudiante.

#### Proceso de Registro

1. En el dashboard, localizar la sección "Tutorías Pendientes de Registro"
2. Hacer clic en "Registrar" junto a la tutoría correspondiente
3. Completar el formulario:

##### Información a Registrar:

**Temas Tratados** (Obligatorio)
- Listar los temas específicos abordados en la sesión
- Ejemplo: "Derivadas parciales, regla de la cadena, ejercicios de aplicación"

**Nivel de Avance** (Obligatorio)
Seleccionar una de las siguientes opciones:
- **Excelente**: Domina completamente los conceptos
- **Bueno**: Comprende bien, con práctica mejorará
- **Regular**: Requiere más estudio y práctica
- **Necesita Refuerzo**: Dificultades significativas

**Observaciones** (Opcional)
- Detalles sobre actitud, participación, dificultades específicas
- Ejemplo: "Mostró interés pero necesita reforzar conceptos previos"

**Recomendaciones** (Obligatorio)
- Sugerencias concretas para estudio autónomo
- Ejemplo: "Resolver ejercicios del capítulo 5, revisar videos sobre límites"

4. Hacer clic en "Guardar Registro"

**Nota**: Esta información será visible para el estudiante y la coordinación académica.

### Visualizar Calendario de Tutorías

En el dashboard puede ver:
- **Hoy**: Todas las tutorías programadas para el día actual
- **Próximas**: Lista de tutorías futuras ordenadas por fecha

Para cada tutoría se muestra:
- Nombre del estudiante
- Asignatura
- Horario
- Modalidad y ubicación

---

## Módulo Coordinador

### Dashboard del Coordinador

Vista general del sistema con:

#### Estadísticas Principales
- **Total de Estudiantes Activos**
- **Total de Tutores Activos**
- **Total de Tutorías Registradas**
- **Tutorías del Mes Actual**

#### Actividad Reciente
Tabla con las tutorías más recientes del sistema, mostrando:
- Fecha y horario
- Estudiante y tutor involucrados
- Asignatura
- Modalidad (presencial/virtual)
- Estado y nivel de avance

### Ver Reportes Detallados

1. Hacer clic en "Ver Reportes Detallados"

#### Gráficos Disponibles

**1. Tutorías por Estado**
- Gráfico circular (donut chart)
- Muestra distribución de tutorías: Programadas, Realizadas, Canceladas
- Incluye números exactos para cada categoría

**2. Tutorías por Asignatura**
- Gráfico de barras
- Compara el número de tutorías por cada asignatura
- Permite identificar asignaturas con mayor demanda

#### Tabla Resumen por Asignatura

Tabla detallada con:
- Nombre de la asignatura
- Total de tutorías
- Desglose por estado (programadas, realizadas, canceladas)
- Tasa de éxito (porcentaje de tutorías realizadas vs canceladas)

#### Indicadores Clave de Desempeño (KPIs)

1. **Satisfacción de Estudiantes**: Porcentaje de satisfacción
2. **Tasa de Asistencia**: Porcentaje de tutorías realizadas
3. **Duración Promedio**: Tiempo promedio por sesión
4. **Tutorías por Estudiante**: Promedio de tutorías por estudiante

### Exportar Datos

1. En el dashboard del coordinador, hacer clic en "Exportar Datos (CSV)"
2. El sistema generará un archivo CSV con todas las tutorías
3. El archivo se descargará automáticamente

**Uso del CSV**: Puede abrir el archivo en Excel, Google Sheets o cualquier software de hojas de cálculo para análisis adicional.

### Identificar Estudiantes en Riesgo

Revisar en los reportes:
- Estudiantes con nivel de avance "Necesita Refuerzo"
- Estudiantes con múltiples tutorías en la misma asignatura
- Patrones de cancelaciones frecuentes

---

## Preguntas Frecuentes

### Para Estudiantes

**P: ¿Puedo solicitar varias tutorías al mismo tiempo?**
R: Sí, puede solicitar múltiples tutorías para diferentes asignaturas o fechas.

**P: ¿Cuánto tiempo antes debo solicitar una tutoría?**
R: Se recomienda solicitar con al menos 24 horas de anticipación.

**P: ¿Qué hago si no veo disponibilidad del tutor?**
R: El tutor aún no ha configurado su disponibilidad. Contacte al coordinador académico.

**P: ¿Puedo cambiar la hora de una tutoría ya programada?**
R: Debe cancelar la tutoría actual y solicitar una nueva en el horario deseado.

**P: ¿Cómo accedo al enlace de la tutoría virtual?**
R: El enlace aparece en la ubicación de la tutoría en su dashboard.

### Para Tutores

**P: ¿Puedo modificar una disponibilidad ya creada?**
R: Actualmente debe eliminar la disponibilidad antigua y crear una nueva.

**P: ¿Qué pasa si necesito cancelar una tutoría?**
R: Contacte al coordinador académico para gestionar cancelaciones especiales.

**P: ¿Debo registrar tutorías canceladas?**
R: No, solo debe registrar tutorías que efectivamente se realizaron.

**P: ¿Cuánto tiempo tengo para registrar una tutoría?**
R: Se recomienda registrar dentro de las 48 horas posteriores a la sesión.

### Para Coordinadores

**P: ¿Cómo agrego nuevos usuarios al sistema?**
R: Actualmente requiere acceso directo a la base de datos. Contacte al administrador del sistema.

**P: ¿Los reportes se actualizan en tiempo real?**
R: Sí, todos los datos y gráficos se actualizan automáticamente.

**P: ¿Puedo ver el historial de un estudiante específico?**
R: Sí, en la tabla de tutorías recientes puede filtrar por estudiante.

---

## Solución de Problemas

### Problemas de Acceso

**Problema**: No puedo iniciar sesión
- Verificar que la cédula esté correcta (10 dígitos, sin espacios)
- Verificar que la contraseña sea correcta (distingue mayúsculas y minúsculas)
- Contactar al coordinador para verificar que su cuenta esté activa

**Problema**: El sistema está lento
- Actualizar la página (F5)
- Limpiar caché del navegador
- Verificar conexión a internet

### Problemas al Solicitar Tutorías

**Problema**: No aparecen tutores disponibles
- El tutor puede no haber configurado disponibilidad para esa asignatura
- Contactar al coordinador académico

**Problema**: No puedo seleccionar una fecha
- Verificar que la fecha esté dentro de la disponibilidad del tutor
- La fecha debe ser futura (no puede programar tutorías en el pasado)

**Problema**: El botón "Confirmar" está deshabilitado
- Completar todos los campos obligatorios
- Verificar que haya seleccionado un tutor con disponibilidad

### Problemas Técnicos

**Problema**: No se cargan los gráficos
- Verificar conexión a internet
- Actualizar la página
- Probar con otro navegador

**Problema**: Los cambios no se guardan
- Verificar que haya hecho clic en el botón de guardar/confirmar
- No cerrar la página mientras se procesa una operación
- Si el problema persiste, contactar al soporte técnico

### Navegadores Recomendados

El sistema funciona mejor en:
- Google Chrome (versión 90 o superior)
- Mozilla Firefox (versión 88 o superior)
- Microsoft Edge (versión 90 o superior)
- Safari (versión 14 o superior)

---

## Contacto y Soporte

Para asistencia técnica o dudas sobre el uso del sistema:

- **Coordinación Académica**: Edificio Administrativo, Piso 2
- **Email**: tutorias@epn.edu.ec
- **Horario de Atención**: Lunes a Viernes, 8:00 - 17:00

---

## Consejos y Mejores Prácticas

### Para Estudiantes
✅ Revise su correo institucional regularmente para notificaciones
✅ Programe tutorías con anticipación
✅ Llegue puntual a las sesiones
✅ Prepare preguntas específicas antes de la tutoría
✅ Revise las recomendaciones después de cada sesión

### Para Tutores
✅ Mantenga actualizada su disponibilidad
✅ Registre las tutorías lo antes posible
✅ Sea específico en las recomendaciones
✅ Comunique cambios con anticipación

### Para Coordinadores
✅ Revise los reportes semanalmente
✅ Identifique patrones de demanda
✅ Contacte proactivamente a estudiantes en riesgo
✅ Mantenga comunicación con tutores sobre su carga

---

**Última actualización**: Enero 2026

**Versión del Manual**: 1.0

---

**© 2026 Escuela Politécnica Nacional - Sistema de Gestión de Tutorías Académicas**
