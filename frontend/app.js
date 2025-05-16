// 🎛️ Tab switching logic
document.querySelectorAll("nav button").forEach(btn => {
  btn.addEventListener("click", () => {
    document.querySelectorAll(".tab").forEach(tab => tab.classList.remove("active"));
    document.getElementById(btn.dataset.tab).classList.add("active");
  });
});

// 🧠 Send prompt to agent
async function sendPrompt(agent) {
  const input = document.getElementById(`${agent}-input`).value;
  const output = document.getElementById(`${agent}-output`);
  output.textContent = "⏳ Thinking...";

  const response = await fetch(`/api/${agent}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ prompt: input }),
  });

  const result = await response.json();
  output.textContent = result.response || "⚠️ No response.";
}

// 🛡️ Load Atlas state
async function loadAtlas() {
  const pre = document.getElementById("atlas-output");
  pre.textContent = "⏳ Loading...";

  const res = await fetch("/api/atlas");
  const data = await res.json();
  pre.textContent = JSON.stringify(data, null, 2);
}

import { renderMoodRing } from './components/MoodRing.js';
import { renderMemory } from './components/MemoryViewer.js';
import { renderAtlasControls } from './components/AtlasControl.js';

// 🛡️ Mount diagnostics UI when Atlas tab is clicked
document.querySelector("[data-tab='atlas']").addEventListener("click", () => {
  renderMoodRing("mood-ring");
  renderMemory("memory-viewer");
  renderAtlasControls("atlas-controls");
});

