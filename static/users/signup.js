const idInput = document.getElementById("ID");
const checkBtn = document.getElementById("id_check");

// 아이디 입력 길이 검사
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

// 중복 확인 버튼 클릭 시
checkBtn.addEventListener("click", function () {
    const userId = idInput.value;

    fetch("/signup/check_user_id/", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
            "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: new URLSearchParams({ user_id: userId })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);  // 백엔드에서 받은 메시지 출력
    })
    .catch(error => {
        alert("서버 요청 중 오류가 발생했습니다.");
        console.error("Error:", error);
    });
});
