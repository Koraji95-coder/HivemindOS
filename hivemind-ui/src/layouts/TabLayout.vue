<template>
  <main>
    <!-- 🧭 Tab Buttons -->
    <nav>
      <button
        v-for="tab in tabs"
        :key="tab.name"
        :class="{ 'active-tab': tab.name === currentTab }"
        :aria-current="tab.name === currentTab ? 'page' : null"
        @click="$emit('update:currentTab', tab.name)"
      >
        <span>{{ tab.emoji }}</span> {{ tab.label }}
      </button>
    </nav>

    <!-- 🎯 Slot-based dynamic content -->
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
      required: true,
    },
    currentTab: {
      type: String,
      required: true,
    },
  },
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
  padding: 0.75rem 1.5rem; /* bigger buttons */
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 500;
  transition: all 0.2s ease; /* smooth hover effect */
  font-size: 1rem;
}

/* Hover effect */
nav button:hover {
  background-color: #333;
  transform: scale(1.05); /* grows a little on hover */
}

/* The active tab (current panel) */
nav button.active-tab {
  background-color: #00bfa5; /* nice teal green */
  box-shadow: 0 0 8px rgba(0, 191, 165, 0.6); /* glow */
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

@media (max-width: 600px) {
  nav {
    flex-direction: column;
    align-items: center;
  }

  nav button {
    width: 90%;
    font-size: 0.95rem;
    margin-bottom: 0.5rem;
  }
}
</style>
