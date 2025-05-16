<template>
  <div>
    <!-- 🧠 App Header -->
    <header>
      <h1>🧠 HivemindOS {{ version }}</h1>
      <!-- 🧭 Navigation Buttons -->
      <nav>
        <button
          v-for="tab in tabs"
          :key="tab"
          :class="{ 'active-tab': current === tab }"
          @click="current = tab"
        >
          {{ capitalize(tab) }}
        </button>
      </nav>
    </header>

    <main>
      <!-- 🧠 Dynamic Agent Tabs -->
      <AgentPanel
        v-if="current === 'bart'"
        name="Bart"
        route="bart"
        emoji="📊"
      />

      <AgentPanel
        v-if="current === 'daphne'"
        name="Daphne"
        route="daphne"
        emoji="💬"
      />

      <AgentPanel
        v-if="current === 'cortexa'"
        name="Cortexa"
        route="cortexa"
        emoji="🧬"
      />

      <AgentPanel
        v-if="current === 'atlas'"
        name="Atlas"
        route="atlas"
        emoji="🛡️"
      />

      <AgentPanel
        v-if="current === 'chain'"
        name="Chain"
        route="chain"
        emoji="🔗"
      />
    </main>

    <!-- 🦶 Footer -->
    <footer>
  <small>HivemindOS UI © 2025 — {{ version }}</small>
</footer>

  </div>
</template>

<script>
// 🧩 Import the reusable agent component
import AgentPanel from "./components/AgentPanel.vue";
import AtlasPanel from "./components/AtlasPanel.vue";
import ChainPanel from "./components/ChainPanel.vue";    

export default {
  name: "App",
  components: {
    AgentPanel,
    AtlasPanel,
    ChainPanel,
  },
  data() {
    return {
      // 🧭 Active tab name
      current: "bart",

      // 📋 List of agents
      tabs: ["bart", "daphne", "cortexa", "atlas", "chain"],
      version: "v?.?",
    };
  },
  methods: {
    // 🔡 Capitalizes the tab name for buttons
    capitalize(name) {
      return name.charAt(0).toUpperCase() + name.slice(1);
    },
  },
mounted() {
    // ✅ Fetch version from backend as soon as app starts
    fetch("/api/atlas")
      .then((res) => res.json())
      .then((data) => {
        this.version = data.version || "v?.?";
      })
      .catch(() => {
        this.version = "unknown";
      });
  },
};
</script>

<style>
@import "./assets/styles.css";
</style>
