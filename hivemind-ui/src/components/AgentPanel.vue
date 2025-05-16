<template>
  <!-- 📦 This is the main HTML structure for the agent panel -->
  <section>
    <!-- 🧠 Title includes name + emoji -->
    <h2>{{ name }} <span v-if="emoji"> {{ emoji }}</span></h2>

    <!-- 📤 Output area: Shows agent response or loading dots -->
    <div class="output" ref="outputRef">
      <!-- ⏳ Show animated thinking dots while loading -->
      <span v-if="loading" class="typing">⏳ Thinking<span class="dot">.</span><span class="dot">.</span><span class="dot">.</span></span>
      
      <!-- ✅ Show response when ready -->
      <span v-else>{{ response }}</span>
    </div>

    <!-- 📝 Text input bound to `prompt` -->
    <input :placeholder="`Ask ${name}...`" v-model="input" />


    <!-- 🚀 Send button triggers `sendPrompt()` -->
    <button @click="sendPrompt">Send</button>
  </section>
</template>
