<!-- ========================= -->
<!-- 🏠 HomePanel.vue -->
<!-- Landing view / fallback safe zone -->
<!-- ========================= -->
<template>
    <transition name="fade">
        <section class="home">
            <h2 tabindex="0">🏠 Welcome to HivemindOS</h2>
            <p>This is your central command hub.</p>

            <ul>
            <li>📊 Use <strong>Bart</strong> for market insights.</li>
            <li>💬 Talk to <strong>Daphne</strong> for meeting notes and summaries.</li>
            <li>🧬 Ask <strong>Cortexa</strong> for research or analysis.</li>
            <li>🛡️ <strong>Atlas</strong> shows your system state.</li>
            <li>🔗 Use <strong>Chain</strong> to execute multi-agent workflows.</li>
            </ul>

            <p style="margin-top: 1rem;">More modules coming soon...</p>
        </section>
  </transition>
</template>

<script>
export default {
  name: "HomePanel",
};
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
.home {
  line-height: 1.75;
  font-size: 1.1rem;
  padding: 1.5rem;
  max-width: 600px;
  margin: auto;
}
</style>
