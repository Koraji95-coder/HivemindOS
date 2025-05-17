<!-- ====================== -->
<!-- 🧠 App.vue -->
<!-- Core layout & routing -->
<!-- ====================== -->
<template>
  <div>
    <!-- 💡 Top Bar / Branding -->
    <header>
      <h1>🧠 HivemindOS UI</h1>
    </header>

    <!-- 🔁 Tab Manager Shell (tabs defined below) -->
    <TabLayout :tabs="tabs" :currentTab="currentTab" @update:currentTab="currentTab = $event">
      <!-- 💬 Injects matching component for active tab -->
      <component :is="currentView" />
    </TabLayout>

    <!-- 📦 Version Tag -->
    <footer>
      <small>HivemindOS v{{ version }}</small>
    </footer>
  </div>
</template>

<script>
import TabLayout from "./components/TabLayout.vue";

// 🧩 Agent Panels (modular)
import AgentPanel from "./components/AgentPanel.vue";
import AtlasPanel from "./components/AtlasPanel.vue";
import ChainPanel from "./components/ChainPanel.vue";

import { version } from "./version.js"; // 📦 Unified version file

export default {
  name: "App",
  components: {
    TabLayout,
    AgentPanel,
    AtlasPanel,
    ChainPanel,
  },
  data() {
    return {
      currentTab: "bart", // 🧭 Default tab on load
      version,            // 🔖 Pulled from version.js

      // 🧠 Registered views: auto-renders in <component :is="..." />
      tabs: [
        { name: "bart", label: "Bart", emoji: "📊" },
        { name: "daphne", label: "Daphne", emoji: "💬" },
        { name: "cortexa", label: "Cortexa", emoji: "🧬" },
        { name: "atlas", label: "Atlas", emoji: "🛡️" },
        { name: "chain", label: "Chain", emoji: "🔗" },
      ],
    };
  },
  computed: {
    currentView() {
      switch (this.currentTab) {
        case "bart": return "AgentPanel";
        case "daphne": return "AgentPanel";
        case "cortexa": return "AgentPanel";
        case "atlas": return "AtlasPanel";
        case "chain": return "ChainPanel";
        default: return "AgentPanel";
      }
    },
  },
};
</script>

<style>
@import "./assets/styles.css";
</style>
