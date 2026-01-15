"""
Sistema de Gestión de Tutorías Académicas - EPN
Aplicación Flask
"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    """Crea y configura la aplicación Flask"""
    # Obtener la ruta del directorio donde está run.py (raíz del proyecto)
    basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    app = Flask(__name__, 
                template_folder=os.path.join(basedir, 'templates'),
                static_folder=os.path.join(basedir, 'static'))
    
    # Configuración
    app.config['SECRET_KEY'] = 'epn-tutorias-2026-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "data", "tutorias.db")}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Inicializar extensiones
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'
    login_manager.login_message = 'Por favor, inicia sesión para acceder a esta página.'
    
    # Registrar blueprints
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    # Crear tablas de la base de datos
    with app.app_context():
        db.create_all()
        # Inicializar datos de prueba
        from app.utils import inicializar_datos_prueba
        inicializar_datos_prueba()
    
    return app
