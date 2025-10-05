<script setup>
import {ref, onMounted} from 'vue';
import apiClient from "../services/ApiClient.js";
import {apiRoutes} from "../services/apiRoutes.js";

const clothingItems = ref([]);

const isModalVisible = ref(false);
const isEditMode = ref(false);
const currentItem = ref({
  id: null,
  name: '',
  category: 'TOP',
  color: '',
  image: null,
});
const imagePreview = ref(null);

const closeModal = () => {
  isModalVisible.value = false;
};

const openAddItemModal = () => {
  isEditMode.value = false;
  // Reset form ke kondisi awal
  currentItem.value = {
    id: null,
    name: '',
    category: 'TOP',
    color: '',
    image: null,
  };
  imagePreview.value = null;
  isModalVisible.value = true;
};

const openEditItemModal = (item) => {
  isEditMode.value = true;
  // Isi form dengan data item yang akan diubah
  currentItem.value = {
    ...item,
    image: null,
  };
  imagePreview.value = item.image;
  isModalVisible.value = true;
};

const handleImageUpload = (event) => {
  const file = event.target.files[0];
  if (file) {
    currentItem.value.image = file;
    // Buat preview gambar secara lokal
    imagePreview.value = URL.createObjectURL(file);
  }
};

const handleSubmit = async () => {
  // Buat objek FormData untuk mengirim data + file
  const formData = new FormData();
  formData.append('name', currentItem.value.name);
  formData.append('category', currentItem.value.category);
  formData.append('color', currentItem.value.color);
  // Hanya tambahkan gambar jika ada file baru yang dipilih
  if (currentItem.value.image instanceof File) {
    formData.append('image', currentItem.value.image);
  }

  try {
    if (isEditMode.value) {
      // Logika untuk UPDATE (menggunakan PATCH)
      await apiClient.patch(apiRoutes.CLOTHING_ITEM_DETAIL(currentItem.value.id), formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
    } else {
      // Logika untuk CREATE (menggunakan POST)
      await apiClient.post(apiRoutes.CLOTHING_ITEMS, formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
    }
    closeModal();
    fetchItems(); // Muat ulang daftar item setelah berhasil
  } catch (error) {
    console.error('Gagal menyimpan data pakaian: ', error.response.data);
  }
};

const fetchItems = async () => {
  try {
    const response = await apiClient.get(apiRoutes.CLOTHING_ITEMS);
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
    <div class="modal-backdrop" v-if="isModalVisible">
      <div class="modal">
        <h2>{{ isEditMode ? 'Ubah Pakaian' : 'Tambah Pakaian Baru' }}</h2>
        <form @submit.prevent="handleSubmit">
          <div class="form-group">
            <label for="name">Nama Pakaian</label>
            <input type="text" id="name" v-model="currentItem.name" required>
          </div>
          <div class="form-group">
            <label for="category">Kategori</label>
            <select id="category" v-model="currentItem.category">
              <option value="TOP">Atasan</option>
              <option value="BOTTOM">Bawahan</option>
              <option value="OUTWEAR">Luaran</option>
              <option value="OTHER">Lainnya</option>
            </select>
          </div>
          <div class="form-group">
            <label for="color">Warna</label>
            <input type="text" id="color" v-model="currentItem.color">
          </div>
          <div class="form-group">
            <label for="image">Gambar</label>
            <input type="file" id="image" @change="handleImageUpload">
            <img v-if="imagePreview" :src="imagePreview" alt="Preview" class="image-preview">
          </div>
          <div class="modal-actions">
            <button type="button" @click="closeModal">Batal</button>
            <button type="submit">Simpan</button>
          </div>
        </form>
      </div>
    </div>
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
          <button class="edit" @click="openEditItemModal(item)">Ubah</button>
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
.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}
.modal {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  width: 90%;
  max-width: 500px;
}
.modal h2 {
  margin-top: 0;
}
.form-group {
  margin-bottom: 1rem;
}
.form-group label {
  display: block;
  margin-bottom: 0.5rem;
}
.form-group input, .form-group select {
  width: 100%;
  padding: 0.5rem;
  border-radius: 4px;
  border: 1px solid #CCCCCC;
}
.image-preview {
  max-width: 100px;
  margin-top: 1rem;
  border-radius: 4px;
}
.modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
  margin-top: 2rem;
}
</style>