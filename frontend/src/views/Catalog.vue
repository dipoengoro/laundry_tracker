<script setup>
import {ref, onMounted} from 'vue';
import apiClient from "../services/ApiClient.js";

const clothingItems = ref([]);

const fetchItems = async () => {
  try {
    const response = await apiClient.get('/catalog/items/');
    clothingItems.value = response.data;
  } catch (error) {
    console.error('Gagal mengambil data pakaian: ', error);
  }
};

const deleteItem = async (itemId) => {
  if (confirm('Apakah Anda yakin ingin menghapus item ini?')) {
    try {
      await apiClient.delete(`/catalog/items/${itemId}`);
      // Hapus item dari list frontend tanpa perlu reload halaman
      clothingItems.value = clothingItems.value.filter(item => item.id !== itemId);
    } catch (error) {
      console.error('Gagal menghapus item: ', error);
    }
  }
};

// Panggil fetchItems saat komponen pertama kali di-mount
onMounted(fetchItems);
</script>

<template>
  <div class="catalog-page">
    <header>
      <h1>Katalog Pakaian Saya</h1>
      <button @click="openAddItemModal">Tambah Pakaian Baru</button>
    </header>

    <div class="item-grid">
      <div v-for="item in clothingItems" :key="item.id" class="item-card">
        <img :src="item.image || 'https://via.placeholder.com/150'" alt="Gambar Pakaian">
        <h3>{{item.name}}</h3>
        <p>{{item.category}} - {{item.color}}</p>
        <div class="actions">
          <button class="edit">Ubah</button>
          <button class="delete" @click="deleteItem(item.id)">Hapus</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.catalog-page {
  padding: 2rem;
}
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}
.item-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1.5rem;
}
.item-card {
  background: white;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  overflow: hidden;
}
.item-card img {
  width: 100%;
  height: 180px;
  object-fit: cover;
}
.item-card h3, .item-card p {
  margin: 0;
  padding: 0.5rem 1rem;
}
.item-card p {
  font-size: 0.9em;
  color: #666666;
  padding-top: 0;
}
.actions {
  display: flex;
  padding: 0.5rem;
}
.actions button {
  flex: 1;
  margin: 0.2rem;
}
</style>