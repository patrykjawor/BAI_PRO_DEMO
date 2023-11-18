<template>
  <div>
    <ul class="nav nav-pills nav-fill nav-css">
      <li class="nav-item">
        <router-link to="/register" class="nav-link" active-class="active"><i></i>Register</router-link>
      </li>
      <li class="nav-item">
        <router-link to="/login" class="nav-link" active-class="active"><i></i>Login</router-link>
      </li>
    </ul>
  </div>

  <div class="d-flex justify-content-center min-vh-100 align-items-center text-center registerForm">
    <form @submit.prevent="submitForm" class="container-mt5">
      <h1>User Login</h1>
      <div class="form-group">
        <label for="username">Username:</label>
        <input type="text" v-model="user.username" id="username" class="form-control" />
      </div>
      <div>
        <label for="password1">Password:</label>
        <input type="password" v-model="user.password" id="password1" class="form-control" />
      </div>
      <div v-if="requires2FA">
         <br>
        <label for="totp_code"><strong>2FA code from Authenticator App:</strong></label>
        <input type="text" v-model="user.totp_code" id="totp_code" class="form-control" />
      </div>
      <div class="mt-3">
        <button type="submit" class="btn btn-outline-secondary btn-lg">Login</button>
      </div>
    </form>
  </div>
</template>

<script>
import api from '../getAxios.js';

export default {
  name: "Login",
  data() {
    return {
      user: {
        username: '',
        password: '',
        totp_code: '', // 2FA code
      },
      requires2FA: false, // Show 2FA code input
    };
  },
  methods: {
    submitForm() {
      this.login();
    },

    login() {
      const formDataLogin = new FormData();
      formDataLogin.append('username', this.user.username);
      formDataLogin.append('password', this.user.password);
      if (this.requires2FA) {
        formDataLogin.append('totp_code', this.user.totp_code); // Include 2FA code
      }
      formDataLogin.append('csrfmiddlewaretoken', this.$cookies.get('csrftoken'));

      api.post('main/login/', formDataLogin, {
        headers: {
          'Content-Type': 'multipart/form-data',
          'X-CSRFToken': this.$cookies.get('csrftoken'),
        },
      })
        .then(response => {
          if (response.data.requires_2fa) {
            // 2FA is required, show the 2FA code input field.
            this.requires2FA = true;
          } else {
            console.log('User logged in successfully:', response.data);
            this.$router.push("/dashboard");
            this.user.username = '';
            this.user.password = '';
          }
        })
        .catch(error => {
          console.error('Error logging in:', error.response.data);
        });
    },
  },
};
</script>