<template>
  <div>
    <!-- 💡 Top Bar / Branding -->
    <header>
      <h1>🧠 HivemindOS UI</h1>
    </header>

    <!-- 🔁 Tab Shell -->
    <TabLayout :tabs="tabs" :currentTab="currentTab" @update:currentTab="currentTab = $event">
      <!-- 💬 Dynamic injection of active tab component -->
      <component :is="currentView" @switch="currentTab = $event" />
    </TabLayout>

    <!-- 📦 Version -->
    <footer>
      <small>HivemindOS v{{ version }}</small>
    </footer>
  </div>
</template>

<script>
import TabLayout from "./components/TabLayout.vue"; //Tab Shell
import { version } from "./version.js";

// Panels
import HomePanel from "./views/HomePanel.vue"; //Home
import BartPanel from "./views/BartPanel.vue";
import DaphnePanel from "./views/DaphnePanel.vue";
import CortexaPanel from "./views/CortexaPanel.vue";
import AtlasPanel from "./views/AtlasPanel.vue";
import ChainPanel from "./views/ChainPanel.vue"; // ✅ Moved from components/

export default {
  name: "App",
  components: {
    TabLayout,
    HomePanel,
    BartPanel,
    DaphnePanel,
    CortexaPanel,
    AtlasPanel,
    ChainPanel,
  },
  data() {
    return {
      currentTab: sessionStorage.getItem("active-tab") || "home", // 🔄 Restore if available
      version,
      tabs: [
        { name: "home", label: "Home", emoji: "🏠" },
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
        return {
            home: "HomePanel",
            bart: "BartPanel",
            daphne: "DaphnePanel",
            cortexa: "CortexaPanel",
            atlas: "AtlasPanel",
            chain: "ChainPanel",
        }[this.currentTab] || "GenericAgentPanel";
    }
  },
  watch: {
    currentTab(newTab) {
      sessionStorage.setItem("active-tab", newTab); // 💾 Save tab
    },
  },
};
</script>

<style>
@import "./assets/styles.css";
</style>
