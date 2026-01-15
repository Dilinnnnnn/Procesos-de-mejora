# Manual de Usuario
## Sistema de Gestión de Tutorías Académicas - EPN

---

## 📖 Índice

1. [Introducción](#introducción)
2. [Acceso al Sistema](#acceso-al-sistema)
3. [Guía para Estudiantes](#guía-para-estudiantes)
4. [Guía para Tutores](#guía-para-tutores)
5. [Guía para Coordinadores](#guía-para-coordinadores)
6. [Preguntas Frecuentes](#preguntas-frecuentes)
7. [Solución de Problemas](#solución-de-problemas)

---

## 1. Introducción

### ¿Qué es el Sistema de Gestión de Tutorías?

El Sistema de Gestión de Tutorías Académicas es una plataforma diseñada para **facilitar y automatizar** el proceso de solicitud, coordinación y seguimiento de tutorías académicas en la Escuela Politécnica Nacional.

### Beneficios del Sistema

- ⚡ **Rapidez**: Reserva tutorías en menos de 5 minutos
- 📅 **Disponibilidad en tiempo real**: Ve horarios disponibles al instante
- 🔔 **Notificaciones automáticas**: Recibe confirmaciones y recordatorios
- 📊 **Historial completo**: Accede a tu registro de tutorías y recomendaciones
- 🚫 **Sin cruces de horarios**: El sistema previene conflictos automáticamente

---

## 2. Acceso al Sistema

### Requisitos del Sistema

- Python 3.8 o superior instalado
- Conexión a la red institucional (en versión completa)
- Credenciales institucionales válidas

### Primera Ejecución

1. Abrir una terminal o línea de comandos
2. Navegar a la carpeta del proyecto:
   ```bash
   cd "c:\6semestre\CYEDS\Procesos de mejora"
   ```
3. Ejecutar el sistema:
   ```bash
   python sistema_tutorias.py
   ```

---

## 3. Guía para Estudiantes

### 3.1 Solicitar una Tutoría

#### Paso 1: Acceder al Menú Principal
```
Seleccionar opción: 3. Solicitar Tutoría
```

#### Paso 2: Ingresar tu ID de Estudiante
```
ID del estudiante: E001
```
> 💡 **Tip**: Tu ID estudiantil es tu número de matrícula

#### Paso 3: Seleccionar la Asignatura
```
Asignatura requerida: Cálculo
```

#### Paso 4: Elegir un Tutor
El sistema mostrará los tutores disponibles:
```
--- TUTORES DISPONIBLES PARA CÁLCULO ---
1. Dr. Juan Pérez (ID: T001)
2. Ing. María González (ID: T002)

Seleccione un tutor (número): 1
```

#### Paso 5: Seleccionar Horario
El sistema muestra horarios disponibles en tiempo real:
```
--- HORARIOS DISPONIBLES DE Dr. Juan Pérez ---
1. Lunes - 10:00 a 11:00 (Presencial)
2. Miércoles - 14:00 a 15:00 (Virtual)
3. Viernes - 09:00 a 10:00 (Presencial)

Seleccione un horario (número): 2
```

#### Paso 6: Confirmación
```
✅ Tutoría reservada exitosamente
ID de Tutoría: TUT-0001
📧 Notificación enviada a tu correo institucional

Para tutorías virtuales:
🔗 Enlace: https://meet.epn.edu.ec/TUT-0001
```

### 3.2 Consultar tu Historial

#### Acceder al Historial
```
Seleccionar opción: 5. Consultar Historial de Estudiante
ID del estudiante: E001
```

#### Información Mostrada
```
--- HISTORIAL DE Ana Torres ---

1. Tutoría ID: TUT-0001
   Tutor: Dr. Juan Pérez
   Asignatura: Cálculo
   Fecha: Miércoles - 14:00
   Estado: Completada
   
   Temas: Derivadas y límites
   Nivel de avance: Alto
   Recomendaciones: Continuar practicando ejercicios del capítulo 5
```

### 3.3 Modalidades de Tutoría

#### Tutoría Presencial
- Asiste al aula o laboratorio indicado
- Lleva tu material de estudio
- Llega 5 minutos antes

#### Tutoría Virtual
- Usa el enlace proporcionado en la confirmación
- Asegúrate de tener buena conexión a internet
- Ten tu cámara y micrófono listos
- Accede 5 minutos antes

### 3.4 Mejores Prácticas

✅ **HACER:**
- Reservar con al menos 24 horas de anticipación
- Preparar preguntas específicas antes de la tutoría
- Revisar las recomendaciones después de cada sesión
- Asistir puntualmente a tus tutorías

❌ **EVITAR:**
- Reservar múltiples horarios simultáneamente
- Cancelar sin aviso previo
- Llegar tarde a las tutorías

---

## 4. Guía para Tutores

### 4.1 Registrarse en el Sistema

```
Seleccionar opción: 1. Gestión de Tutores
Seleccionar: 1. Registrar nuevo tutor

ID del tutor: T004
Nombre completo: Dr. Roberto Sánchez
Asignatura: Química
```

### 4.2 Configurar tu Disponibilidad

#### Registrar Horarios
```
Seleccionar opción: 1. Gestión de Tutores
Seleccionar: 2. Registrar disponibilidad de tutor

ID del tutor: T004
Día: Lunes
Hora inicio: 10:00
Hora fin: 11:00
Modalidad: Presencial
```

#### Recomendaciones
- Registra todos tus horarios disponibles semanalmente
- Considera tu carga académica antes de definir disponibilidad
- Actualiza tu disponibilidad si hay cambios

### 4.3 Recibir Notificaciones de Tutorías

Cuando un estudiante reserva una tutoría contigo:
```
📧 Notificación enviada a [tutor]
✅ Tutoría confirmada: Miércoles a las 14:00

Detalles:
- Estudiante: Ana Torres (E001)
- Asignatura: Cálculo
- Modalidad: Virtual
- Enlace: https://meet.epn.edu.ec/TUT-0001
```

### 4.4 Registrar Información Post-Tutoría

Este paso es **FUNDAMENTAL** para el seguimiento académico del estudiante.

#### Proceso de Registro
```
Seleccionar opción: 4. Registrar Sesión de Tutoría
ID de la tutoría: TUT-0001

--- REGISTRO POST-TUTORÍA ---
Temas tratados: Derivadas parciales, regla de la cadena
Nivel de avance: Alto
Observaciones: Buen dominio de conceptos básicos
Recomendaciones: Practicar ejercicios 15-20 del libro
```

#### Guía para Evaluar Nivel de Avance

- **Alto**: El estudiante comprende >80% de los conceptos
- **Medio**: El estudiante comprende 50-80% de los conceptos
- **Bajo**: El estudiante comprende <50% de los conceptos

#### Importancia del Registro

El registro post-tutoría permite:
- Seguimiento continuo del progreso del estudiante
- Identificación temprana de dificultades académicas
- Continuidad entre sesiones de tutoría
- Evidencia institucional del apoyo brindado

### 4.5 Ver tus Tutorías Programadas

```
Seleccionar opción: 7. Ver Tutores y Disponibilidad
```

Verás:
- Tus horarios aún disponibles
- Tutorías ya reservadas (marcadas como no disponibles)

---

## 5. Guía para Coordinadores Académicos

### 5.1 Generar Reportes Generales

```
Seleccionar opción: 6. Generar Reporte General
```

#### Información del Reporte
```
=============================================================
REPORTE GENERAL DEL SISTEMA
=============================================================
Total de tutorías: 45
Tutorías completadas: 38
Tutorías reservadas: 7
Tutores activos: 12
Estudiantes registrados: 156
=============================================================
```

### 5.2 Identificar Estudiantes en Riesgo

Los coordinadores pueden:
1. Consultar historiales de estudiantes específicos
2. Identificar estudiantes con "Nivel de avance: Bajo" recurrente
3. Ver recomendaciones de múltiples tutores
4. Tomar acciones preventivas basadas en datos

### 5.3 Evaluar Efectividad del Sistema

**Métricas Clave:**
- Tasa de utilización de tutorías
- Distribución de tutorías por asignatura
- Estudiantes con seguimiento continuo
- Mejora en indicadores académicos

---

## 6. Preguntas Frecuentes

### Para Estudiantes

**P: ¿Puedo reservar varias tutorías a la vez?**  
R: Sí, pero asegúrate de que no se crucen en horario. El sistema te permitirá reservar múltiples sesiones con diferentes tutores.

**P: ¿Qué hago si no veo horarios disponibles?**  
R: Intenta con otro tutor de la misma asignatura, o espera a que los tutores actualicen su disponibilidad.

**P: ¿Cómo cancelo una tutoría?**  
R: Contacta directamente al tutor o a coordinación académica con al menos 24 horas de anticipación.

**P: ¿Puedo ver las recomendaciones que me dio el tutor?**  
R: Sí, consulta tu historial (opción 5) donde encontrarás todas las recomendaciones.

### Para Tutores

**P: ¿Qué pasa si no puedo atender una tutoría reservada?**  
R: Contacta inmediatamente al estudiante y a coordinación académica para reprogramar.

**P: ¿Cuándo debo registrar la información post-tutoría?**  
R: Idealmente inmediatamente después de cada sesión, máximo 24 horas después.

**P: ¿Puedo cambiar mi disponibilidad?**  
R: Sí, pero ten en cuenta las tutorías ya reservadas que debes honrar.

### Técnicas

**P: ¿Qué navegador debo usar?**  
R: En esta versión prototipo se ejecuta desde terminal. La versión web futura será compatible con Chrome, Firefox, Safari y Edge.

**P: ¿Funciona en dispositivos móviles?**  
R: La versión prototipo es de escritorio. La versión web futura será responsive.

---

## 7. Solución de Problemas

### Problema: No aparecen tutores disponibles

**Causa**: Los tutores no han registrado disponibilidad  
**Solución**: 
1. Verifica que buscas la asignatura correcta
2. Contacta a coordinación académica
3. Intenta en diferentes días/horarios

### Problema: El sistema no acepta mi ID

**Causa**: ID no registrado en el sistema  
**Solución**:
1. Verifica que tu ID sea correcto
2. Si eres nuevo, regístrate primero (opción 2)
3. Contacta a soporte técnico

### Problema: No recibí la notificación

**Causa**: Correo institucional con problemas  
**Solución**:
1. Revisa tu carpeta de spam
2. Verifica tu correo institucional
3. La confirmación también aparece en pantalla

### Problema: Error al generar diagramas

**Causa**: Falta instalar matplotlib  
**Solución**:
```bash
pip install matplotlib
```

---

## 📞 Soporte Técnico

### Canales de Ayuda

**Para problemas técnicos:**
- Email: soporte.tutorias@epn.edu.ec
- Extensión: 1234

**Para consultas académicas:**
- Email: coordinacion.academica@epn.edu.ec
- Extensión: 5678

**Horario de atención:**
- Lunes a Viernes: 8:00 - 18:00
- Sábados: 8:00 - 12:00

---

## 📝 Consejos Finales

### Para Estudiantes
1. 🎯 **Sé específico**: Prepara preguntas concretas antes de la tutoría
2. 📚 **Estudia antes**: Revisa el material por tu cuenta primero
3. 📝 **Toma notas**: Durante la tutoría anota conceptos importantes
4. 🔄 **Aplica recomendaciones**: Sigue las sugerencias del tutor

### Para Tutores
1. 🕒 **Puntualidad**: Respeta los horarios acordados
2. 📋 **Prepárate**: Revisa el historial del estudiante antes
3. 🎓 **Personaliza**: Adapta tu explicación al nivel del estudiante
4. 📊 **Registra siempre**: El registro es fundamental para el seguimiento

### Para Coordinadores
1. 📈 **Monitorea**: Revisa reportes periódicamente
2. 🎯 **Actúa**: Identifica y apoya estudiantes en riesgo
3. 💡 **Mejora**: Usa datos para optimizar el proceso
4. 🤝 **Comunica**: Mantén informados a tutores y estudiantes

---

**Versión del Manual:** 1.0.0  
**Última actualización:** 14 de enero de 2026  
**Sistema:** Gestión de Tutorías Académicas - EPN
