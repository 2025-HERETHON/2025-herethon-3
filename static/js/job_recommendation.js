document.addEventListener("DOMContentLoaded", function () {

const jobs = [
  {
    title: "환경 데이터 분석가",
    description: "환경 관련 센서·데이터 기반 기후 패턴 분석",
    tags: ["#환경/지속가능성"],
    category: ["Science", "Tech"]
  },

  {
    title: "AI 서비스 기획자",
    description: "AI 기술을 활용한 사용자 서비스 설계",
    tags: ["#AI/생성기술"],
    category: ["Tech", "Math"]
  },

  {
    title: "UX 리서처",
    description: "사용자 경험 중심 리서치 및 분석",
    tags: ["#디자인/미적경험", "#창작/창의활동"],
    category: ["Engineering", "Tech"]
  },

  {
    title: "지속가능 소재 연구원",
    description: "생분해성 플라스틱, 대체 섬유 등 지속 가능한 소재 연구",
    tags: ["#환경/지속가능성"],
    category: ["Science"]
  },

  {
    title: "커뮤니티 플랫폼 개발자",
    description: "온라인 커뮤니티 인프라와 시스템 개발",
    tags: ["#커뮤니티/소셜네트워킹", "#창작/창의활동"],
    category: ["Tech", "Engineering"]
  },

  {
    title: "ESG 리포터",
    description: "기업 ESG 데이터 분석 및 보고서 작성",
    tags: ["#환경/지속가능성"],
    category: ["Math", "Science"]
  },

  {
    title: "디지털 헬스케어 기획자",
    description: "헬스케어 앱 기획 및 UX 설계",
    tags: ["#건강/웰니스", "#창작/창의활동"],
    category: ["Science", "Tech"]
  },

  {
    title: "패션 AI 분석가",
    description: "패션 트렌드 예측 AI 모델 개발",
    tags: ["#뷰티/패션", "#AI/생성기술", "#창작/창의활동"],
    category: ["Math", "Tech"]
  },

  {
    title: "환경 시뮬레이션 모델러",
    description: "환경 변화 시뮬레이션·수학적 모델링",
    tags: ["#환경/지속가능성", "#AI/생성기술"],
    category: ["Math", "Science"]
  },

  {
    title: "스마트홈 IoT 개발자",
    description: "가정용 IoT 기기 설계 및 개발",
    tags: ["#AI/생성기술"],
    category: ["Engineering", "Tech"]
  }
];

const cardContainer = document.querySelector('.card_container');

// 관심사 기반으로 매칭 점수 계산 + 정렬
const matchedJobs = jobs
  .map(job => ({
    ...job,
    score: job.tags.filter(tag => userData.interests.includes(tag)).length
  }))
  .sort((a, b) => b.score - a.score)
  .filter(job => job.score > 0)
  .slice(0, 3); // 최대 3개만 보여주기

cardContainer.innerHTML = "";

matchedJobs.forEach((job, idx) => {
  const card = document.createElement('div');
  card.classList.add('job_card');

  card.innerHTML = `
    <div class="index_badge">${idx + 1}/3</div>
    <h2>${job.title}</h2>
    <div class="job_tags">
      ${job.tags.map(tag => `<span>${tag}</span>`).join('')}
    </div>
    <div class="job_desc">${job.description}</div>
<div class="badge_group">
  ${job.category.map(cat => `<span class="badge ${cat.toLowerCase()}">${cat}</span>`).join('')}
</div>
    <button class="detail_btn">
    보러 가기
    <img src="${GO_ICON_URL}" alt=">" class="go"/>
    </button>
  `;

  cardContainer.appendChild(card);
});


const tagContainer = document.querySelector('.tags');
tagContainer.innerHTML = "";

userData.interests.forEach(tag => {
  const btn = document.createElement('button');
  btn.classList.add('tag');
  btn.textContent = tag;
  tagContainer.appendChild(btn);
});

function updateActiveCard() {
  const cards = document.querySelectorAll('.job_card');
  const containerCenter = cardContainer.scrollLeft + cardContainer.offsetWidth / 2;

  cards.forEach(card => {
    const cardCenter = card.offsetLeft + card.offsetWidth / 2;
    const distance = Math.abs(containerCenter - cardCenter);
    if (distance < card.offsetWidth / 2) {
      card.classList.add('active');
    } else {
      card.classList.remove('active');
    }
  });
}

cardContainer.addEventListener('scroll', () => {
  window.requestAnimationFrame(updateActiveCard);
});

window.addEventListener('load', updateActiveCard); // 처음 진입 시에도 적용

});