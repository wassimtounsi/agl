function showMessage(message) {
  alert(message);
}
document.getElementById('submit-today-menu').addEventListener('click', function() {
  showMessage('Today\'s menu submitted successfully!');
});

document.getElementById('submit-tomorrow-menu').addEventListener('click', function() {
  showMessage('Tomorrow\'s menu submitted successfully!');
});
