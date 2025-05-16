export async function renderAtlasControls(containerId) {
  const el = document.getElementById(containerId);

  el.innerHTML = `
    <label for="modeSelect">🔧 Set Mode:</label>
    <select id="modeSelect">
      <option value="development">Development</option>
      <option value="maintenance">Maintenance</option>
      <option value="restricted">Restricted</option>
    </select>
    <button id="setModeBtn">Apply</button>
    <div id="modeStatus">Status: (not set)</div>
  `;

  document.getElementById("setModeBtn").onclick = async () => {
    const mode = document.getElementById("modeSelect").value;

    const res = await fetch("/api/atlas/mode", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ mode })
    });

    const data = await res.json();
    document.getElementById("modeStatus").textContent = `✅ Set mode to: ${data.mode}`;
  };
}
