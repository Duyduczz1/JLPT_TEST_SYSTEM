document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.flash').forEach((flash) => {
    setTimeout(() => {
      flash.style.display = 'none';
    }, 3500);
  });
});
