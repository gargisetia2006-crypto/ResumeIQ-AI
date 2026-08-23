const fileInput = document.getElementById("resumeInput");
const filePill = document.getElementById("filePill");
const fileName = document.getElementById("fpName");
const fileSize = document.getElementById("fpSize");
const removeBtn = document.getElementById("fpRemove");
const dropzone = document.getElementById("dropzone");

// Show selected file
fileInput.addEventListener("change", function () {

    if (this.files.length === 0) return;

    const file = this.files[0];

    fileName.textContent = file.name;

    fileSize.textContent =
        (file.size / 1024).toFixed(1) + " KB";

    filePill.classList.add("show");

    // Optional: hide upload box after choosing file
    dropzone.style.display = "none";
});


// Remove selected file
removeBtn.addEventListener("click", function () {

    fileInput.value = "";

    filePill.classList.remove("show");

    dropzone.style.display = "block";

});