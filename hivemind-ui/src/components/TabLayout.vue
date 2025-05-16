<!-- TabLayout.vue -->
<template>
  <div class="tab-layout">
    <header>
      <h1>🧠 HivemindOS v0.2.0</h1>

      <!-- 🧭 Navigation buttons -->
      <nav>
        <button
          v-for="tab in tabs"
          :key="tab"
          :class="{ 'active-tab': current === tab }"
          @click="$emit('update:current', tab)" <!-- 🔁 Sync selected tab -->
        >
          {{ capitalize(tab) }}
        </button>
      </nav>
    </header>

    <main>
      <slot /> <!-- 🔌 Injected content from App.vue (panels) -->
    </main>

    <footer>
      <small>HivemindOS UI © 2025 — <span id="version-tag">loading...</span></small>
    </footer>
  </div>
</template>

<script>
export default {
  name: "TabLayout",
  props: {
    current: String, // 🔁 Active tab (two-way bound)
    tabs: Array,     // 📋 Tab list to render
  },
  methods: {
    capitalize(name) {
      return name.charAt(0).toUpperCase() + name.slice(1);
    },
  },
};
</script>
