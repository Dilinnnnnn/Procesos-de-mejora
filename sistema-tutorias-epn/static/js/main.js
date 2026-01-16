// JavaScript para el Sistema de Gestión de Tutorías EPN

// Sistema de Tema Oscuro/Claro
function initTheme() {
    const htmlElement = document.documentElement;
    const themeToggle = document.getElementById('themeToggle');
    
    // Obtener el tema guardado o usar el preferido del sistema
    const savedTheme = localStorage.getItem('theme');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    const initialTheme = savedTheme || (prefersDark ? 'dark' : 'light');
    
    // Aplicar tema inicial
    setTheme(initialTheme);
    
    // Event listener para el botón de cambio de tema
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            const currentTheme = localStorage.getItem('theme') || 'light';
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            setTheme(newTheme);
        });
    }
}

function setTheme(theme) {
    const htmlElement = document.documentElement;
    const themeToggle = document.getElementById('themeToggle');
    
    if (theme === 'dark') {
        htmlElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark');
        if (themeToggle) {
            themeToggle.innerHTML = '<i class="bi bi-sun-fill"></i>';
            themeToggle.title = 'Modo claro';
        }
    } else {
        htmlElement.removeAttribute('data-theme');
        localStorage.setItem('theme', 'light');
        if (themeToggle) {
            themeToggle.innerHTML = '<i class="bi bi-moon-fill"></i>';
            themeToggle.title = 'Modo oscuro';
        }
    }
}

document.addEventListener('DOMContentLoaded', function() {
    // Inicializar tema
    initTheme();
    
    // Inicializar tooltips de Bootstrap
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Inicializar popovers de Bootstrap
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Auto-cerrar alertas después de 5 segundos (excepto las que contienen disponibilidad o están en modales)
    const alerts = document.querySelectorAll('.alert:not(.alert-permanent):not(#disponibilidadContent):not(.modal .alert)');
    alerts.forEach(alert => {
        setTimeout(() => {
            // Verificar que el elemento aún exista en el DOM y no esté dentro de un modal
            if (document.contains(alert) && !alert.closest('.modal')) {
                const bsAlert = new bootstrap.Alert(alert);
                bsAlert.close();
            }
        }, 5000);
    });

    // Animación de fade-in para elementos
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.card, .list-group-item').forEach(el => {
        observer.observe(el);
    });
});

// Función para confirmar acciones destructivas
function confirmarAccion(mensaje) {
    return confirm(mensaje || '¿Estás seguro de que deseas realizar esta acción?');
}

// Función para mostrar spinner de carga
function mostrarCargando(elemento) {
    if (typeof elemento === 'string') {
        elemento = document.querySelector(elemento);
    }
    if (elemento) {
        elemento.innerHTML = '<div class="text-center"><div class="spinner-border text-primary" role="status"><span class="visually-hidden">Cargando...</span></div></div>';
    }
}

// Función para formatear fechas
function formatearFecha(fecha) {
    const opciones = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(fecha).toLocaleDateString('es-ES', opciones);
}

// Función para validar formularios
function validarFormulario(formId) {
    const form = document.getElementById(formId);
    if (!form) return false;

    const inputs = form.querySelectorAll('input[required], select[required], textarea[required]');
    let valido = true;

    inputs.forEach(input => {
        if (!input.value.trim()) {
            input.classList.add('is-invalid');
            valido = false;
        } else {
            input.classList.remove('is-invalid');
            input.classList.add('is-valid');
        }
    });

    return valido;
}

// Función para limpiar validaciones
function limpiarValidaciones(formId) {
    const form = document.getElementById(formId);
    if (!form) return;

    const inputs = form.querySelectorAll('.is-invalid, .is-valid');
    inputs.forEach(input => {
        input.classList.remove('is-invalid', 'is-valid');
    });
}

// Función para mostrar notificaciones
function mostrarNotificacion(mensaje, tipo = 'info') {
    const alertContainer = document.createElement('div');
    alertContainer.className = `alert alert-${tipo} alert-dismissible fade show position-fixed top-0 end-0 m-3`;
    alertContainer.style.zIndex = '9999';
    alertContainer.style.minWidth = '300px';
    alertContainer.innerHTML = `
        ${mensaje}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    document.body.appendChild(alertContainer);
    
    setTimeout(() => {
        alertContainer.remove();
    }, 5000);
}

// Función para filtrar tablas
function filtrarTabla(inputId, tablaId) {
    const input = document.getElementById(inputId);
    const tabla = document.getElementById(tablaId);
    
    if (!input || !tabla) return;

    input.addEventListener('keyup', function() {
        const filtro = this.value.toLowerCase();
        const filas = tabla.getElementsByTagName('tr');

        for (let i = 1; i < filas.length; i++) {
            const fila = filas[i];
            const texto = fila.textContent.toLowerCase();
            
            if (texto.includes(filtro)) {
                fila.style.display = '';
            } else {
                fila.style.display = 'none';
            }
        }
    });
}

// Función para copiar al portapapeles
function copiarAlPortapapeles(texto) {
    if (navigator.clipboard) {
        navigator.clipboard.writeText(texto).then(() => {
            mostrarNotificacion('Copiado al portapapeles', 'success');
        }).catch(() => {
            mostrarNotificacion('Error al copiar', 'danger');
        });
    } else {
        // Fallback para navegadores antiguos
        const textarea = document.createElement('textarea');
        textarea.value = texto;
        textarea.style.position = 'fixed';
        textarea.style.opacity = '0';
        document.body.appendChild(textarea);
        textarea.select();
        try {
            document.execCommand('copy');
            mostrarNotificacion('Copiado al portapapeles', 'success');
        } catch (err) {
            mostrarNotificacion('Error al copiar', 'danger');
        }
        document.body.removeChild(textarea);
    }
}

// Función para exportar tabla a CSV
function exportarTablaCSV(tablaId, nombreArchivo = 'datos.csv') {
    const tabla = document.getElementById(tablaId);
    if (!tabla) return;

    let csv = [];
    const filas = tabla.querySelectorAll('tr');

    filas.forEach(fila => {
        const cols = fila.querySelectorAll('td, th');
        const filaData = Array.from(cols).map(col => {
            return '"' + col.textContent.trim().replace(/"/g, '""') + '"';
        });
        csv.push(filaData.join(','));
    });

    const csvString = csv.join('\n');
    const blob = new Blob([csvString], { type: 'text/csv;charset=utf-8;' });
    const link = document.createElement('a');
    
    if (link.download !== undefined) {
        const url = URL.createObjectURL(blob);
        link.setAttribute('href', url);
        link.setAttribute('download', nombreArchivo);
        link.style.visibility = 'hidden';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }
}

// Función para actualizar contadores en tiempo real
function actualizarContador(elementoId, valorNuevo, duracion = 1000) {
    const elemento = document.getElementById(elementoId);
    if (!elemento) return;

    const valorActual = parseInt(elemento.textContent) || 0;
    const diferencia = valorNuevo - valorActual;
    const incremento = diferencia / (duracion / 10);
    let contador = valorActual;

    const intervalo = setInterval(() => {
        contador += incremento;
        if ((incremento > 0 && contador >= valorNuevo) || 
            (incremento < 0 && contador <= valorNuevo)) {
            elemento.textContent = valorNuevo;
            clearInterval(intervalo);
        } else {
            elemento.textContent = Math.round(contador);
        }
    }, 10);
}

// Función para validar email
function validarEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

// Función para validar cédula ecuatoriana
function validarCedula(cedula) {
    if (cedula.length !== 10) return false;
    
    const digitos = cedula.split('').map(Number);
    const digitoVerificador = digitos[9];
    const coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2];
    
    let suma = 0;
    for (let i = 0; i < 9; i++) {
        let valor = digitos[i] * coeficientes[i];
        if (valor >= 10) valor -= 9;
        suma += valor;
    }
    
    const modulo = suma % 10;
    const resultado = modulo === 0 ? 0 : 10 - modulo;
    
    return resultado === digitoVerificador;
}

// Función para modo oscuro (opcional)
function toggleModoOscuro() {
    document.body.classList.toggle('dark-mode');
    const isDarkMode = document.body.classList.contains('dark-mode');
    localStorage.setItem('darkMode', isDarkMode);
}

// Cargar preferencia de modo oscuro
if (localStorage.getItem('darkMode') === 'true') {
    document.body.classList.add('dark-mode');
}

// Función de búsqueda en tiempo real
function busquedaTiempoReal(inputId, contenedorId, selector) {
    const input = document.getElementById(inputId);
    const contenedor = document.getElementById(contenedorId);
    
    if (!input || !contenedor) return;

    input.addEventListener('input', function() {
        const termino = this.value.toLowerCase();
        const elementos = contenedor.querySelectorAll(selector);

        elementos.forEach(elemento => {
            const texto = elemento.textContent.toLowerCase();
            if (texto.includes(termino)) {
                elemento.style.display = '';
                elemento.classList.add('fade-in');
            } else {
                elemento.style.display = 'none';
            }
        });
    });
}

// Prevenir envío doble de formularios
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function() {
        const submitBtn = this.querySelector('button[type="submit"]');
        if (submitBtn) {
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Procesando...';
        }
    });
});

// Imprimir página
function imprimirPagina() {
    window.print();
}

// Volver arriba
function volverArriba() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Mostrar botón de volver arriba cuando se hace scroll
window.addEventListener('scroll', function() {
    const botonVolverArriba = document.getElementById('btnVolverArriba');
    if (botonVolverArriba) {
        if (window.pageYOffset > 300) {
            botonVolverArriba.style.display = 'block';
        } else {
            botonVolverArriba.style.display = 'none';
        }
    }
});

console.log('Sistema de Tutorías EPN - JavaScript Cargado ✓');
