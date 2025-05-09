<template>
  <div>
    <h1>Welcome to the Home Page</h1>
    <Login />  <!-- ใช้คอมโพเนนต์ Login.vue ที่นำเข้า -->
  </div>
</template>

<script>
import Login from '../components/Login.vue';  <!-- แก้ไขเส้นทางเป็น ../components/Login.vue -->

export default {
  name: 'Home',
  components: {
    Login  // ลงทะเบียนคอมโพเนนต์ Login
  }
}
</script>

<style scoped>
/* สไตล์ของหน้า Home.vue */
h1 {
  color: #4CAF50;
}
</style>
