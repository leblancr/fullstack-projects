// polls/static/polls/script.js
document.addEventListener("DOMContentLoaded", function() {
  // Restore saved background (no flash-critical logic here)
  const savedBg = localStorage.getItem("background");
  if (savedBg) {
    document.body.style.backgroundImage = `url('${savedBg}')`;
  }

  // Only handle clicking items to change background and save choice.
  document.querySelectorAll(".bg-menu li").forEach(li => {
    li.addEventListener("click", () => {
      const bgUrl = li.dataset.bg;
      if (!bgUrl) return;
      document.body.style.backgroundImage = `url('${bgUrl}')`;
      localStorage.setItem("background", bgUrl);
    });
  });
});
