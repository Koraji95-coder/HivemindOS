export async function renderMoodRing(containerId) {
  const el = document.getElementById(containerId);
  el.textContent = "🔄 Loading mood...";

  try {
    const res = await fetch("/api/state/mood");
    const { mood, user } = await res.json();

    const emoji = {
      sad: "😢", frustrated: "😠", happy: "😄", excited: "⚡", neutral: "😐", undefined: "❓"
    }[mood] || "🤖";

    el.innerHTML = `<strong>${emoji}</strong> ${user} is feeling <em>${mood}</em>`;
  } catch (err) {
    el.textContent = "❌ Mood fetch failed.";
  }
}
