<!-- ====================== -->
<!-- 🧬 CortexaPanel.vue -->
<!-- ====================== -->
<template>
  <section>
    <h2>{{ name }} {{ emoji }}</h2>

    <!-- 🖥️ Output -->
    <div class="output">
      <span v-if="loading" class="typing">
        ⏳ Thinking<span class="dot">.</span><span class="dot">.</span><span class="dot">.</span>
      </span>
      <span v-else>{{ output }}</span>
    </div>

    <!-- ✍ Input + Send -->
    <input :placeholder="`Ask ${name}...`" v-model="input" />
    <button @click="sendPrompt">Send</button>

    <!-- 🧠 History Tools -->
    <button @click="showHistory = !showHistory">🧠 History</button>
    <button @click="clearHistory">🧼 Clear</button>

    <!-- 📜 Past History -->
    <div v-if="showHistory" class="history">
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
import { useToast } from "vue-toastification";
const toast = useToast();
toast.success("🚀 It Works!");

export default {
  name: "CortexaPanel",
  data() {
    return {
      name: "Cortexa",
      emoji: "🧬",
      route: "cortexa",
      input: "",
      output: "",
      loading: false,
      showHistory: false,
      history: [],
      historyKey: "hivemind-history-cortexa",
      toast: null,
    };
  },
  mounted() {
    this.toast = useToast();
    this.loadLastSession();
    this.toast.success("✅ CortexaPanel ready.");
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

        const data = await res.json();
        this.output = data.response || "⚠️ No response";

        // 🧠 Store locally
        const log = {
          prompt: this.input,
          response: data.response,
          timestamp: new Date().toISOString(),
        };
        const stored = JSON.parse(sessionStorage.getItem(this.historyKey)) || [];
        stored.push(log);
        sessionStorage.setItem(this.historyKey, JSON.stringify(stored));
        this.history = stored;

        // ☁️ Push to logs backend
        await fetch("/api/logs/save", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(log),
        });

        this.toast.success(`${this.name} responded.`);
      } catch (err) {
        this.output = "❌ Error";
        this.toast.error(`Failed to reach ${this.name}`);
        console.error(err);
      } finally {
        this.loading = false;
      }
    },

    clearHistory() {
      sessionStorage.removeItem(this.historyKey);
      this.history = [];
      this.toast("🧼 History cleared.");
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
};
</script>

<style scoped>
/* 🎨 Minimal scoped override if needed */
</style>
