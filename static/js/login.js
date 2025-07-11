document.addEventListener("DOMContentLoaded", function () {
  const ID = document.getElementById("ID");
  const PW = document.getElementById("PW");
  const LogInBtn = document.getElementById("loginBtn");
  const ErrorMsg = document.getElementById("Error");
  const InputBoxes = document.getElementsByClassName("InputBox");

  LogInBtn.addEventListener("click", async (e) => {
    e.preventDefault();

    const user_id = ID.value.trim();
    const password = PW.value.trim();

    // 초기화
    ErrorMsg.classList.remove("show");
    for (let box of InputBoxes) box.classList.remove("show");

    // 빈값 검사
    if (!user_id || !password) {
      ErrorMsg.textContent = "아이디와 비밀번호를 모두 입력해주세요.";
      ErrorMsg.classList.add("show");
      for (let box of InputBoxes) box.classList.add("show");
      return;
    }

    try {
      const response = await fetch("/login/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]")
            .value,
        },
        body: JSON.stringify({ user_id, password }),
      });

      // const result = await response.json();

      // // ← 여기를 response.ok 대신 result.success로만 체크
      // if (result.success) {
      //   window.location.href = "/home/";
      // } else {
      //   ErrorMsg.textContent =
      //     result.error || "아이디 또는 비밀번호를 다시 확인해주세요.";
      //   ErrorMsg.classList.add("show");
      //   for (let box of InputBoxes) box.classList.add("show");
      // }

      let result;
      try {
        result = await response.json();
      } catch {
        // 파싱 실패는 곧 “로그인 실패” 로 간주
        result = {
          success: false,
          error: "아이디 또는 비밀번호를 다시 확인해주세요.",
        };
      }

      if (result.success) {
        window.location.href = "/home/";
      } else {
        // 무조건 이 블록이 실행됩니다
        ErrorMsg.textContent = result.error;
        ErrorMsg.classList.add("show");
        for (let box of InputBoxes) box.classList.add("show");
      }
    } catch (err) {
      console.error(err);
      ErrorMsg.textContent = "SERVER ERRORs.";
      ErrorMsg.classList.add("show");
      for (let box of InputBoxes) box.classList.add("show");
    }
  });
});
