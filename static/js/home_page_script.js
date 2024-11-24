document.addEventListener("DOMContentLoaded", function() {
    const errorContainer = document.getElementById('error-container');
    const errorMessage = errorContainer.getAttribute('data-error-message');
    
    if (errorMessage) {
        alert(errorMessage);
    }
});
