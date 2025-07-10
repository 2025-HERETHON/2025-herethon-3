const idInput = document.getElementById("ID");
const checkBtn = document.getElementById("check_user_id");
const helperText = document.querySelector(".HelperText1 p");

const passwordInput = document.getElementById("PW");
const passwordtryInput = document.getElementById("PW_try");

const pwBox = document.querySelector(".password_input1 .InputBox");
const pwHelperText = document.querySelector(".HelperText2 p");

const pwtryBox = document.querySelector(".password_input2 .InputBox");
const pwtryHelperText = document.querySelector(".HelperText3 p");

const signupForm = document.getElementById("SignupInput"); // form 태그에 id 부여 필요

let isIdAvailable = false;  

console.log("✅ JS 파일 정상 로드됨");


// 1. ID 6자 이상, 영어 또는 숫자 → 중복확인 버튼 활성화
function isIdValid(id) {
    const pattern = /^[A-Za-z0-9]{6,10}$/;
    return pattern.test(id);
}

function checkIdInput() {
    const id = idInput.value.trim();

    if (isIdValid(id)) {
        checkBtn.classList.add("active");
        checkBtn.disabled = false;
        isIdAvailable = false;
    } else {
        checkBtn.classList.remove("active");
        checkBtn.disabled = true;
    }
}
idInput.addEventListener("input", checkIdInput);

// 2. 중복확인 버튼 클릭 시 메시지 출력
checkBtn.addEventListener("click", function () {
    const userId = idInput.value.trim();

    console.log("✅ 요청 URL:", window.location.href);


    fetch("/check_user_id/", {
        method: "POST",  // 백엔드에 맞게 GET으로 바꿔도 됨
        headers: {
            "Content-Type": "application/json",
            "X-Requested-With": "XMLHttpRequest"
        },
        body: JSON.stringify({ user_id: userId })
    })
    .then(response => response.json())
    .then(data => {
        if (data.exists) {
            helperText.textContent = "중복된 아이디입니다.";
            helperText.classList.add("error-text");
            isIdAvailable = false;
        } else {
            helperText.textContent = "사용 가능한 아이디입니다.";
            helperText.classList.remove("error-text");
            isIdAvailable = true;
        }
    })
    .catch(err => {
        console.error(err);
        isIdAvailable = false;
    });
});

// 3. 비밀번호 유효성 검사 함수
function isPasswordValid(password) {
    const pattern = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]).{6,20}$/;
    return pattern.test(password);
}

// 4. 회원가입 버튼 클릭 → 유효성 체크 & 유효하지 않으면 전송 차단
signupForm.addEventListener("submit", function (e) {
    const password = passwordInput.value.trim();
    const passwordTry = passwordtryInput.value.trim();
    let isValid = true;

    if (!isIdAvailable) {
    helperText.textContent = "아이디 중복 확인을 해주세요.";
    helperText.classList.add("error-text");
    isValid = false;
    }

    // 비밀번호 조건 확인
    if (!isPasswordValid(password)) {
        pwBox.classList.add("error-border");
        pwHelperText.classList.add("error-text");
        isValid = false;
    } else {
        pwBox.classList.remove("error-border");
        pwHelperText.classList.remove("error-text");
    }

    // 비밀번호 일치 확인
    if (password !== passwordTry) {
        pwtryBox.classList.add("error-border");
        pwtryHelperText.style.display = "block";
        isValid = false;
    } else {
        pwtryBox.classList.remove("error-border");
        pwtryHelperText.style.display = "none";
    }

    if (!isValid) {
        e.preventDefault(); 
    }
});