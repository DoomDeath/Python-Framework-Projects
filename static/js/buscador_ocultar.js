// buscador_ocultar.js
function toggleBusqueda() {
    var busquedaForm = document.getElementById("searchForm");
    var nuevaBusquedaBtn = document.getElementById("btn-nueva-busqueda");

    if (busquedaForm.style.display === "none") {
        busquedaForm.style.display = "block";
        nuevaBusquedaBtn.style.display = "none";
    } else {
        busquedaForm.style.display = "none";
        nuevaBusquedaBtn.style.display = "block";
    }
}