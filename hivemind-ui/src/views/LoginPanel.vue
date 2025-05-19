<template>
  <div class="login-container">
    <h3 v-if="mode==='login'">🔐 System Login</h3>
    <h3 v-if="mode==='register'">📝 Register Account</h3>
    <h3 v-if="mode==='reset'">🔑 Reset Password</h3>

    <div v-if="mode!=='reset'">
      <input v-model="email" placeholder="Email" type="email" autocomplete="username" />
      <input v-model="password" placeholder="Password" type="password" autocomplete="current-password" />
    </div>

    <div v-if="mode==='register'">
      <input v-model="pin" placeholder="Set a PIN (optional)" type="text" maxlength="6" />
    </div>

    <div v-if="mode==='login' && step==='2fa'">
      <input v-model="code" placeholder="Enter 2FA code" />
    </div>

    <div class="actions">
      <button v-if="mode==='login'" @click="login">Login</button>
      <button v-if="mode==='register'" @click="register">Register</button>
      <button v-if="mode==='reset'" @click="requestReset">Send Reset</button>
    </div>

    <div class="links">
      <a v-if="mode==='login'" @click="mode='register'">Register</a> |
      <a v-if="mode==='login'" @click="mode='reset'">Forgot password?</a> |
      <a v-if="mode!=='login'" @click="mode='login'">Back to login</a>
    </div>

    <div v-if="error" class="error">{{ error }}</div>
    <div v-if="message" class="info">{{ message }}</div>
  </div>
</template>

<script>
import { loginUser, registerUser, requestPasswordReset } from "@/api";

export default {
  name: "LoginPanel",
  data() {
    return {
      mode: "login", // login, register, reset
      email: "",
      password: "",
      pin: "",
      code: "",
      error: "",
      message: "",
      step: "main",  // "main" or "2fa"
    };
  },
  methods: {
    async login() {
      this.error = "";
      this.message = "";
      try {
        // --- First login step (could be username+password only or request 2FA) ---
        const res = await loginUser(this.email, this.password, this.code);
        if (res.token) {
          localStorage.setItem("authToken", res.token);
          this.$emit("logged-in");
        } else if (res.needs2fa) {
          this.step = "2fa"; // Show 2FA input
          this.message = "Enter the code sent to your email/PIN app.";
        } else {
          this.error = res.error || "Login failed";
        }
      } catch (e) {
        this.error = e.message || "Login failed.";
      }
    },
    async register() {
      this.error = "";
      try {
        const res = await registerUser(this.email, this.password, this.pin);
        if (res.ok) {
          this.message = "✅ Registered. Please verify via email and login.";
          this.mode = "login";
        } else {
          this.error = res.error || "Registration failed";
        }
      } catch (e) {
        this.error = e.message || "Error registering.";
      }
    },
    async requestReset() {
      this.error = "";
      try {
        const res = await requestPasswordReset(this.email);
        if (res.ok) {
          this.message = "Check your email for a reset code.";
        } else {
          this.error = res.error || "Email send failed";
        }
      } catch (e) {
        this.error = e.message || "Error requesting reset.";
      }
    },
  },
};
</script>

<style scoped>
.login-container { max-width: 420px; margin: auto; background: #191919; padding: 1.5rem; border-radius: 7px; }
input { display: block; margin: 1rem 0; width: 100%; padding: 0.7rem; border-radius: 4px; border: 1px solid #333; background: #232323; color: #fff; }
button { background: #123; color: #fff; border: none; border-radius: 4px; padding: 0.6rem 1.5rem;}
.actions { margin-bottom: 1rem; }
.error { color: #f44; margin-top: 1rem; }
.info { color: #3fa; margin-top: 1rem; }
a { color: #0bf; cursor: pointer; text-decoration: underline; margin: 0 0.2rem;}
</style>