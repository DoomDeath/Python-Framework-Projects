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
    });
});
