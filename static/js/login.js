document.addEventListener("DOMContentLoaded", function () {
  const ID = document.getElementById("ID");
  const PW = document.getElementById("PW");
  const LogInBtn = document.getElementById("loginBtn");
  const ErrorMsg = document.getElementById("Error");
  const InputBoxes = document.getElementsByClassName("InputBox");

  LogInBtn.addEventListener("click", async (event) => {
    event.preventDefault(); // 폼이 제출되는 기본 동작을 막음

    const user_id = ID.value;
    const password = PW.value;

    // 로그인 정보를 서버로 전송
    const response = await fetch('/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value, // CSRF 토큰 추가
      },
      body: JSON.stringify({ user_id: user_id, password: password }),
    });

    const result = await response.json();

    if (response.ok && result.success) {
      // 로그인 성공 시 홈 화면으로 리디렉션
      window.location.href = 'home/';  // 홈 화면으로 리디렉션 (혹은 리디렉션 URL을 변경)
    } else {
      ErrorMsg.textContent = result.error || "아이디 또는 비밀번호를 다시 확인해주세요.";
      ErrorMsg.classList.add("show"); // 로그인 실패 시 에러 메시지 보이기
      for (let box of InputBoxes) {
        box.classList.add("show");
        }
    }
  });
});
