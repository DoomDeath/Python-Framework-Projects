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

document.addEventListener("DOMContentLoaded", function () {
    const editButtons = document.querySelectorAll(".edit-button");

    editButtons.forEach(button => {
        button.addEventListener("click", () => {
            const row = button.closest("tr");
            const cells = row.querySelectorAll("td.editable");
            const tipoUsuarioLabel = row.querySelector(".tipo-usuario-label");
            const tipoUsuarioSelect = row.querySelector(".tipo-usuario-select");

            const dataToSave = {};

            cells.forEach(cell => {
                const fieldName = cell.getAttribute("data-field-name");
                const cellValue = cell.textContent.trim();

                if (cellValue) {
                    dataToSave[fieldName] = cellValue;
                }

                if (fieldName === "TipoUsuario") {
                    if (cell.getAttribute("contenteditable") === "false") {
                        cell.setAttribute("contenteditable", "true");
                        tipoUsuarioLabel.style.display = "none";
                        tipoUsuarioSelect.style.display = "block";
                    } else {
                        cell.setAttribute("contenteditable", "false");
                        tipoUsuarioLabel.style.display = "block";
                        tipoUsuarioSelect.style.display = "none";
                    }
                }
            });

            const userId = row.querySelector("td[data-user-id]").getAttribute("data-user-id");
            dataToSave["user_id"] = userId;
            console.log("Antes de la solicitud AJAX:", dataToSave);

            if (button.textContent === "Guardar") {
                fetch('/updateData', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(dataToSave)
                })
                    .then(response => response.json())
                    .then(data => {
                        console.log(data.mensaje);
                    })
                    .catch(error => {
                        console.error("Error al guardar los datos:", error);
                    });

                cells.forEach(cell => {
                    cell.setAttribute("contenteditable", "false");
                });
                tipoUsuarioLabel.style.display = "block";
                tipoUsuarioSelect.style.display = "none";

                button.textContent = "Editar";
            } else {
                cells.forEach(cell => {
                    if (cell.getAttribute("contenteditable") === "false") {
                        cell.setAttribute("contenteditable", "true");
                    } else {
                        cell.setAttribute("contenteditable", "false");
                    }
                });

                button.textContent = "Guardar";
            }
        });
    });
});
