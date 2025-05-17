<template>
  <section>
    <h2>{{ name }} <span v-if="emoji">{{ emoji }}</span></h2>

    <!-- 🔄 Manual refresh -->
    <button @click="loadState">🔁 Refresh System Snapshot</button>

    <!-- 🧠 System diagnostics output -->
    <pre>{{ system }}</pre>
  </section>
</template>

<script>
import { useToast } from "vue-toastification";
import { PanelSettings } from "@/config/panelSettings.js";


export default {
  name: "AtlasPanel",
  props: ["name", "route", "emoji"],
  data() {
    return {
      system: "Loading...",
      toast: null,
    };
  },
  mounted() {
    this.toast = useToast();

    const config = panelSettings["atlas"];
    if (config?.heartbeat) {
      this.loadState();
    }
  },
  methods: {
    async loadState() {
      this.system = "⏳ Loading...";
      try {
        const res = await fetch("/api/atlas");
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        const data = await res.json();
        this.system = JSON.stringify(data, null, 2);
        this.toast.success("✅ Atlas system loaded.");
      } catch (err) {
        this.system = "🚨 Failed to fetch Atlas state.";
        this.toast.error("❌ Atlas failed to load.");
        console.error(err);
      }
    },
  },
};
</script>

<style scoped>
button {
  margin-bottom: 1rem;
  background: #222;
  color: #fff;
  border: 1px solid #444;
  padding: 0.5rem 1rem;
  border-radius: 4px;
}
pre {
  background: #111;
  color: #0f0;
  padding: 1rem;
  white-space: pre-wrap;
  font-size: 0.9rem;
  border-radius: 6px;
  border: 1px solid #333;
}
</style>
