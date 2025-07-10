// JS 코드 (inline 또는 외부 .js 파일로 분리 가능)
document.addEventListener("DOMContentLoaded", () => {
  
  const boxContainer = document.getElementById("BoxContainer");
  const jobCards = document.querySelectorAll(".Box");
  const recentJob = document.getElementById("recentJob");
  const emptyJobSection = document.getElementById("emptyJobSection");
  const logoutBtn = document.getElementById("logout");
  

  if (jobCards.length === 0) {
    // 직무 카드가 없을 때: 안내 문구만 보이게
    boxContainer.style.display = "none";
    recentJob.style.display = "none";
    emptyJobSection.style.display = "flex";

    // LOGOUT 버튼 위치 조정
    logoutBtn.style.marginTop = "152px";
  } else {
    // 직무 카드가 있을 때
    boxContainer.style.display = "flex";
    recentJob.style.display = "block";
    emptyJobSection.style.display = "none";

    // 원래대로 위치
    logoutBtn.style.marginTop = "208.5px";
  }

  // 로그아웃 모달 관련
  const logoutBox = document.getElementById("logoutBox");
  const overlay = document.getElementById("overlay");
  const cancelBtn = document.getElementById("cancel");
  const confirmBtn = document.getElementById("confirm");

  if (logoutBox && overlay && confirmBtn && logoutBtn) {
    logoutBtn.addEventListener("click", () => {
      logoutBox.style.display = "flex";
      overlay.style.display = "block";
    });

    cancelBtn.addEventListener("click", () => {
      logoutBox.style.display = "none";
      overlay.style.display = "none";
    });

    confirmBtn.addEventListener("click", () => {
      console.log("🚪 로그아웃 버튼 클릭됨!"); // ✅ 반드시 이 로그가 찍혀야 함
      const logoutUrl = confirmBtn.dataset.logoutUrl?.split('?')[0];
      if (logoutUrl) {
        window.location.href = logoutUrl;
      }
    });
  }
});
