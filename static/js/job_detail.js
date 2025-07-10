document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("like-form");
  const button = document.getElementById("like-button");

  if (!form || !button) return;

  const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute("content");

  form.addEventListener("submit", function (event) {
    event.preventDefault();

    fetch(form.dataset.url, {
      method: "POST",
      headers: {
        "X-CSRFToken": csrfToken,
        "Content-Type": "application/json"
      },
    })
    .then(response => response.json())
    .then(data => {
      if (data.status === "liked") {
        button.textContent = "♥ 저장됨";
      } else if (data.status === "unliked") {
        button.textContent = "♡ 저장하기";
      }
    })
    .catch(error => {
      console.error("저장 중 오류 발생:", error);
    });
  });
});
