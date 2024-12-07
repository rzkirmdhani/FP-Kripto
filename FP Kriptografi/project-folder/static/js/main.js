document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const fileInput = document.getElementById('pdf');
    const submitButton = document.querySelector('button[type="submit"]');

    // Disable submit button if no file is selected
    fileInput.addEventListener('change', function () {
        if (fileInput.files.length > 0) {
            submitButton.disabled = false;
        } else {
            submitButton.disabled = true;
        }
    });

    // Show loading text on submit
    form.addEventListener('submit', function () {
        submitButton.textContent = 'Processing...';
        submitButton.disabled = true;
    });
});
