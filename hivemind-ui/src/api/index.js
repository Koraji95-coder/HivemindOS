const BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000/api";

/**
 * Send prompt to an agent endpoint (e.g. bart, daphne, cortexa)
 * @param {string} agent - e.g. "bart"
 * @param {string} prompt
 * @returns {Promise<{response: string}>}
 */
export async function askAgent(agent, prompt) {
  const res = await fetch(`${BASE_URL}/${agent}/ask`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ prompt }),
  });
  if (!res.ok) throw new Error(await res.text());
  return await res.json();
}

// Example for chaining more endpoints:
export async function fetchAtlasState() {
  const res = await fetch(`${BASE_URL}/atlas`);
  if (!res.ok) throw new Error(await res.text());
  return await res.json();
}

// --- Authentication ---
export async function loginUser(email, password, code) {
  const res = await fetch(`${BASE_URL}/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password, code }),
  });
  return await res.json(); // {token, needs2fa, error}
}

export async function registerUser(email, password, pin) {
  const res = await fetch(`${BASE_URL}/auth/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password, pin }),
  });
  return await res.json();
}

export async function requestPasswordReset(email) {
  const res = await fetch(`${BASE_URL}/auth/request_reset`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email }),
  });
  return await res.json();
}