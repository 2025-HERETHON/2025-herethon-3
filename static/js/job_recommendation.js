/* ---------- 0. DOM → jobs 배열 ---------- */
const cardContainer = document.querySelector('.card_container');
const cardElements = [...document.querySelectorAll('.job_card')];

const jobs = cardElements.map(card => ({
  title: card.querySelector('h2').textContent.trim(),
  description: card.querySelector('.job_desc').textContent.trim(),
  tags: (card.dataset.tags || '').split(',').map(t => t.trim()).filter(Boolean),
  category: (card.dataset.categories || '').split(',').map(c => c.trim()).filter(Boolean)
}));

/* ---------- 1. 매칭 점수 계산 ---------- */
const matchedJobs = jobs
  .map(job => ({
    ...job,
    score: job.tags.filter(tag => userData.interests.includes(tag)).length
  }))
  .filter(job => job.score > 0)
  .sort((a, b) => b.score - a.score)
  .slice(0, 3);

/* ---------- 2. 기존 카드 지우기 ---------- */
cardContainer.innerHTML = '';

/* ---------- 3. 상위 3개 렌더 ---------- */
matchedJobs.forEach((job, idx) => {
  const card = document.createElement('div');
  card.className = 'job_card';
  card.innerHTML = `
    <div class="index_badge">${idx + 1}/3</div>
    <h2>${job.title}</h2>

    <div class="job_tags">
      ${job.tags.map(t => `<span>${t}</span>`).join('')}
    </div>

    <div class="job_desc">${job.description}</div>

    <div class="badge_group">
      ${job.category.map(c => {
    const key = c.toLowerCase();
    return `<span class="badge ${key}">${c}</span>`;
  }).join('')}
    </div>

    <button class="detail_btn">
      보러 가기 <img src="${GO_ICON_URL}" class="go" alt=">">
    </button>
  `;

  cardContainer.appendChild(card);
});


/* ---------- 4. 스크롤 활성 카드 표시 ---------- */
function updateActiveCard() {
  const cards = document.querySelectorAll('.job_card');
  const center = cardContainer.scrollLeft + cardContainer.offsetWidth / 2;
  cards.forEach(card => {
    const cardCenter = card.offsetLeft + card.offsetWidth / 2;
    card.classList.toggle('active', Math.abs(center - cardCenter) < card.offsetWidth / 2);
  });
}
cardContainer.addEventListener('scroll', () => requestAnimationFrame(updateActiveCard));
window.addEventListener('load', updateActiveCard);
