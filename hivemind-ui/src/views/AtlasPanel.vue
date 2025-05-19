<template>
  <section>
    <h2>🛡️ Atlas System</h2>

    <!-- Show login panel if not authenticated -->
    <LoginPanel v-if="!authenticated" @logged-in="loadState" @registered="onRegistered" />

    <!-- Show system admin/dashboard if logged in -->
    <div v-else>
      <button @click="logout">🚪 Logout</button>
      <button @click="loadState">🔁 Refresh System Snapshot</button>
      <pre>{{ system }}</pre>
    </div>
  </section>
</template>

<script>
import { fetchAtlasState } from "@/api";
import LoginPanel from "./LoginPanel.vue";

export default {
  name: "AtlasPanel",
  components: { LoginPanel },
  data() {
    return {
      authenticated: false,
      user: null,      // can be loaded from backend or local storage
      system: "Loading...",
    };
  },
  async mounted() {
    // On mount, check Auth status
    await this.checkAuth();
  },
  methods: {
    async checkAuth() {
      // Mock: Check for a token/local session
      // Real: Call backend /api/system/user_status (&/or check JWT)
      const token = localStorage.getItem("authToken");
      if (!token) {
        this.authenticated = false;
        return;
      }
      // Optionally, verify token w/backend and load user info
      // let res = await fetch("/api/system/user_status", ...);
      this.authenticated = true;
      // (set this.user if needed)
      this.loadState();
    },
    async loadState() {
      this.system = "⏳ Loading...";
      try {
        const data = await fetchAtlasState();
        this.system = JSON.stringify(data, null, 2);
      } catch (err) {
        this.system = "🚨 Failed to fetch Atlas state.";
        console.error(err);
      }
    },
    logout() {
      localStorage.removeItem("authToken");
      this.authenticated = false;
      this.system = "Logged out!";
    },
    onRegistered() {
      // After register, can show message or prompt login
    }
  },
};
</script>