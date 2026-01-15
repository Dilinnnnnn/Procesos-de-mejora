"""
Modelos de la base de datos para el Sistema de Tutorías
"""
from datetime import datetime
from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(UserMixin, db.Model):
    """Modelo de Usuario (Estudiante, Tutor, Coordinador)"""
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    cedula = db.Column(db.String(10), unique=True, nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    tipo = db.Column(db.String(20), nullable=False)  # estudiante, tutor, coordinador
    activo = db.Column(db.Boolean, default=True)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relaciones
    tutorias_como_estudiante = db.relationship('Tutoria', backref='estudiante', 
                                                foreign_keys='Tutoria.estudiante_id',
                                                lazy='dynamic')
    tutorias_como_tutor = db.relationship('Tutoria', backref='tutor',
                                          foreign_keys='Tutoria.tutor_id',
                                          lazy='dynamic')
    disponibilidades = db.relationship('Disponibilidad', backref='tutor', lazy='dynamic')
    
    def set_password(self, password):
        """Establece el hash de la contraseña"""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Verifica la contraseña"""
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<Usuario {self.nombre} - {self.tipo}>'


class Asignatura(db.Model):
    """Modelo de Asignatura"""
    __tablename__ = 'asignaturas'
    
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(20), unique=True, nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)
    activa = db.Column(db.Boolean, default=True)
    
    # Relaciones
    disponibilidades = db.relationship('Disponibilidad', backref='asignatura', lazy='dynamic')
    tutorias = db.relationship('Tutoria', backref='asignatura', lazy='dynamic')
    
    def __repr__(self):
        return f'<Asignatura {self.codigo} - {self.nombre}>'


class Disponibilidad(db.Model):
    """Modelo de Disponibilidad del Tutor"""
    __tablename__ = 'disponibilidades'
    
    id = db.Column(db.Integer, primary_key=True)
    tutor_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    asignatura_id = db.Column(db.Integer, db.ForeignKey('asignaturas.id'), nullable=False)
    dia_semana = db.Column(db.Integer, nullable=False)  # 0=Lunes, 6=Domingo
    hora_inicio = db.Column(db.String(5), nullable=False)  # Formato HH:MM
    hora_fin = db.Column(db.String(5), nullable=False)
    modalidad = db.Column(db.String(20), nullable=False)  # presencial, virtual
    ubicacion = db.Column(db.String(100))  # Aula o enlace de meet
    activa = db.Column(db.Boolean, default=True)
    
    def __repr__(self):
        dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        return f'<Disponibilidad {dias[self.dia_semana]} {self.hora_inicio}-{self.hora_fin}>'


class Tutoria(db.Model):
    """Modelo de Tutoría"""
    __tablename__ = 'tutorias'
    
    id = db.Column(db.Integer, primary_key=True)
    estudiante_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    tutor_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    asignatura_id = db.Column(db.Integer, db.ForeignKey('asignaturas.id'), nullable=False)
    
    fecha = db.Column(db.Date, nullable=False)
    hora_inicio = db.Column(db.String(5), nullable=False)
    hora_fin = db.Column(db.String(5), nullable=False)
    modalidad = db.Column(db.String(20), nullable=False)
    ubicacion = db.Column(db.String(100))
    
    estado = db.Column(db.String(20), default='programada')  # programada, realizada, cancelada
    
    # Información del registro (se completa después de la tutoría)
    temas_tratados = db.Column(db.Text)
    nivel_avance = db.Column(db.String(20))  # excelente, bueno, regular, necesita_refuerzo
    observaciones = db.Column(db.Text)
    recomendaciones = db.Column(db.Text)
    
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_registro = db.Column(db.DateTime)  # Cuando el tutor registra el resultado
    
    def __repr__(self):
        return f'<Tutoria {self.fecha} {self.hora_inicio} - Estado: {self.estado}>'
