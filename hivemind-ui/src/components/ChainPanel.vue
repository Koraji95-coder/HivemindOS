<template>
  <section>
    <h2>Agent Chain 🔁</h2>

    <!-- 🧱 Step-by-step agent sequence -->
    <div v-for="(step, index) in chain" :key="index" class="step">
      <label>Step {{ index + 1 }}</label>
      <select v-model="step.agent">
        <option disabled value="">Choose agent</option>
        <option value="bart">Bart</option>
        <option value="daphne">Daphne</option>
        <option value="cortexa">Cortexa</option>
      </select>
      <input v-model="step.prompt" placeholder="Prompt for this agent..." />
    </div>

    <!-- ➕ Add step -->
    <button @click="addStep">➕ Add Step</button>

    <!-- 🌐 Base input shared by chain -->
    <textarea v-model="baseInput" placeholder="Shared input (optional)"></textarea>

    <!-- 🚀 Run agent chain -->
    <button @click="runChain">▶️ Run Chain</button>

    <!-- 📤 Output display -->
    <pre class="output">{{ output }}</pre>
  </section>
</template>

<script>
export default {
  name: "ChainPanel",
  data() {
    return {
      baseInput: "", // 👥 Shared initial input
      chain: [
        { agent: "", prompt: "" }, // 🧠 Each step: agent + their specific prompt
      ],
      output: "",
    };
  },
  methods: {
    // ➕ Add another agent-prompt step
    addStep() {
      this.chain.push({ agent: "", prompt: "" });
    },

    // 🔁 Run the full chain
    async runChain() {
      this.output = "⏳ Running agent chain...";
      try {
        const response = await fetch("/api/chain/run", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            input: this.baseInput,
            chain: this.chain,
          }),
        });

        const data = await response.json();
        this.output = JSON.stringify(data, null, 2);
      } catch (error) {
        console.error("❌ Chain error:", error);
        this.output = "⚠️ Chain execution failed.";
      }
    },
  },
};
</script>

<style scoped>
.step {
  margin-bottom: 1rem;
  padding: 0.5rem;
  background: #1a1a1a;
  border: 1px solid #333;
  border-radius: 6px;
}
select,
input {
  margin-top: 0.25rem;
  margin-right: 0.5rem;
  background: #222;
  color: white;
  padding: 0.3rem;
  border: 1px solid #444;
}
</style>
