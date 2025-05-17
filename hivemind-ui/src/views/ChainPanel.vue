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

    <!-- 🧠 User Input Run Agent Chain-->
    <textarea v-model="input" placeholder="Run a chain..."></textarea>
    <button @click="runChain">▶️ Execute</button>

    <!-- 📤 Output display -->
    <pre class="output">{{ output }}</pre>
  </section>
</template>

<script>
import { useToast } from "vue-toastification";
const toast = useToast();
toast.success("🚀 It Works!");

export default {
  name: "ChainPanel",
  data() {
     return {
      input: "",       // 🧠 User prompt
      output: "",      // 📥 Backend response
      toast: null,     // 🔔 Toast ref
    };
  },
  mounted() {
    this.toast = useToast();  // 🔌 Initialize toast on mount
  },
  methods: {
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
        this.toast.success("✅ Chain executed successfully.");
      } catch (err) {
        this.output = "❌ Chain execution failed.";
        this.toast.error("🚨 Failed to run chain.");
        console.error(err);
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
