document.addEventListener("DOMContentLoaded", () => {
  const selectedTags = new Set();
  const submitBtn = document.getElementById("submit_btn");
  const tagButtons = document.querySelectorAll(".tag");
  const form = document.querySelector("form");
  const interestsInput = document.getElementById("interestsInput");

  tagButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      const tagName = btn.value;

      if (btn.classList.contains("selected")) {
        btn.classList.remove("selected");
        selectedTags.delete(tagName);
      } else {
        btn.classList.add("selected");
        selectedTags.add(tagName);
      }

      const count = selectedTags.size;
      submitBtn.textContent = count === 0
        ? "관심사 선택 후 추천 받기"
        : `${count}개 선택 완료! 추천 받기`;

      submitBtn.style.backgroundColor = count === 0 ? "#D9D9D9" : "#2B66D0";
      submitBtn.style.color = count === 0 ? "#000000" : "#ffffff";

      interestsInput.value = Array.from(selectedTags).join(",");
    });
  });

  form.addEventListener("submit", (e) => {
    if (selectedTags.size === 0) {
      e.preventDefault();
      alert("관심사를 하나 이상 선택해주세요!");
    }
  });
});
