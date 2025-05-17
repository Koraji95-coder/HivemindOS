<!-- ====================== -->
<!-- 🧠 AGENT PANEL UI LAYOUT -->
<!-- ====================== -->
<template>
  <section>
    <!-- 🔤 Agent name and emoji header -->
    <h2>{{ name }} <span v-if="emoji">{{ emoji }}</span></h2>

    <!-- 🖥️ OUTPUT DISPLAY AREA -->
    <div class="output" ref="outputRef">
      <!-- ⏳ Show animation while waiting -->
      <span v-if="loading" class="typing">
        ⏳ Thinking<span class="dot">.</span><span class="dot">.</span><span class="dot">.</span>
      </span>
      <!-- ✅ Show output text once received -->
      <span v-else>{{ output }}</span>
    </div>

    <!-- 🧾 INPUT BOX + SEND BUTTON -->
    <input :placeholder="`Ask ${name}...`" v-model="input" />
    <button @click="sendPrompt">Send</button>

    <!-- 🧠 SESSION MEMORY: VIEW + CLEAR -->
    <button @click="showHistory = !showHistory">🧠 View History</button>
    <button @click="clearHistory">🧼 Clear</button>

    <!-- 🧾 PAST PROMPT HISTORY LIST -->
    <div v-if="showHistory" class="history">
      <h3>🗃️ Past Prompts</h3>
      <ul>
        <li v-for="entry in history" :key="entry.timestamp">
          🕒 {{ entry.timestamp }}<br />
          <strong>Prompt:</strong> {{ entry.prompt }}<br />
          <strong>Response:</strong> {{ entry.response }}
        </li>
      </ul>
    </div>
  </section>
</template>

<!-- ====================== -->
<!-- 🧠 LOGIC & MEMORY SCRIPT -->
<!-- ====================== -->
<script>
export default {
  name: "AgentPanel",

  // 📥 Props from parent component
  props: ["name", "route", "emoji"],

  // 📦 Local state variables
  data() {
    return {
      input: "",                        // 📝 Current prompt
      output: "",                       // 📤 Last response
      loading: false,                   // ⏳ Loading state
      showHistory: false,               // 👁️ Show/hide history
      history: [],                      // 🧠 Full log list
      historyKey: `hivemind-history-${this.route}`, // 🧠 Storage key per agent
    };
  },

  methods: {
    // 🚀 SEND AGENT PROMPT
    async sendPrompt() {
      this.loading = true;
      this.output = "";

      try {
        // 🌐 POST to backend
        const res = await fetch(`/api/${this.route}`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ prompt: this.input }),
        });

        const data = await res.json();
        this.output = data.response || "⚠️ No response";

        // 💾 Save to sessionStorage
        const log = {
          prompt: this.input,
          response: data.response,
          timestamp: new Date().toISOString(),
        };
        const stored = JSON.parse(sessionStorage.getItem(this.historyKey)) || [];
        stored.push(log);
        sessionStorage.setItem(this.historyKey, JSON.stringify(stored));
        this.history = stored;

        // 🧠 Optional: Persist to backend for long-term logs
        await fetch("/api/logs/save", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(log),
        });

      } catch (err) {
        this.output = "❌ Error contacting agent.";
        console.error(err);
      } finally {
        this.loading = false;
      }
    },

    // 🧽 CLEAR SESSION HISTORY
    clearHistory() {
      sessionStorage.removeItem(this.historyKey);
      this.history = [];
    },

    // ♻️ RESTORE LAST SESSION
    loadLastSession() {
      const stored = JSON.parse(sessionStorage.getItem(this.historyKey)) || [];
      this.history = stored;

      if (stored.length > 0) {
        const last = stored[stored.length - 1];
        this.input = last.prompt;
        this.output = last.response;
      }
    },
  },

  // 🚦 ON MOUNT, LOAD LAST MEMORY
  mounted() {
    this.loadLastSession();
  },
};
</script>

<!-- ====================== -->
<!-- 🎨 STYLES (OPTIONAL) -->
<!-- ====================== -->
<style scoped>
/* Add scoped style overrides here if needed */
</style>
