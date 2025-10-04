<template>
  <div id="app-wrapper">
    <router-view />
  </div>
</template>

<style>
body {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

#app-wrapper {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>