const timer = document.getElementById('timer');
if (timer) {
  let seconds = Number(timer.dataset.minutes || 20) * 60;
  const tick = () => {
    const minutes = String(Math.floor(seconds / 60)).padStart(2, '0');
    const rest = String(seconds % 60).padStart(2, '0');
    timer.textContent = `${minutes}:${rest}`;
    if (seconds <= 0) {
      const form = document.querySelector('.exam-form');
      if (form) form.submit();
      return;
    }
    seconds -= 1;
  };
  tick();
  setInterval(tick, 1000);
}
