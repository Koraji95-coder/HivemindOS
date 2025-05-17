<!-- ====================== -->
<!-- 🧱 TabLayout.vue -->
<!-- Generic slot-based tab layout container -->
<!-- ====================== -->
<template>
  <main>
    <!-- 🧭 Tab Buttons -->
    <nav>
      <button
        v-for="tab in tabs"
        :key="tab.name"
        :class="{ 'active-tab': tab.name === currentTab }"
        @click="$emit('update:currentTab', tab.name)"
      >
        <span>{{ tab.emoji }}</span> {{ tab.label }}
      </button>
    </nav>

    <!-- 🎯 Active tab content (from parent <component>) -->
    <section class="tab-content">
      <slot />
    </section>
  </main>
</template>

<script>
export default {
  name: "TabLayout",
  props: {
    tabs: {
      type: Array,
      required: true
    },
    currentTab: {
      type: String,
      required: true
    }
  }
};
</script>

<style scoped>
/* ========================== */
/* 🧬 Tab Navigation Styling */
/* ========================== */
nav {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

nav button {
  background: #222;
  color: #eee;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 500;
  transition: all 0.2s ease;
}

nav button:hover {
  background-color: #333;
}

nav button.active-tab {
  background-color: #009688;
  font-weight: bold;
}

/* ========================== */
/* 🧾 Tab Panel Wrapper */
/* ========================== */
.tab-content {
  background: #1b1b1b;
  padding: 1rem;
  border-radius: 6px;
  border: 1px solid #333;
}
</style>
