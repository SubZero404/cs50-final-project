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

function confirmDelete(event, form) {
    event.preventDefault(); // Prevent the form from being submitted immediately

    Swal.fire({
        title: "Are you sure?",
        text: "You want to delete?",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Yes, delete it!"
    }).then((result) => {
        if (result.isConfirmed) {
            // Now submit the form after confirmation
            form.submit();
        }
    });
}
