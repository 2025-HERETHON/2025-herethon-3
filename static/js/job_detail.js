// document.addEventListener("DOMContentLoaded", function () {
//   const form = document.getElementById("like-form");
//   const button = document.getElementById("like-button");

//   if (!form || !button) return;

//   const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute("content");

//   form.addEventListener("submit", function (event) {
//     event.preventDefault();

//     fetch(form.dataset.url, {
//       method: "POST",
//       headers: {
//         "X-CSRFToken": csrfToken,
//         "Content-Type": "application/json"
//       },
//     })
//     .then(response => response.json())
//     .then(data => {
//       if (data.status === "liked") {
//         button.textContent = "♥ 저장됨";
//       } else if (data.status === "unliked") {
//         button.textContent = "♡ 저장하기";
//       }
//     })
//     .catch(error => {
//       console.error("저장 중 오류 발생:", error);
//     });
//   });
// });



// 가로 스크롤 부분

function enableDragScroll(element) {
    let isDown = false, startX, scrollLeft;

    element.addEventListener('mousedown', (e) => {
        isDown = true;
        element.classList.add('active');
        startX = e.pageX - element.offsetLeft;
        scrollLeft = element.scrollLeft;
        e.preventDefault();
    });

    element.addEventListener('mouseleave', () => {
        isDown = false;
        element.classList.remove('active');
    });

    element.addEventListener('mouseup', () => {
        isDown = false;
        element.classList.remove('active');
    });

    element.addEventListener('mousemove', (e) => {
        if (!isDown) return;
        e.preventDefault();
        const x = e.pageX - element.offsetLeft;
        const walk = (x - startX) * 1.5;
        element.scrollLeft = scrollLeft - walk;
    });
}

enableDragScroll(document.getElementById('scrollBox1'));
enableDragScroll(document.getElementById('scrollBox2'));


// 플로팅 버튼 눌렀을 때 하트 색칠되는 부분
document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("like-form");
    const button = document.getElementById("like-button");
    const heartImg = document.getElementById("heartImg");

    if (!form || !button || !heartImg) return;

    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute("content");

    let liked = false;

    // 버튼 누르면 하트 이미지만 바뀜
    button.addEventListener("click", () => {
        liked = !liked;
        heartImg.src = liked ? window.staticPaths.heartFill : window.staticPaths.heartEmpty;
    });

    // 서버에 좋아요 상태 전송 (이미지랑 liked 상태 유지용)
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
                liked = true;
                heartImg.src = window.staticPaths.heartFill;
            } else if (data.status === "unliked") {
                liked = false;
                heartImg.src = window.staticPaths.heartEmpty;
            }
        })
        .catch(error => {
            console.error("저장 중 오류 발생:", error);
        });
    });
});

