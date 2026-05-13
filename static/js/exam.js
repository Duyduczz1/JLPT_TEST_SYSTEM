document.querySelectorAll('.option input').forEach((input) => {
  input.addEventListener('change', () => {
    document.querySelectorAll(`input[name="${input.name}"]`).forEach((item) => {
      item.closest('.option').classList.remove('selected');
    });
    input.closest('.option').classList.add('selected');
  });
});
