function enviarFormulario(idButton, id) {
    // Deshabilitar el botón al hacer clic
    var boton = document.getElementById(idButton);
    boton.disabled = true;

    // Cambiar el color del botón deshabilitado (por ejemplo, a gris)
    boton.style.backgroundColor = '#CCCCCC'; // Puedes ajustar el color según tus necesidades

    // Cambiar el texto del botón a "Cargando..."
    boton.innerHTML = 'Cargando...';

    // Enviar el formulario
    var formulario = document.getElementById(id);
    formulario.submit();

    console.log("SE PRESIONÓ");

    // Opcionalmente, puedes mostrar un mensaje de espera o realizar otras acciones necesarias
}
