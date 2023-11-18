function enviarFormulario(idButton, idForm) {

     // Mostrar el overlay al hacer clic en el botón
     mostrarOverlay();
    // Deshabilitar el botón al hacer clic
    var boton = document.getElementById(idButton);
    boton.disabled = true;

   

    if (idButton === 'id_logout') {
        // El código dentro de este bloque se ejecutará si la condición es verdadera
        boton.innerText = 'Cerrando Session...';
    } else if (idButton === 'button_search') {
        boton.style.backgroundColor = '#CCCCCC'; // Puedes ajustar el color según tus necesidades
        boton.innerText = 'Buscando...';
    } else {
        boton.style.backgroundColor = '#CCCCCC'; // Puedes ajustar el color según tus necesidades
        boton.innerText = 'Cargando...';
    }


    // Enviar el formulario
    var formulario = document.getElementById(idForm);
    formulario.submit();


    // Opcionalmente, puedes mostrar un mensaje de espera o realizar otras acciones necesarias
}


function mostrarOverlay() {
    document.getElementById('overlay').style.display = 'flex';
}

function ocultarOverlay() {
    document.getElementById('overlay').style.display = 'none';
}
