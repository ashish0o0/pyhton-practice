function toggleDarkMode() {
  document.body.classList.toggle('dark');
  localStorage.setItem('theme', document.body.classList.contains('dark') ? 'dark' : 'light');
}

function loadTheme() {
  const theme = localStorage.getItem('theme');
  if (theme === 'dark') {
    document.body.classList.add('dark');
  }
}

window.onload = () => {
  loadTheme();
};

function append(value) {
  display.value += value;
}

function calculate() {
  try {
    const expression = display.value;
    const result = eval(expression);
    const record = `${expression} = ${result}`;
    addToHistory(record);
    display.value = result;
    historyIndex = -1; // reset arrow navigation
  } catch {
    display.value = 'Error';
  }
}

function clearDisplay() {
  display.value = '';
}

function addToHistory(entry) {
  let history = JSON.parse(localStorage.getItem('calcHistory')) || [];
  history.unshift(entry); // newest first
  localStorage.setItem('calcHistory', JSON.stringify(history));
  renderHistory();
}

function renderHistory() {
  const history = JSON.parse(localStorage.getItem('calcHistory')) || [];
  historyList.innerHTML = '';
  history.forEach(item => {
    const div = document.createElement('div');
    div.textContent = item;
    historyList.appendChild(div);
  });
}

window.onload = () => {
  loadTheme();
  renderHistory();
};

document.addEventListener('keydown', (e) => {
  const key = e.key;

  if (/\d/.test(key) || ['+', '-', '*', '/', '%', '.', '(', ')'].includes(key)) {
    append(key);
  } else if (key === 'Enter') {
    e.preventDefault();  // prevents form submission or refresh
    calculate();
  } else if (key === 'Backspace') {
    display.value = display.value.slice(0, -1);
  } else if (key === 'Escape') {
    clearDisplay();
  } else if (key === 'ArrowUp') {
    navigateHistory(-1);
  } else if (key === 'ArrowDown') {
    navigateHistory(1);
  }
});

let historyIndex = -1;

function navigateHistory(direction) {
  const history = JSON.parse(localStorage.getItem('calcHistory')) || [];
  if (history.length === 0) return;

  historyIndex += direction;

  if (historyIndex < 0) historyIndex = 0;
  if (historyIndex >= history.length) historyIndex = history.length - 1;

  const expression = history[historyIndex].split('=')[0].trim();
  display.value = expression;
}
