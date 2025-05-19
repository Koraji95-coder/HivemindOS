<template>
  <section>
    <h2>{{ name }} <span v-if="emoji">{{ emoji }}</span></h2>

    <div class="output" ref="outputRef">
      <span v-if="loading" class="typing">
        ⏳ Thinking<span class="dot">.</span><span class="dot">.</span><span class="dot">.</span>
      </span>
      <span v-else>{{ output }}</span>
    </div>

    <input :placeholder="`Ask ${name}...`" v-model="input" />
    <button @click="sendPrompt">Send</button>

    <button @click="showHistory = !showHistory">🧠 View History</button>
    <button @click="clearHistory">🧼 Clear</button>

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

<script>
export default {
  name: "AgentPanel",
  props: ["name", "route", "emoji"],

  data() {
    return {
      input: "",
      output: "",
      loading: false,
      showHistory: false,
      history: [],
    };
  },

  computed: {
    historyKey() {
      return `hivemind-history-${this.route}`;
    },
  },

  methods: {
    async sendPrompt() {
      this.loading = true;
      this.output = "";

      try {
        const res = await fetch(`/api/${this.route}`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ prompt: this.input }),
        });

        if (!res.ok) throw new Error(`Server ${res.status}`);
        const data = await res.json();

        this.output = data.response || "⚠️ No response";

        const log = {
          prompt: this.input,
          response: data.response,
          timestamp: new Date().toISOString(),
        };

        const stored = JSON.parse(sessionStorage.getItem(this.historyKey)) || [];
        stored.push(log);
        sessionStorage.setItem(this.historyKey, JSON.stringify(stored));
        this.history = stored;

        await fetch("/api/logs/save", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(log),
        });
      } catch (err) {
        this.output = "❌ Error contacting agent.";
        console.error("🛑 Agent Error:", err);
      } finally {
        this.loading = false;
      }
    },

    clearHistory() {
      sessionStorage.removeItem(this.historyKey);
      this.history = [];
    },

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

  mounted() {
    this.loadLastSession();
  },
};
</script>

<style scoped>
.output {
  padding: 1rem;
  min-height: 100px;
  background: #f6f6f6;
  border: 1px solid #ddd;
  margin-bottom: 1rem;
}
.typing .dot {
  animation: blink 1.2s infinite;
}
@keyframes blink {
  0%, 100% { opacity: 0.2; }
  50% { opacity: 1; }
}
</style>
