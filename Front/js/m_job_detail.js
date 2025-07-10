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
const heartBtn = document.getElementById("heartBtn");
const heartImg = document.getElementById("heartImg");

let liked = false;

heartBtn.addEventListener("click", () => {
    liked = !liked;
    if (liked) {
        heartImg.src = "../img/fill_heart.svg";  // 채워진 하트 이미지 경로
    } else {
        heartImg.src = "../img/heart.svg";   // 빈 하트 이미지 경로
    }
});
