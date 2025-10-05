<template>
  <div class="auth-container">
    <form @submit.prevent="handleRegister">
      <h2>Buat Akun Baru</h2>

      <div class="form-group">
        <label for="username">Username</label>
        <input id="username" type="text" v-model="username" required />
      </div>

      <div class="form-group">
        <label for="email">Alamat Email</label>
        <input id="email" type="email" v-model="email" required />
      </div>

      <div class="form-group">
        <label for="password">Password</label>
        <input id="password" type="password" v-model="password" required />
      </div>

      <div class="form-group">
        <label for="password2">Konfirmasi Password</label>
        <input id="password2" type="password" v-model="password2" required />
      </div>

      <button type="submit">Daftar</button>
      <p v-if="error">{{ error }}</p>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import apiClient from "../services/ApiClient.js";
import {useRouter} from "vue-router";
import {apiRoutes} from "../services/apiRoutes.js";

const username = ref('');
const email = ref('');
const password = ref('');
const password2 = ref('');
const error = ref(null);
const router = useRouter()

const handleRegister = async () => {
  error.value = null;
  if (password.value !== password2.value) {
    error.value = "Password tidak cocok!";
    return;
  }
  try {
    const response = await apiClient.post(apiRoutes.REGISTER, {
      username: username.value,
      email: email.value,
      password: password.value,
      password2: password2.value,
    });
    console.log('Registrasi berhasil: ', response.data);
    router.push('/login');
  } catch (error) {
    error.value = 'Registrasi gagal. Coba lagi.';
    console.error(error.response.data);
  }
};
</script>

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