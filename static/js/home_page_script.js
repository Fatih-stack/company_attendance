document.addEventListener("DOMContentLoaded", function() {
    // Hata durumlarını kullanıcıya göstermek için bir kontrol ekleyin
    const errorMessage = "\{\{ error_message\|default_if_none:'' \}\}";
    if (errorMessage) {
        alert(errorMessage);
    }
});