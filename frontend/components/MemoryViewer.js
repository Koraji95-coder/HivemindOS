export async function renderMemory(containerId) {
  const el = document.getElementById(containerId);
  el.textContent = "🔄 Loading memory...";

  try {
    const res = await fetch("/api/state/memory");
    const json = await res.json();

    el.textContent = JSON.stringify(json, null, 2);
  } catch (err) {
    el.textContent = "❌ Failed to load session memory.";
  }
}
