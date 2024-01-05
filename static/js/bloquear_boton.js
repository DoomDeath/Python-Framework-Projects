function enviarFormulario(idButton, idForm) {
    // Mostrar el overlay al hacer clic en el botón

    mostrarOverlay();
    // Deshabilitar el botón al hacer clic
    var boton = document.getElementById(idButton);
    boton.disabled = true;


    if (idButton === 'id_logout') {
        boton.innerText = 'Cerrando Sesión...';
    } else if (idButton === 'button_search') {
        boton.style.backgroundColor = '#CCCCCC';
        boton.innerText = 'Buscando...';
    } else if (idButton === 'buttonDelete') {

    } else if (idButton === 'paginador_anterior' || idButton === 'paginador_siguiente') {
        return true;
    } else {
        boton.style.backgroundColor = '#CCCCCC';
        boton.innerText = 'Cargando...';
    }

    // Retornar false si la validación no pasa para evitar el envío del formulario
    var formulario = document.getElementById(idForm);

    if (!formulario || !formulario.checkValidity()) {
        return false;
    }

    // Opcionalmente, puedes mostrar un mensaje de espera o realizar otras acciones necesarias
}

function mostrarOverlay() {
    document.getElementById('overlay').style.display = 'flex';
}

function ocultarOverlay() {
    document.getElementById('overlay').style.display = 'none';
}
