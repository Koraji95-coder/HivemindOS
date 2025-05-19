import { createApp } from 'vue';
import App from './App.vue';
import Toast from 'vue-toastification';
import 'vue-toastification/dist/index.css'; // 🎨 Toast styles

const app = createApp(App);

// 🍞 Global toast configuration
const options = {
  position: "top-right",
  timeout: 4000,
  closeOnClick: true,
  pauseOnHover: true,
  draggable: true,
  showCloseButtonOnHover: false,
  hideProgressBar: false,
  theme: "dark", // or "light"
};

app.use(Toast, options);
app.mount('#app');