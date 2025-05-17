<!-- ========================= -->
<!-- 🏠 HomePanel.vue -->
<!-- Landing view / fallback safe zone -->
<!-- ========================= -->
<template>
  <section class="home">
    <h2>🏠 Welcome to HivemindOS</h2>
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
</template>

<script>
export default {
  name: "HomePanel",
};
</script>

<style scoped>
.home {
  line-height: 1.6;
  font-size: 1.05rem;
  padding: 1rem;
}
</style>
