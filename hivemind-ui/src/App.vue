<template>
  <div>
    <!-- 🧠 App Header -->
    <header>
      <h1>🧠 HivemindOS v0.2.0</h1>
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
    </main>

    <!-- 🦶 Footer -->
    <footer>
      <small>HivemindOS UI &copy; 2025 – <span id="version-tag">v0.2.0</span></small>
    </footer>
  </div>
</template>

<script>
// 🧩 Import the reusable agent component
import AgentPanel from "./components/AgentPanel.vue";

export default {
  name: "App",
  components: {
    AgentPanel,
  },
  data() {
    return {
      // 🧭 Active tab name
      current: "bart",

      // 📋 List of agents
      tabs: ["bart", "daphne", "cortexa"],
    };
  },
  methods: {
    // 🔡 Capitalizes the tab name for buttons
    capitalize(name) {
      return name.charAt(0).toUpperCase() + name.slice(1);
    },
  },
};
</script>

<style>
@import "./assets/styles.css";
</style>
