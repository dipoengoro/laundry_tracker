<script setup>
import { ref } from 'vue';
import apiClient from "../services/ApiClient.js";
import { useRouter } from 'vue-router';
import { apiRoutes } from "../services/apiRoutes.js";

const email = ref('');
const password = ref('');
const error = ref(null);
const router = useRouter();

const handleLogin = async () => {
  error.value = null;
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
  }
};
</script>

<template>
<div class="auth-container">
  <form @submit.prevent="handleLogin">
    <h2>Selamat Datang Kembali</h2>

    <div class="form-group">
      <label for="email">Alamat Email</label>
      <input id="email" type="email" v-model="email" required />
    </div>

    <div class="form-group">
      <label for="password">Password</label>
      <input id="password" type="password" v-model="password" required />
    </div>
    <button type="submit">Masuk</button>
    <p v-if="error">{{ error }}</p>
  </form>
</div>
</template>

<style scoped>
  .auth-container {}
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
</style>