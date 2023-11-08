document.addEventListener("DOMContentLoaded", function () {
    const mostrarFormulario = document.getElementById("mostrarFormulario");
    const formularioCrearUsuario = document.getElementById("formularioCrearUsuario");
    const cerrarFormulario = document.getElementById("cerrarFormulario");
    const cancelar = document.getElementById("cancelar");
    const submitButton = document.getElementById("submit-button"); // Agregamos el botón "Guardar" al formulario

    mostrarFormulario.addEventListener("click", function () {
        mostrarFormulario.style.display = "none";
        formularioCrearUsuario.style.display = "block";
        cerrarFormulario.style.display = "none";
    });

    cancelar.addEventListener("click", function () {
        mostrarFormulario.style.display = "block";
        formularioCrearUsuario.style.display = "none";
        cerrarFormulario.style.display = "block";
    });
});

const editButtons = document.querySelectorAll(".edit-button");

editButtons.forEach(button => {
    button.addEventListener("click", () => {
        const row = button.closest("tr"); // Obtener la fila actual
        const cells = row.querySelectorAll("td.editable");
        const dataToSave = {}; // Inicializa el objeto dataToSave fuera del bucle

        cells.forEach(cell => {
            const fieldName = cell.getAttribute("data-field-name");
            const cellValue = cell.textContent.trim(); // Asegúrate de que el valor no tenga espacios en blanco alrededor
            if (cellValue) {
                dataToSave[fieldName] = cellValue;
            }
        });
        const userId = row.querySelector("td[data-user-id]").getAttribute("data-user-id");
            dataToSave["user_id"] = userId;
        console.log("Antes de la solicitud AJAX:", dataToSave);

        if (button.textContent === "Guardar") {
            // Realiza una solicitud AJAX para guardar los datos
            fetch('/updateData', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(dataToSave)
            })
                .then(response => response.json())
                .then(data => {
                    console.log(data.mensaje); // Muestra la respuesta del servidor en la consola
                })
                .catch(error => {
                    console.error("Error al guardar los datos:", error);
                });
        }

        cells.forEach(cell => {
            if (cell.getAttribute("contenteditable") === "false") {
                cell.setAttribute("contenteditable", "true");
            } else {
                cell.setAttribute("contenteditable", "false");
            }
        });

        if (button.textContent === "Editar") {
            button.textContent = "Guardar";
        } else {
            button.textContent = "Editar";
        }
    });
});
