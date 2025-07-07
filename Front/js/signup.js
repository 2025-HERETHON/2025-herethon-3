const idInput = document.getElementById("ID");
const checkBtn = document.getElementById("id_check");

function checkIdLength() {
    const isValid = idInput.value.trim().length >= 6;

    if (isValid) {
        checkBtn.classList.add("active");
        checkBtn.disabled = false;
    } else {
        checkBtn.classList.remove("active");
        checkBtn.disabled = true;
    }
}

idInput.addEventListener("input", checkIdLength);
