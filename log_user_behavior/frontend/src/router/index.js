import { createRouter, createWebHistory } from 'vue-router';
import Login from '../views/Login.vue';

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  }
  // เพิ่มหน้าอื่นตรงนี้ได้ เช่น Dashboard
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
