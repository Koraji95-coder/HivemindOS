<template>
  <section>
    <h2>Agent Chain 🔁</h2>

    <!-- 🧠 Multi-agent prompt -->
    <textarea v-model="input" placeholder="Type your chain command..."></textarea>

    <!-- 🚀 Trigger backend call -->
    <button @click="runChain">▶️ Run Chain</button>

    <!-- 📥 Output from the backend -->
    <pre class="output">{{ output }}</pre>
  </section>
</template>

<script>
export default {
  name: "ChainPanel",
  data() {
    return {
      input: "", // ✍ User command
      output: "", // 📥 API reply
    };
  },
  methods: {
    // 🔗 POST to chain executor
    async runChain() {
      this.output = "⏳ Running chain...";
      try {
        const res = await fetch("/api/chain/run", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ prompt: this.input }),
        });
        const data = await res.json();
        this.output = JSON.stringify(data, null, 2);
      } catch (err) {
        this.output = "⚠️ Chain execution failed.";
        console.error(err);
      }
    },
  },
};
</script>
