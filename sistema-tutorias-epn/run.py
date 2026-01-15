"""
Punto de entrada para ejecutar la aplicación Flask
"""
from app import create_app

app = create_app()

if __name__ == '__main__':
    print("\n" + "="*60)
    print("Sistema de Gestión de Tutorías Académicas - EPN")
    print("="*60)
    print("\n🚀 Servidor iniciando...")
    print("📍 URL: http://localhost:5000")
    print("📍 URL: http://127.0.0.1:5000")
    print("\n⚠️  Presiona CTRL+C para detener el servidor\n")
    print("="*60 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
