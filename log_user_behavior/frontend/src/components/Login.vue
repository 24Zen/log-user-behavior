<template>
    <div class="login-container">
      <h2>Login</h2>
      <form @submit.prevent="handleLogin">
        <input v-model="username" type="text" placeholder="Username" />
        <input v-model="password" type="password" placeholder="Password" />
        <button type="submit">Login</button>
      </form>
      <p v-if="error" style="color: red;">{{ error }}</p>
      <p v-if="token">Token: {{ token }}</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        username: '',
        password: '',
        error: '',
        token: ''
      };
    },
    methods: {
      async handleLogin() {
        try {
          const response = await axios.post('http://localhost:5000/login', {
            username: this.username,
            password: this.password
          });
          this.token = response.data.access_token;
          this.error = '';
          console.log("Login success:", this.token);
        } catch (err) {
          this.error = 'Login failed';
          this.token = '';
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .login-container {
    max-width: 300px;
    margin: auto;
    padding: 1rem;
    border: 1px solid #ccc;
    border-radius: 10px;
  }
  input {
    display: block;
    margin: 0.5rem 0;
    width: 100%;
  }
  button {
    width: 100%;
    padding: 0.5rem;
  }
  </style>
  