<script setup>
import { ref } from 'vue';
import apiClient from "../services/ApiClient.js";
import { useRouter } from 'vue-router';
import { apiRoutes } from "../services/apiRoutes.js";
import AuthLayout from "../layouts/AuthLayout.vue";

const email = ref('');
const password = ref('');
const error = ref(null);
const router = useRouter();
const isLoading = ref(false);

const handleLogin = async () => {
  error.value = null;
  isLoading.value = true;
  try {
    const response = await apiClient.post(apiRoutes.LOGIN, {
      email: email.value,
      password: password.value,
    });
    const newToken = response.data.access;
    console.log('TOKEN BARU DITERIMA: ', newToken);

    // Simpan token untuk penggunaan di masa depan (saat refresh halaman)
    localStorage.setItem('authToken', newToken);

    // Langsung terapkan token baru ke apiClient yang sedang aktif
    apiClient.defaults.headers.common['Authorization'] = `Bearer ${newToken}`;
    router.push('/')
  } catch (error) {
    error.value = 'Email atau password salah.';
    console.error('Login gagal: ', error);
  } finally {
    isLoading.value = false;
  }
};
</script>

<template>
  <AuthLayout>
    <form @submit.prevent="handleLogin">
      <h2>Selamat Datang Kembali</h2>

      <div class="form-group">
        <label for="email">Alamat Email</label>
        <input type="email" id="email" v-model="email" required />
      </div>

      <div class="form-group">
        <label for="password">Password</label>
        <input type="password" id="password" v-model="password" required />
      </div>

      <button type="submit" :disabled="isLoading">
        {{ isLoading ? 'Memproses...' : 'Masuk' }}
      </button>
      <p v-if="error" class="error-message">{{ error }}</p>

      <p class="navigation-link">
        Belum punya akun? <router-link to="/register">Daftar di sini</router-link>
      </p>
    </form>
  </AuthLayout>
</template>

<style scoped>
  h2 {
    text-align: center;
    color: var(--text-color);
    margin-bottom: 30px;
    font-weight: 700;
  }

  form {
    background-color: var(--form-background);
    padding: 40px;
    border-radius: 12px;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0, 0.1);
    width: 100%;
    max-width: 400px;
  }

  form h2 {
    text-align: center;
    color: var(--text-color);
    margin-bottom: 30px;
    font-weight: 700px;
  }

  form input {
    width: 100%;
    padding: 12px 15px;
    border: 1px solid var(--input-border-color);
    border-radius: 8px;
    font-size: 16px;
    transition: border-color 0.3s;
    box-sizing: border-box;
  }

  form input:focus {
    outline: none;
    border-color: var(--primary-color);
  }

  form button {
    width: 100%;
    padding: 15px;
    background-color: var(--primary-color);
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 16px;
    font-weight: 500;
    cursor: pointer;
    transition: background-color 0.3s;
  }

  form button:hover {
    background-color: var(--primary-hover);
  }

  form p {
    color: var(--error-color);
    text-align: center;
    margin-top: 15px;
    font-size: 14px;
  }

  .form-group {
    margin-bottom: 20px;
    text-align: left;
  }

  .form-group label {
    display: block;
    margin-bottom: 8px;
    font-size: 14px;
    font-weight: 500;
    color: #555;
  }

  button:disabled {
    background-color: #A288E3;
    opacity: 0.7;
    cursor: not-allowed;
  }

  .error-message {
    color: var(--error-color);
    margin-top: 15px;
    font-size: 14px;
  }

  .navigation-link {
    margin-top: 25px;
    font-size: 14px;
  }

  .navigation-link a {
    color: var(--primary-color);
    font-weight: 500;
    text-decoration: none;
  }

  .navigation-link a:hover {
    text-decoration: underline;
  }
</style>