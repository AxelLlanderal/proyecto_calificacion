document.addEventListener('DOMContentLoaded', () => {
    // Seleccionar ambos formularios
    const formAgregar = document.getElementById('form-agregar');
    const formActualizar = document.getElementById('form-actualizar');
    
    // Depuración para confirmar que el script se carga
    console.log('Script cargado. FormAgregar:', formAgregar, 'FormActualizar:', formActualizar);

    // Función de validación general
    function validateForm(form) {
        if (!form) {
            console.log('Formulario no encontrado:', form);
            return;
        }
        
        form.addEventListener('submit', (e) => {
            console.log('Evento submit capturado para el formulario:', form.id);
            e.preventDefault();
            let isValid = true;

            // Limpiar mensajes de error previos
            form.querySelectorAll('.error').forEach(error => error.textContent = '');

            // Validar nombre
            const nombre = form.querySelector('#nombre').value.trim();
            console.log('Validando nombre:', nombre);
            if (!nombre) {
                form.querySelector('#error-nombre').textContent = 'El nombre es obligatorio.';
                isValid = false;
            } else if (!/^[a-zA-Z\s]+$/.test(nombre)) {
                form.querySelector('#error-nombre').textContent = 'El nombre solo debe contener letras y espacios.';
                isValid = false;
            } else if (nombre.length > 100) {
                form.querySelector('#error-nombre').textContent = 'El nombre no debe exceder los 100 caracteres.';
                isValid = false;
            }

            // Validar edad
            const edad = form.querySelector('#edad').value;
            console.log('Validando edad:', edad);
            if (!edad) {
                form.querySelector('#error-edad').textContent = 'La edad es obligatoria.';
                isValid = false;
            } else if (isNaN(edad) || edad < 3 || edad > 99 || !Number.isInteger(Number(edad))) {
                form.querySelector('#error-edad').textContent = 'La edad debe ser un número entero entre 3 y 99.';
                isValid = false;
            }

            // Validar correo electrónico
            const correo = form.querySelector('#correo_electronico').value.trim();
            const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
            console.log('Validando correo:', correo);
            if (!correo) {
                form.querySelector('#error-correo').textContent = 'El correo electrónico es obligatorio.';
                isValid = false;
            } else if (!correo.includes('@')) {
                form.querySelector('#error-correo').textContent = 'El correo debe contener un símbolo "@".';
                isValid = false;
            } else if (!emailRegex.test(correo)) {
                form.querySelector('#error-correo').textContent = 'Ingrese un correo electrónico válido (ejemplo: nombre@dominio.com).';
                isValid = false;
            }

            // Validar calificaciones
            const calificaciones = [
                { id: 'calificacion_1', errorId: 'error-calificacion_1' },
                { id: 'calificacion_2', errorId: 'error-calificacion_2' },
                { id: 'calificacion_3', errorId: 'error-calificacion_3' }
            ];

            calificaciones.forEach(cal => {
                const valor = form.querySelector(`#${cal.id}`).value;
                console.log(`Validando ${cal.id}:`, valor);
                if (!valor) {
                    form.querySelector(`#${cal.errorId}`).textContent = 'La calificación es obligatoria.';
                    isValid = false;
                } else if (isNaN(valor) || valor < 0 || valor > 100) {
                    form.querySelector(`#${cal.errorId}`).textContent = 'La calificación debe estar entre 0.0 y 100.0.';
                    isValid = false;
                } else {
                    // Asegurar que tenga máximo un decimal
                    const decimalPlaces = (valor.toString().split('.')[1] || '').length;
                    if (decimalPlaces > 1) {
                        form.querySelector(`#${cal.errorId}`).textContent = 'La calificación debe tener máximo un decimal (ejemplo: 85.5).';
                        isValid = false;
                    }
                }
            });

            // Si todas las validaciones pasan, enviar el formulario
            console.log('Resultado de la validación:', isValid);
            if (isValid) {
                console.log('Formulario válido, enviando...');
                form.submit();
            } else {
                console.log('Formulario inválido, no se envía.');
            }
        });
    }

    // Aplicar validaciones a ambos formularios
    validateForm(formAgregar);
    validateForm(formActualizar);
});