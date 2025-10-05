<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import apiClient from "../services/ApiClient.js";
import { apiRoutes } from "../services/apiRoutes.js";

const router = useRouter();
const isSidebarOpen = ref(true);
const user = ref(null);

const toggleSidebar = () => {
  isSidebarOpen.value = !isSidebarOpen.value;
};

const fetchUser = async () => {
  try {
    const response = await apiClient.get(apiRoutes.USER_DETAIL);
    user.value = response.data;
  } catch (error) {
    console.error("Gagal mengambil data pengguna: ", error);
  }
};

onMounted(fetchUser);

const handleLogout = () => {
  localStorage.removeItem('authToken');

  delete apiClient.defaults.headers.common['Authorization'];

  router.push('/login');
};
</script>

<template>
  <div class="main-layout" :class="{ 'sidebar-closed': !isSidebarOpen }">
    <aside class="sidebar">
      <h1 class="logo">Laundry Tracker</h1>
      <nav class="navigation">
        <router-link to="/">Katalog Pakaian</router-link>
      </nav>
    </aside>

    <div class="content-wrapper">
      <header class="top-bar">
        <button class="hamburger-button" @click="toggleSidebar">
          <span></span>
          <span></span>
          <span></span>
        </button>
        <div class="top-bar-right">
          <div class="user-info">
            Selamat Datang, **{{ user?.username || 'Pengguna' }}**!
          </div>
          <button @click="handleLogout" class="logout-button">Logout</button>
        </div>
      </header>

      <main class="page-content">
        <router-view />
      </main>
    </div>
  </div>
</template>

<style scoped>
:root {
  --sidebar-width: 250px;
  --sidebar-transition-speed: 0.3s;
  --hamburger-size: 44px;
  --hamburger-thick: 2px;
  --hamburger-gap: 6px;
  --duration: 0.25s;
}
.main-layout {
  display: flex;
  min-height: 100vh;
}

.sidebar {
  width: var(--sidebar-width);
  flex-shrink: 0;
  background-color: white;
  padding: 2rem;
  box-shadow: 2px 0 5px rgba(0, 0, 0, 0.05);
  display: flex;
  flex-direction: column;
  transition: margin-left var(--sidebar-transition-speed) ease;
  white-space: nowrap;
}

.main-layout.sidebar-closed .sidebar {
  margin-left: calc(-1 * var(--sidebar-width));
}

.logo {
  font-size: 24px;
  font-weight: 700;
  color: var(--primary-color);
  text-align: center;
  margin-bottom: 2rem;
}

.navigation {
  margin-top: 1rem;
}

.navigation a {
  display: block;
  padding: 10px 15px;
  margin-bottom: 10px;
  border-radius: 6px;
  text-decoration: none;
  color: #333333;
  font-weight: 500;
  transition: background-color 0.2s, color 0.2s;
}

.navigation a:hover,
.navigation a.router-link-exact-active {
  background-color: var(--primary-color);
  color: white;
}

.content-wrapper {
  flex-grow: 1;
  background-color: var(--background-color);
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.top-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background-color: white;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  flex-shrink: 0;
}

.top-bar-right {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.user-info {
  font-weight: 500;
  color: #333333;
}

.logout-button {
  background-color: var(--primary-color);
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.logout-button:hover {
  background-color: var(--primary-color);
}

.hamburger-button {
  inline-size: var(--hamburger-size);
  block-size: var(--hamburger-size);
  display: inline-grid;
  place-items: center;
  gap: var(--hamburger-gap);
  background: transparent;
  border: 0;
  padding: 0;
  cursor: pointer;
  border-radius: 10px;
}

.hamburger-button:focus-visible {
  outline: 2px solid Highlight;
  outline-offset: 3px;
}

.hamburger-button span {
  inline-size: var(--hamburger-thick);
  background: currentColor;
  border-radius: 999px;
  transition: transform var(--duration) ease, opacity var(--duration) ease, translate var(--duration) ease;
}

.hamburger-button {
  position: relative;
}
.hamburger-button span {
  position: absolute;
  left: 50%;
  translate: -50% 0;
}
.hamburger-button span:nth-child(1) {
  top: calc(50% - (var(--hamburger-gap) + var(--hamburger-thick)));
}
.hamburger-button span:nth-child(2) {
  top: 50%;
}
.hamburger-button span:nth-child(3) {
  top: calc(50% + (var(--hamburger-gap) + var(--hamburger-thick)));
}

.hamburger-button.is-open span:nth-child(1) {
  transform: translateY(calc(var(--hamburger-gap) + var(--hamburger-thick))) rotate(45deg);
}
.hamburger-button.is-open span:nth-child(2) {
  opacity: 0;
}
.hamburger-button.is-open span:nth-child(3) {
  transform: translateY(calc(-1 * (var(--hamburger-gap) + var(--hamburger-thick)))) rotate(-45deg);
}

@media (prefers-reduced-motion: reduce) {
  .hamburger-button span { transition: none; }
}

.page-content {
  padding: 2rem;
  flex-grow: 1;
  overflow-y: auto;
}
</style>