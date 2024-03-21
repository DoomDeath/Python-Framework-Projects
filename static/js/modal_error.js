document.addEventListener('DOMContentLoaded', function() {
    var errorMessages = document.getElementById('flash-messages');
    if (errorMessages && errorMessages.children.length > 0) {
        var modalErrorMessages = document.getElementById('modal-error-messages');
        modalErrorMessages.innerHTML = errorMessages.innerHTML;

        var modal = document.getElementById('errorModal');
        modal.style.display = 'block';
    }
});

function cerrarModal() {
    var modal = document.getElementById('errorModal');
    modal.style.display = 'none';
}

