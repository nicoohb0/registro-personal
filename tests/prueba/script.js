class RegistroPeso {
    constructor() {
        this.datosGuardados = [];
        this.nombreArchivo = 'datos-peso-corporal.txt';
        this.pesoMinimo = 2.0;
        this.pesoMaximo = 300.0;
        
        this.inicializarElementos();
        this.cargarDatos();
        this.configurarEventos();
    }

    inicializarElementos() {
        this.nombreInput = document.getElementById('nombreCompleto');
        this.pesoInput = document.getElementById('peso');
        this.guardarBtn = document.getElementById('guardarBtn');
        this.resultadoDiv = document.getElementById('resultado');
        this.listaDatosDiv = document.getElementById('listaDatos');
    }

    configurarEventos() {
        this.guardarBtn.addEventListener('click', () => this.guardarDatos());
        
        // Permitir guardar con Enter
        this.pesoInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.guardarDatos();
            }
        });
    }

    async cargarDatos() {
        try {
            // En un entorno real, aquí harías una petición al servidor
            // Para este ejemplo, cargamos desde localStorage como alternativa
            const datosGuardados = localStorage.getItem(this.nombreArchivo);
            if (datosGuardados) {
                this.datosGuardados = JSON.parse(datosGuardados);
                this.mostrarDatos();
            }
        } catch (error) {
            console.error('Error al cargar datos:', error);
        }
    }

    async guardarEnArchivo(datos) {
        try {
            // En un entorno real, aquí enviarías los datos al servidor
            // Para este ejemplo, usamos localStorage como alternativa
            localStorage.setItem(this.nombreArchivo, JSON.stringify(datos));
            return true;
        } catch (error) {
            console.error('Error al guardar en archivo:', error);
            return false;
        }
    }

    async guardarDatos() {
        const nombre = this.nombreInput.value.trim();
        const pesoTexto = this.pesoInput.value.trim();

        // Validar campos vacíos
        if (!nombre || !pesoTexto) {
            this.mostrarResultado('Completame ambos campos', 'error');
            return;
        }

        // Validar que el peso sea un número
        let peso;
        try {
            peso = parseFloat(pesoTexto);
            if (isNaN(peso)) {
                throw new Error('No es un número válido');
            }
        } catch (error) {
            this.mostrarResultado('Ingresa un peso válido (número)', 'error');
            return;
        }

        // Validar rango de peso
        if (peso < this.pesoMinimo || peso > this.pesoMaximo) {
            this.mostrarResultado(
                `El peso debe estar entre ${this.pesoMinimo} y ${this.pesoMaximo} kg`, 
                'advertencia'
            );
            return;
        }

        // Crear y guardar datos
        const datos = {
            nombre: nombre,
            peso: peso,
            fecha: new Date().toLocaleString()
        };

        this.datosGuardados.push(datos);

        // Guardar en archivo (localStorage en este caso)
        const guardadoExitoso = await this.guardarEnArchivo(this.datosGuardados);

        if (guardadoExitoso) {
            this.mostrarResultado('Datos guardados correctamente', 'exito');
            
            // Limpiar campos
            this.nombreInput.value = '';
            this.pesoInput.value = '';
            
            // Mostrar datos actualizados
            this.mostrarDatos();
            
            // Enfocar el campo de nombre
            this.nombreInput.focus();
        } else {
            this.mostrarResultado('Datos guardados, pero error al guardar en el fichero', 'advertencia');
        }
    }

    mostrarResultado(mensaje, tipo = 'info') {
        this.resultadoDiv.textContent = mensaje;
        this.resultadoDiv.className = 'resultado';
        
        switch (tipo) {
            case 'error':
                this.resultadoDiv.classList.add('error');
                break;
            case 'exito':
                this.resultadoDiv.classList.add('exito');
                break;
            case 'advertencia':
                this.resultadoDiv.classList.add('advertencia');
                break;
        }
    }

    mostrarDatos() {
        if (!this.datosGuardados || this.datosGuardados.length === 0) {
            this.listaDatosDiv.textContent = 'No hay datos guardados';
            return;
        }

        let textoDatos = 'Datos guardados:\n\n';
        this.datosGuardados.forEach((dato, index) => {
            textoDatos += `${index + 1}. Nombre: ${dato.nombre} - Peso: ${dato.peso} kg`;
            if (dato.fecha) {
                textoDatos += ` (${dato.fecha})`;
            }
            textoDatos += '\n';
        });

        this.listaDatosDiv.textContent = textoDatos;
    }

    // Método para exportar datos (opcional)
    exportarDatos() {
        let contenido = "---- REGISTRO PESO ----\n";
        this.datosGuardados.forEach(dato => {
            contenido += `${dato.nombre}, ${dato.peso} Kg\n`;
        });

        const blob = new Blob([contenido], { type: 'text/plain' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = this.nombreArchivo;
        a.click();
        URL.revokeObjectURL(url);
    }

    // Método para limpiar todos los datos (opcional)
    limpiarDatos() {
        if (confirm('¿Estás seguro de que quieres eliminar todos los datos?')) {
            this.datosGuardados = [];
            localStorage.removeItem(this.nombreArchivo);
            this.mostrarDatos();
            this.mostrarResultado('Todos los datos han sido eliminados', 'exito');
        }
    }
}

// Inicializar la aplicación cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', () => {
    new RegistroPeso();
});

// Agregar funciones globales para uso opcional desde la consola
window.registroPeso = {
    exportar: function() {
        const app = document.querySelector('script')._app || 
                   Object.values(document.querySelectorAll('*')).find(el => el.constructor.name === 'RegistroPeso');
        if (app && app.exportarDatos) app.exportarDatos();
    },
    limpiar: function() {
        const app = document.querySelector('script')._app || 
                   Object.values(document.querySelectorAll('*')).find(el => el.constructor.name === 'RegistroPeso');
        if (app && app.limpiarDatos) app.limpiarDatos();
    }
};