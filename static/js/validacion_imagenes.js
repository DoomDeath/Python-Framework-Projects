document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("guardar_disco_form").addEventListener("submit", function(event) {
        // Validar la imagen
        var imagenInput = document.getElementById("imagen");
        var imagenValue = imagenInput.value.toLowerCase();

        if (!imagenValue.endsWith(".jpg") && !imagenValue.endsWith(".jpeg")) {
            alert("Por favor, seleccione un archivo JPEG.");
            event.preventDefault();  // Evitar el envío del formulario si la validación falla
        }
    });
});