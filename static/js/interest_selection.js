const submitBtn = document.getElementById("submit_btn");
const tagButtons = document.querySelectorAll(".tag");

tagButtons.forEach((btn) => {
  btn.addEventListener("click", () => {
    btn.classList.toggle("selected");

    const selectedCount = document.querySelectorAll(".tag.selected").length;

    if (selectedCount === 0) {
      submitBtn.textContent = "관심사 선택 후 추천 받기";
      submitBtn.style.backgroundColor = "#D9D9D9";
      submitBtn.style.color = "#000000";      
    } else {
      submitBtn.textContent = `${selectedCount}개 선택 완료! 추천 받기`;
      submitBtn.style.backgroundColor = "#2B66D0";
      submitBtn.style.color = "#fff";
    }
  });
});

// form 제출 전에 선택된 태그들 input에 넣기
const form = document.querySelector("form");
const interestsInput = document.getElementById("interestsInput");

form.addEventListener("submit", (e) => {
  const selectedTags = Array.from(document.querySelectorAll(".tag.selected"))
    .map(tag => tag.textContent.trim());

  if (selectedTags.length === 0) {
    e.preventDefault(); // 선택 안 했으면 제출 막기
    alert("관심사를 하나 이상 선택해주세요!");
    return;
  }

  interestsInput.value = selectedTags.join(",");
});
