"""
Rutas y controladores de la aplicación
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from datetime import datetime, date, timedelta
from app import db, login_manager
from app.models import Usuario, Asignatura, Disponibilidad, Tutoria

main_bp = Blueprint('main', __name__)

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))


# ==================== RUTAS GENERALES ====================

@main_bp.route('/')
def index():
    """Página principal"""
    return render_template('index.html')


@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Inicio de sesión"""
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    
    if request.method == 'POST':
        cedula = request.form.get('cedula')
        password = request.form.get('password')
        
        usuario = Usuario.query.filter_by(cedula=cedula).first()
        
        if usuario and usuario.check_password(password):
            login_user(usuario)
            flash(f'¡Bienvenido, {usuario.nombre}!', 'success')
            return redirect(url_for('main.dashboard'))
        else:
            flash('Cédula o contraseña incorrectos', 'danger')
    
    return render_template('login.html')


@main_bp.route('/logout')
@login_required
def logout():
    """Cerrar sesión"""
    logout_user()
    flash('Has cerrado sesión exitosamente', 'info')
    return redirect(url_for('main.index'))


@main_bp.route('/dashboard')
@login_required
def dashboard():
    """Dashboard según el tipo de usuario"""
    if current_user.tipo == 'estudiante':
        return redirect(url_for('main.estudiante_dashboard'))
    elif current_user.tipo == 'tutor':
        return redirect(url_for('main.tutor_dashboard'))
    elif current_user.tipo == 'coordinador':
        return redirect(url_for('main.coordinador_dashboard'))
    else:
        return redirect(url_for('main.index'))


# ==================== RUTAS ESTUDIANTE ====================

@main_bp.route('/estudiante/dashboard')
@login_required
def estudiante_dashboard():
    """Dashboard del estudiante"""
    if current_user.tipo != 'estudiante':
        flash('No tienes permiso para acceder a esta página', 'danger')
        return redirect(url_for('main.dashboard'))
    
    # Obtener tutorías programadas
    tutorias_programadas = Tutoria.query.filter_by(
        estudiante_id=current_user.id,
        estado='programada'
    ).filter(Tutoria.fecha >= date.today()).order_by(Tutoria.fecha, Tutoria.hora_inicio).all()
    
    # Obtener últimas tutorías realizadas
    tutorias_realizadas = Tutoria.query.filter_by(
        estudiante_id=current_user.id,
        estado='realizada'
    ).order_by(Tutoria.fecha.desc()).limit(5).all()
    
    return render_template('estudiante/dashboard.html',
                         tutorias_programadas=tutorias_programadas,
                         tutorias_realizadas=tutorias_realizadas)


@main_bp.route('/estudiante/solicitar-tutoria', methods=['GET', 'POST'])
@login_required
def solicitar_tutoria():
    """Solicitar nueva tutoría"""
    if current_user.tipo != 'estudiante':
        flash('No tienes permiso para acceder a esta página', 'danger')
        return redirect(url_for('main.dashboard'))
    
    asignaturas = Asignatura.query.filter_by(activa=True).all()
    
    if request.method == 'POST':
        asignatura_id = request.form.get('asignatura_id')
        tutor_id = request.form.get('tutor_id')
        fecha = request.form.get('fecha')
        hora_inicio = request.form.get('hora_inicio')
        hora_fin = request.form.get('hora_fin')
        
        # Obtener disponibilidad para la ubicación y modalidad
        disponibilidad = Disponibilidad.query.filter_by(
            tutor_id=tutor_id,
            asignatura_id=asignatura_id
        ).first()
        
        # Crear nueva tutoría
        nueva_tutoria = Tutoria(
            estudiante_id=current_user.id,
            tutor_id=tutor_id,
            asignatura_id=asignatura_id,
            fecha=datetime.strptime(fecha, '%Y-%m-%d').date(),
            hora_inicio=hora_inicio,
            hora_fin=hora_fin,
            modalidad=disponibilidad.modalidad if disponibilidad else 'presencial',
            ubicacion=disponibilidad.ubicacion if disponibilidad else 'Por definir',
            estado='programada'
        )
        
        db.session.add(nueva_tutoria)
        db.session.commit()
        
        flash('¡Tutoría programada exitosamente!', 'success')
        return redirect(url_for('main.estudiante_dashboard'))
    
    return render_template('estudiante/solicitar_tutoria.html', asignaturas=asignaturas)


@main_bp.route('/estudiante/historial')
@login_required
def estudiante_historial():
    """Ver historial de tutorías"""
    if current_user.tipo != 'estudiante':
        flash('No tienes permiso para acceder a esta página', 'danger')
        return redirect(url_for('main.dashboard'))
    
    tutorias = Tutoria.query.filter_by(estudiante_id=current_user.id).order_by(
        Tutoria.fecha.desc(), Tutoria.hora_inicio.desc()
    ).all()
    
    return render_template('estudiante/historial.html', tutorias=tutorias)


# ==================== RUTAS TUTOR ====================

@main_bp.route('/tutor/dashboard')
@login_required
def tutor_dashboard():
    """Dashboard del tutor"""
    if current_user.tipo != 'tutor':
        flash('No tienes permiso para acceder a esta página', 'danger')
        return redirect(url_for('main.dashboard'))
    
    # Tutorías de hoy
    tutorias_hoy = Tutoria.query.filter_by(
        tutor_id=current_user.id,
        fecha=date.today(),
        estado='programada'
    ).order_by(Tutoria.hora_inicio).all()
    
    # Próximas tutorías
    tutorias_proximas = Tutoria.query.filter_by(
        tutor_id=current_user.id,
        estado='programada'
    ).filter(Tutoria.fecha > date.today()).order_by(
        Tutoria.fecha, Tutoria.hora_inicio
    ).limit(5).all()
    
    # Tutorías pendientes de registro
    tutorias_pendientes = Tutoria.query.filter_by(
        tutor_id=current_user.id,
        estado='programada'
    ).filter(Tutoria.fecha < date.today()).all()
    
    return render_template('tutor/dashboard.html',
                         tutorias_hoy=tutorias_hoy,
                         tutorias_proximas=tutorias_proximas,
                         tutorias_pendientes=tutorias_pendientes)


@main_bp.route('/tutor/disponibilidad', methods=['GET', 'POST'])
@login_required
def tutor_disponibilidad():
    """Gestionar disponibilidad"""
    if current_user.tipo != 'tutor':
        flash('No tienes permiso para acceder a esta página', 'danger')
        return redirect(url_for('main.dashboard'))
    
    if request.method == 'POST':
        asignatura_id = request.form.get('asignatura_id')
        dia_semana = int(request.form.get('dia_semana'))
        hora_inicio = request.form.get('hora_inicio')
        hora_fin = request.form.get('hora_fin')
        modalidad = request.form.get('modalidad')
        ubicacion = request.form.get('ubicacion')
        
        nueva_disponibilidad = Disponibilidad(
            tutor_id=current_user.id,
            asignatura_id=asignatura_id,
            dia_semana=dia_semana,
            hora_inicio=hora_inicio,
            hora_fin=hora_fin,
            modalidad=modalidad,
            ubicacion=ubicacion
        )
        
        db.session.add(nueva_disponibilidad)
        db.session.commit()
        
        flash('Disponibilidad agregada exitosamente', 'success')
        return redirect(url_for('main.tutor_disponibilidad'))
    
    disponibilidades = Disponibilidad.query.filter_by(
        tutor_id=current_user.id, activa=True
    ).all()
    
    asignaturas = Asignatura.query.filter_by(activa=True).all()
    
    return render_template('tutor/disponibilidad.html',
                         disponibilidades=disponibilidades,
                         asignaturas=asignaturas)


@main_bp.route('/tutor/registrar-tutoria/<int:tutoria_id>', methods=['GET', 'POST'])
@login_required
def registrar_tutoria(tutoria_id):
    """Registrar resultado de tutoría"""
    if current_user.tipo != 'tutor':
        flash('No tienes permiso para acceder a esta página', 'danger')
        return redirect(url_for('main.dashboard'))
    
    tutoria = Tutoria.query.get_or_404(tutoria_id)
    
    if tutoria.tutor_id != current_user.id:
        flash('No tienes permiso para registrar esta tutoría', 'danger')
        return redirect(url_for('main.tutor_dashboard'))
    
    if request.method == 'POST':
        tutoria.temas_tratados = request.form.get('temas_tratados')
        tutoria.nivel_avance = request.form.get('nivel_avance')
        tutoria.observaciones = request.form.get('observaciones')
        tutoria.recomendaciones = request.form.get('recomendaciones')
        tutoria.estado = 'realizada'
        tutoria.fecha_registro = datetime.utcnow()
        
        db.session.commit()
        
        flash('Tutoría registrada exitosamente', 'success')
        return redirect(url_for('main.tutor_dashboard'))
    
    return render_template('tutor/registrar_tutoria.html', tutoria=tutoria)


# ==================== RUTAS COORDINADOR ====================

@main_bp.route('/coordinador/dashboard')
@login_required
def coordinador_dashboard():
    """Dashboard del coordinador"""
    if current_user.tipo != 'coordinador':
        flash('No tienes permiso para acceder a esta página', 'danger')
        return redirect(url_for('main.dashboard'))
    
    # Estadísticas generales
    total_estudiantes = Usuario.query.filter_by(tipo='estudiante', activo=True).count()
    total_tutores = Usuario.query.filter_by(tipo='tutor', activo=True).count()
    total_tutorias = Tutoria.query.count()
    tutorias_mes = Tutoria.query.filter(
        Tutoria.fecha >= date.today().replace(day=1)
    ).count()
    
    # Tutorías recientes
    tutorias_recientes = Tutoria.query.order_by(
        Tutoria.fecha.desc(), Tutoria.hora_inicio.desc()
    ).limit(10).all()
    
    return render_template('coordinador/dashboard.html',
                         total_estudiantes=total_estudiantes,
                         total_tutores=total_tutores,
                         total_tutorias=total_tutorias,
                         tutorias_mes=tutorias_mes,
                         tutorias_recientes=tutorias_recientes)


@main_bp.route('/coordinador/reportes')
@login_required
def coordinador_reportes():
    """Ver reportes y estadísticas"""
    if current_user.tipo != 'coordinador':
        flash('No tienes permiso para acceder a esta página', 'danger')
        return redirect(url_for('main.dashboard'))
    
    # Tutorías por asignatura
    asignaturas = Asignatura.query.all()
    datos_asignaturas = []
    for asignatura in asignaturas:
        total = Tutoria.query.filter_by(asignatura_id=asignatura.id).count()
        datos_asignaturas.append({
            'nombre': asignatura.nombre,
            'total': total
        })
    
    # Tutorías por estado
    programadas = Tutoria.query.filter_by(estado='programada').count()
    realizadas = Tutoria.query.filter_by(estado='realizada').count()
    canceladas = Tutoria.query.filter_by(estado='cancelada').count()
    
    return render_template('coordinador/reportes.html',
                         datos_asignaturas=datos_asignaturas,
                         programadas=programadas,
                         realizadas=realizadas,
                         canceladas=canceladas)


# ==================== API ENDPOINTS ====================

@main_bp.route('/api/tutores-por-asignatura/<int:asignatura_id>')
@login_required
def api_tutores_asignatura(asignatura_id):
    """Obtener tutores disponibles para una asignatura"""
    disponibilidades = Disponibilidad.query.filter_by(
        asignatura_id=asignatura_id, activa=True
    ).all()
    
    tutores = {}
    for disp in disponibilidades:
        if disp.tutor_id not in tutores:
            tutores[disp.tutor_id] = {
                'id': disp.tutor.id,
                'nombre': disp.tutor.nombre,
                'email': disp.tutor.email
            }
    
    return jsonify(list(tutores.values()))


@main_bp.route('/api/disponibilidad-tutor/<int:tutor_id>/<int:asignatura_id>')
@login_required
def api_disponibilidad_tutor(tutor_id, asignatura_id):
    """Obtener disponibilidad de un tutor para una asignatura"""
    disponibilidades = Disponibilidad.query.filter_by(
        tutor_id=tutor_id,
        asignatura_id=asignatura_id,
        activa=True
    ).all()
    
    dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    
    datos = []
    for disp in disponibilidades:
        datos.append({
            'id': disp.id,
            'dia': dias[disp.dia_semana],
            'dia_num': disp.dia_semana,
            'hora_inicio': disp.hora_inicio,
            'hora_fin': disp.hora_fin,
            'modalidad': disp.modalidad,
            'ubicacion': disp.ubicacion
        })
    
    return jsonify(datos)


@main_bp.route('/api/eliminar-disponibilidad/<int:disp_id>', methods=['POST'])
@login_required
def api_eliminar_disponibilidad(disp_id):
    """Eliminar una disponibilidad"""
    if current_user.tipo != 'tutor':
        return jsonify({'error': 'No autorizado'}), 403
    
    disponibilidad = Disponibilidad.query.get_or_404(disp_id)
    
    if disponibilidad.tutor_id != current_user.id:
        return jsonify({'error': 'No autorizado'}), 403
    
    disponibilidad.activa = False
    db.session.commit()
    
    return jsonify({'success': True})


@main_bp.route('/api/cancelar-tutoria/<int:tutoria_id>', methods=['POST'])
@login_required
def api_cancelar_tutoria(tutoria_id):
    """Cancelar una tutoría"""
    tutoria = Tutoria.query.get_or_404(tutoria_id)
    
    # Verificar permisos
    if current_user.id != tutoria.estudiante_id and current_user.id != tutoria.tutor_id:
        return jsonify({'error': 'No autorizado'}), 403
    
    tutoria.estado = 'cancelada'
    db.session.commit()
    
    return jsonify({'success': True})
