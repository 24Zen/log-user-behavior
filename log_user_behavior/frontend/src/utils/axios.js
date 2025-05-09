// ตัวอย่างการใช้ axios ใน component
import { ref } from 'vue';
import axiosInstance from '../utils/axios';
import { useAuthStore } from '../store/useAuthStore';

export default {
  name: 'LoginPage',
  setup() {
    const authStore = useAuthStore();
    const email = ref('');
    const password = ref('');
    
    const login = async () => {
      try {
        const response = await axiosInstance.post('/login', {
          email: email.value,
          password: password.value,
        });
        authStore.setUser(response.data.user);
        authStore.setToken(response.data.token);
      } catch (error) {
        console.error(error);
      }
    };

    return { email, password, login };
  },
};
