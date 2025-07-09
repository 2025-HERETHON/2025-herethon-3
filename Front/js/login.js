document.addEventListener("DOMContentLoaded", function () {
  const ID = document.getElementById("ID");
  const PW = document.getElementById("PW");
  const LogInBtn = document.getElementById("loginBtn");
  const ErrorMsg = document.getElementById("Error");
  const InputBoxes = document.getElementsByClassName("InputBox");

  LogInBtn.addEventListener("click", (event) => {
    const username = ID.value;
    const password = PW.value;

    if (username == "user" && password == "asdf") {
      alert("You have successfully logged in.");
      ErrorMsg.classList.remove("show"); // 로그인 성공 시 에러 메시지 숨기기
      for (let box of InputBoxes) {
        box.classList.remove("show");
      }
    } else {
      ErrorMsg.classList.add("show"); // 로그인 실패 시 에러 메시지 보이기
      for (let box of InputBoxes) {
        box.classList.add("show");
      }
    }
  });
});
