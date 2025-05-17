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
const toast = useToast();
toast.success("🚀 It Works!");

export default {
  name: "AtlasPanel",
  props: ["name", "route", "emoji"],
  data() {
    return {
      system: "Loading...",   // 📦 Output placeholder
      toast: null,            // 🔔 Toast reference
    };
  },
  mounted() {
    this.toast = useToast();  // 🔌 Bind toast on mount
    this.loadState();         // 🔄 Auto-run diagnostics
  },
  methods: {
    // 🌐 Load system diagnostics from /api/atlas
    async loadState() {
      this.system = "⏳ Loading...";
      try {
        const res = await fetch("/api/atlas");
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
/* 🎨 Optional: Add styling overrides if needed */
</style>
