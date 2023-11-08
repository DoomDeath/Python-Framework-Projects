document.addEventListener("DOMContentLoaded", function () {
    const mostrarFormulario = document.getElementById("mostrarFormulario");
    const formularioCrearUsuario = document.getElementById("formularioCrearUsuario");
    const cerrarFormulario = document.getElementById("cerrarFormulario");
    const cancelar = document.getElementById("cancelar");

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
        const cells = row.querySelectorAll("td[contenteditable]");
        const td = row.querySelector("td[data-user-id]");

        if (td) {
            const userId = td.getAttribute("data-user-id");
            console.log("ID del usuario:", userId);
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
