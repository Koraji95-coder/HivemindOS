<template>
  <div>
    <!-- 💡 Top Bar / Branding -->
    <header>
      <h1>🧠 HivemindOS UI</h1>
    </header>

    <!-- 🔁 Tab Shell -->
    <TabLayout 
        :tabs="tabs"
        :currentTab="currentTab"
        @update:currentTab="currentTab = $event"
    >
        <!-- This changes what panel is shown when you click tabs -->
        <component :is="currentView" />
    </TabLayout>

    <!-- 📦 Version -->
    <footer>
      <small>HivemindOS v{{ version }}</small>
    </footer>
  </div>
</template>

<script>
import TabLayout from "@/layouts/TabLayout.vue";
import { version } from "./version.js";

import HomePanel from "./views/HomePanel.vue";
import BartPanel from "./views/BartPanel.vue";
import DaphnePanel from "./views/DaphnePanel.vue";
import CortexaPanel from "./views/CortexaPanel.vue";
import AtlasPanel from "./views/AtlasPanel.vue";
import ChainPanel from "./views/ChainPanel.vue";
import GenericAgentPanel from "./views/GenericAgentPanel.vue"; // ✅ Added fallback component

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
    GenericAgentPanel, // ✅ registered
  },
  data() {
    return {
      currentTab: sessionStorage.getItem("active-tab") || "home",
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
  mounted() {
    const sessionId = sessionStorage.getItem("session-id");
    if (!sessionId) {
      const newId = crypto.randomUUID?.() || Math.random().toString(36).substring(2); // ✅ safer fallback
      sessionStorage.setItem("session-id", newId);
      console.log("🔐 New session:", newId);
    } else {
      console.log("🔁 Resumed session:", sessionId);
    }
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
      }[this.currentTab] || "GenericAgentPanel"; // ✅ will now resolve properly
    },
  },
  watch: {
    currentTab(newTab) {
      sessionStorage.setItem("active-tab", newTab);
    },
  },
};
</script>

<style>
@import "./assets/styles.css";
</style>
