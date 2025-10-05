<script setup>

</script>

<template>
  <div class="auth-layout">
    <div class="form-card">
      <h1 class="app-title">Laundry Tracker</h1>
      <slot></slot>
    </div>
  </div>
</template>

<style scoped>
.auth-layout {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: var(--background-color);
  font-family: var(--main-font);
}

.form-card {
  background-color: var(--form-background);
  padding: 40px;
  border-radius: 12px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 400px;
  text-align: center;
}

.app-title {
  font-weight: 700;
  font-size: 28px;
  color: var(--primary-color);
  margin-bottom: 30px;
}
</style>