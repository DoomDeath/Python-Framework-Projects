// Obtener todos los checkboxes
var checkboxes = document.getElementsByName("criterio");

checkboxes.forEach(function (checkbox) {
    checkbox.addEventListener('change', function () {
        // Desmarcar los demás checkboxes
        checkboxes.forEach(function (otherCheckbox) {
            if (otherCheckbox !== checkbox) {
                otherCheckbox.checked = false;
            }
        });

        // Realizar la búsqueda automáticamente
        buscarRegistros();
    });
});

// Agregar el evento input a la barra de búsqueda
var searchInput = document.getElementById("searchInput");
searchInput.addEventListener('input', function () {
    buscarRegistros();
});

function buscarRegistros() {
    // Obtener el valor de la barra de búsqueda
    var termino = searchInput.value;

    // Obtener el criterio de búsqueda seleccionado
    var criterio = obtenerCriterioSeleccionado();

    // Enviar la solicitud de búsqueda al servidor (puedes usar AJAX o Fetch)

    // Actualizar la tabla con los resultados obtenidos del servidor
    actualizarTablaConResultados();
}

function obtenerCriterioSeleccionado() {
    var criterio = null;

    checkboxes.forEach(function (checkbox) {
        if (checkbox.checked) {
            criterio = checkbox.value;
        }
    });
    // Si ninguno está seleccionado, seleccionar el primero
    if (!criterio && checkboxes.length > 0) {
        checkboxes[0].checked = true;
        criterio = checkboxes[0].value;
    }


    return criterio;
}

function actualizarTablaConResultados() {
    // ... (como en el ejemplo anterior)
}