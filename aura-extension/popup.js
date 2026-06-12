// Tab Switching System
document.getElementById('tab-link').addEventListener('click', () => switchTab('link'));
document.getElementById('tab-manual').addEventListener('click', () => switchTab('manual'));

function switchTab(type) {
  document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
  
  if (type === 'link') {
    document.getElementById('tab-link').classList.add('active');
    document.getElementById('panel-link').classList.add('active');
  } else {
    document.getElementById('tab-manual').classList.add('active');
    document.getElementById('panel-manual').classList.add('active');
  }
}

// Action Trigger Listeners
document.getElementById('analyze-url-btn').addEventListener('click', analyzeUrl);
document.getElementById('analyze-manual-btn').addEventListener('click', analyzeManualText);

function analyzeUrl() {
  const url = document.getElementById('post-url').value;
  if (!url) return alert("Please enter a valid link.");
  
  sendToBackend({ type: "url", data: url });
}

function analyzeManualText() {
  const text = document.getElementById('manual-text').value;
  if (!text) return alert("Please enter some text to analyze.");
  
  sendToBackend({ type: "text", data: text });
}

function sendToBackend(payload) {
  const chartContainer = document.getElementById('results-chart');
  resetGraph();

// Ensure this line uses 8080
    fetch("http://127.0.0.1:8080/analyze", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
    })
  .then(res => {
    if (!res.ok) throw new Error(`Server returned status: ${res.status}`);
    return res.json();
  })
  .then(data => {
    chartContainer.style.display = "block";
    setTimeout(() => {
      animateBar('pos', data.positive);
      animateBar('neu', data.neutral);
      animateBar('neg', data.negative);
    }, 50);
  })
  .catch(err => {
    alert("Connection error. Check your terminal to confirm Flask is actively listening on port 5000.");
    console.error(err);
  });
}

function animateBar(id, value) {
  document.getElementById(`bar-${id}`).style.width = `${value}%`;
  document.getElementById(`txt-${id}`).innerText = `${Math.round(value)}%`;
}

function resetGraph() {
  document.getElementById('bar-pos').style.width = "0%";
  document.getElementById('bar-neu').style.width = "0%";
  document.getElementById('bar-neg').style.width = "0%";
}