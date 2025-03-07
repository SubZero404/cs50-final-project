document.addEventListener('DOMContentLoaded', function () {
    // Check if there are any flash messages in the page
    const messages = document.querySelectorAll('.flashed-message');
    
    messages.forEach(message => {
        const category = message.dataset.category; // success, error, etc.
        const text = message.dataset.message;
        
        // Trigger SweetAlert2 with the flashed message
        Swal.fire({
            position: "botton-end",
            icon: category,
            title: text,
            showConfirmButton: false,
            timer: 3000
        });
    });
});
