"""
Funciones utilitarias
"""
from datetime import datetime, date, timedelta
from app import db
from app.models import Usuario, Asignatura, Disponibilidad, Tutoria


def inicializar_datos_prueba():
    """Inicializa la base de datos con datos de prueba"""
    
    # Verificar si ya hay datos
    if Usuario.query.count() > 0:
        return
    
    print("Inicializando datos de prueba...")
    
    # Crear asignaturas
    asignaturas = [
        Asignatura(codigo='CALC-101', nombre='Cálculo Diferencial', 
                  descripcion='Introducción al cálculo diferencial'),
        Asignatura(codigo='PROG-201', nombre='Programación Avanzada',
                  descripcion='Programación orientada a objetos'),
        Asignatura(codigo='FIS-101', nombre='Física I',
                  descripcion='Mecánica clásica'),
        Asignatura(codigo='ALG-101', nombre='Álgebra Lineal',
                  descripcion='Espacios vectoriales y transformaciones lineales'),
        Asignatura(codigo='QUIM-101', nombre='Química General',
                  descripcion='Fundamentos de química'),
    ]
    
    for asig in asignaturas:
        db.session.add(asig)
    db.session.commit()
    
    # Crear usuarios
    # Coordinador
    coordinador = Usuario(
        cedula='1700000001',
        nombre='Dr. Carlos Mendoza',
        email='carlos.mendoza@epn.edu.ec',
        tipo='coordinador'
    )
    coordinador.set_password('coord123')
    db.session.add(coordinador)
    
    # Tutores
    tutores_data = [
        {'cedula': '1700000002', 'nombre': 'Ing. María García', 'email': 'maria.garcia@epn.edu.ec'},
        {'cedula': '1700000003', 'nombre': 'Ing. Juan Pérez', 'email': 'juan.perez@epn.edu.ec'},
        {'cedula': '1700000004', 'nombre': 'Ing. Ana Rodríguez', 'email': 'ana.rodriguez@epn.edu.ec'},
        {'cedula': '1700000005', 'nombre': 'Ing. Luis Torres', 'email': 'luis.torres@epn.edu.ec'},
    ]
    
    tutores = []
    for t_data in tutores_data:
        tutor = Usuario(
            cedula=t_data['cedula'],
            nombre=t_data['nombre'],
            email=t_data['email'],
            tipo='tutor'
        )
        tutor.set_password('tutor123')
        db.session.add(tutor)
        tutores.append(tutor)
    
    # Estudiantes
    estudiantes_data = [
        {'cedula': '1750000001', 'nombre': 'Pedro Sánchez', 'email': 'pedro.sanchez@epn.edu.ec'},
        {'cedula': '1750000002', 'nombre': 'Laura Martínez', 'email': 'laura.martinez@epn.edu.ec'},
        {'cedula': '1750000003', 'nombre': 'Diego Ramírez', 'email': 'diego.ramirez@epn.edu.ec'},
        {'cedula': '1750000004', 'nombre': 'Sofía Morales', 'email': 'sofia.morales@epn.edu.ec'},
        {'cedula': '1750000005', 'nombre': 'Andrés Castro', 'email': 'andres.castro@epn.edu.ec'},
    ]
    
    estudiantes = []
    for e_data in estudiantes_data:
        estudiante = Usuario(
            cedula=e_data['cedula'],
            nombre=e_data['nombre'],
            email=e_data['email'],
            tipo='estudiante'
        )
        estudiante.set_password('est123')
        db.session.add(estudiante)
        estudiantes.append(estudiante)
    
    db.session.commit()
    
    # Crear disponibilidades para tutores
    disponibilidades_data = [
        # María García - Cálculo y Álgebra
        {'tutor': tutores[0], 'asignatura': asignaturas[0], 'dia': 0, 'inicio': '09:00', 'fin': '11:00', 
         'modalidad': 'presencial', 'ubicacion': 'Aula 201'},
        {'tutor': tutores[0], 'asignatura': asignaturas[0], 'dia': 2, 'inicio': '14:00', 'fin': '16:00',
         'modalidad': 'virtual', 'ubicacion': 'https://meet.google.com/abc-defg-hij'},
        {'tutor': tutores[0], 'asignatura': asignaturas[3], 'dia': 3, 'inicio': '10:00', 'fin': '12:00',
         'modalidad': 'presencial', 'ubicacion': 'Aula 305'},
        
        # Juan Pérez - Programación
        {'tutor': tutores[1], 'asignatura': asignaturas[1], 'dia': 1, 'inicio': '08:00', 'fin': '10:00',
         'modalidad': 'presencial', 'ubicacion': 'Laboratorio 102'},
        {'tutor': tutores[1], 'asignatura': asignaturas[1], 'dia': 4, 'inicio': '15:00', 'fin': '17:00',
         'modalidad': 'virtual', 'ubicacion': 'https://meet.google.com/xyz-abcd-efg'},
        
        # Ana Rodríguez - Física
        {'tutor': tutores[2], 'asignatura': asignaturas[2], 'dia': 0, 'inicio': '14:00', 'fin': '16:00',
         'modalidad': 'presencial', 'ubicacion': 'Lab. Física 1'},
        {'tutor': tutores[2], 'asignatura': asignaturas[2], 'dia': 3, 'inicio': '09:00', 'fin': '11:00',
         'modalidad': 'virtual', 'ubicacion': 'https://meet.google.com/fis-1234-xyz'},
        
        # Luis Torres - Química
        {'tutor': tutores[3], 'asignatura': asignaturas[4], 'dia': 2, 'inicio': '10:00', 'fin': '12:00',
         'modalidad': 'presencial', 'ubicacion': 'Lab. Química A'},
        {'tutor': tutores[3], 'asignatura': asignaturas[4], 'dia': 4, 'inicio': '13:00', 'fin': '15:00',
         'modalidad': 'presencial', 'ubicacion': 'Lab. Química B'},
    ]
    
    for disp_data in disponibilidades_data:
        disp = Disponibilidad(
            tutor_id=disp_data['tutor'].id,
            asignatura_id=disp_data['asignatura'].id,
            dia_semana=disp_data['dia'],
            hora_inicio=disp_data['inicio'],
            hora_fin=disp_data['fin'],
            modalidad=disp_data['modalidad'],
            ubicacion=disp_data['ubicacion']
        )
        db.session.add(disp)
    
    db.session.commit()
    
    # Crear algunas tutorías de ejemplo
    hoy = date.today()
    
    # Tutorías pasadas (realizadas)
    tutorias_pasadas = [
        {
            'estudiante': estudiantes[0], 'tutor': tutores[0], 'asignatura': asignaturas[0],
            'fecha': hoy - timedelta(days=7), 'inicio': '09:00', 'fin': '10:30',
            'modalidad': 'presencial', 'ubicacion': 'Aula 201',
            'estado': 'realizada', 'temas': 'Derivadas y límites',
            'nivel': 'bueno', 'observaciones': 'Buen dominio de límites, practicar más derivadas',
            'recomendaciones': 'Resolver ejercicios del capítulo 3'
        },
        {
            'estudiante': estudiantes[1], 'tutor': tutores[1], 'asignatura': asignaturas[1],
            'fecha': hoy - timedelta(days=5), 'inicio': '15:00', 'fin': '16:30',
            'modalidad': 'virtual', 'ubicacion': 'https://meet.google.com/xyz-abcd-efg',
            'estado': 'realizada', 'temas': 'Programación orientada a objetos',
            'nivel': 'excelente', 'observaciones': 'Excelente comprensión de los conceptos',
            'recomendaciones': 'Continuar con patrones de diseño'
        },
    ]
    
    for tut_data in tutorias_pasadas:
        tut = Tutoria(
            estudiante_id=tut_data['estudiante'].id,
            tutor_id=tut_data['tutor'].id,
            asignatura_id=tut_data['asignatura'].id,
            fecha=tut_data['fecha'],
            hora_inicio=tut_data['inicio'],
            hora_fin=tut_data['fin'],
            modalidad=tut_data['modalidad'],
            ubicacion=tut_data['ubicacion'],
            estado=tut_data['estado'],
            temas_tratados=tut_data['temas'],
            nivel_avance=tut_data['nivel'],
            observaciones=tut_data['observaciones'],
            recomendaciones=tut_data['recomendaciones'],
            fecha_registro=datetime.utcnow()
        )
        db.session.add(tut)
    
    # Tutorías futuras (programadas)
    tutorias_futuras = [
        {
            'estudiante': estudiantes[0], 'tutor': tutores[0], 'asignatura': asignaturas[0],
            'fecha': hoy + timedelta(days=2), 'inicio': '09:00', 'fin': '10:30',
            'modalidad': 'presencial', 'ubicacion': 'Aula 201'
        },
        {
            'estudiante': estudiantes[2], 'tutor': tutores[2], 'asignatura': asignaturas[2],
            'fecha': hoy + timedelta(days=3), 'inicio': '14:00', 'fin': '15:30',
            'modalidad': 'presencial', 'ubicacion': 'Lab. Física 1'
        },
        {
            'estudiante': estudiantes[3], 'tutor': tutores[1], 'asignatura': asignaturas[1],
            'fecha': hoy + timedelta(days=4), 'inicio': '08:00', 'fin': '09:30',
            'modalidad': 'presencial', 'ubicacion': 'Laboratorio 102'
        },
    ]
    
    for tut_data in tutorias_futuras:
        tut = Tutoria(
            estudiante_id=tut_data['estudiante'].id,
            tutor_id=tut_data['tutor'].id,
            asignatura_id=tut_data['asignatura'].id,
            fecha=tut_data['fecha'],
            hora_inicio=tut_data['inicio'],
            hora_fin=tut_data['fin'],
            modalidad=tut_data['modalidad'],
            ubicacion=tut_data['ubicacion'],
            estado='programada'
        )
        db.session.add(tut)
    
    db.session.commit()
    
    print("✓ Datos de prueba inicializados exitosamente")
    print("\n=== CREDENCIALES DE ACCESO ===")
    print("\nCoordinador:")
    print("  Cédula: 1700000001")
    print("  Password: coord123")
    print("\nTutor (ejemplo):")
    print("  Cédula: 1700000002")
    print("  Password: tutor123")
    print("\nEstudiante (ejemplo):")
    print("  Cédula: 1750000001")
    print("  Password: est123")
    print("\n==============================\n")
