<template>
  <section>
    <h2>Atlas 🛡️</h2>

    <!-- 🔄 Refresh button -->
    <button @click="loadState">🔁 Refresh System Snapshot</button>

    <!-- 🧠 Display current system state -->
    <pre>{{ system }}</pre>
  </section>
</template>

<script>
export default {
  name: "AtlasPanel",
  data() {
    return {
      system: "Loading...", // 🧠 Output placeholder
    };
  },
  methods: {
    // 🌐 Calls backend to fetch Atlas state (/api/atlas)
    async loadState() {
      this.system = "⏳ Loading...";
      try {
        const res = await fetch("/api/atlas");
        const data = await res.json();
        this.system = JSON.stringify(data, null, 2); // 📋 Prettified JSON
      } catch (err) {
        this.system = "🚨 Failed to fetch Atlas state.";
        console.error(err);
      }
    },
  },
  mounted() {
    this.loadState(); // 🔄 Auto-run on mount
  },
};
</script>
