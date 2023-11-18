function enviarFormulario(id) {
    // Deshabilitar el botón al hacer clic
    var boton = document.getElementById("botonEnviar");
    boton.disabled = true;

    // Enviar el formulario
    var formulario = document.getElementById(id);
    formulario.submit();

    console.log("SE PRESIONO")

    // Opcionalmente, puedes mostrar un mensaje de espera o realizar otras acciones necesarias
}