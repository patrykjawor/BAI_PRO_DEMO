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
  <div class="d-flex flex-column justify-content-center align-items-center text-center min-vh-100 registerForm">
      <div v-if= "qrCodeImage" class="pt-2">
            <h3> Register Sucessfull!<br/>Scan this code with your Authenticator App.<br/> Be carefull it only shows once per register!</h3> <br>
          <img :src="qrCodeImage" alt="QR Code for 2FA" />
      </div>
      <form @submit.prevent="submitForm" class="container-mt5">
          <h1>User Register</h1>
          <div class="form-group">
              <label for="username">Username:</label>
              <input type="text" v-model="user.username" id="username" class="form-control"/>
          </div>
          <div>
              <label for="email">Email:</label>
              <input type="email" v-model="user.email" id="email" class="form-control" placeholder="Please provide a REAL email"/>
          </div>
          <div>
              <label for="password1">Password:</label>
              <input type="password" v-model="user.password1" id="password1" class="form-control"/>
          </div>
          <div>
              <label for="password2">Confirm Password:</label>
              <input type="password" v-model="user.password2" id="password2" class="form-control"/>
          </div>
          <div>
              <label for="enable_2fa">Enable Two-Factor Authentication:</label>
              <input type="checkbox" v-model="user.enable_2fa" id="enable_2fa" class="form-check-input" />
          </div>
          <div class="mt-3">
              <button type="submit" class="btn btn-outline-secondary btn-lg">
                  Register
              </button>
          </div>
      </form>

  </div>
</template>
  
  <script>
  import api from '../getAxios.js';
  
  export default {
    name: "Register",
    
    data() {
      return {
        user: {
          username: '',
          email: '',
          password1: '',
          password2: '',
          enable_2fa: false, // Initialize 2FA checkbox to false
        },
        qrCodeImage: null, // Initialize QR code image to null
      };
    },
    methods: {
  
      submitForm() {
          this.register();
      },
  
      register() {
          const formDataRegister = new FormData();
          formDataRegister.append('username', this.user.username);
          formDataRegister.append('email', this.user.email);
          formDataRegister.append('password1', this.user.password1);
          formDataRegister.append('password2', this.user.password2);
          formDataRegister.append('enable_2fa', this.user.enable_2fa);
          formDataRegister.append('csrfmiddlewaretoken', this.$cookies.get('csrftoken'))
  
          api.post('main/register/', formDataRegister, {
              headers:{
                  'Content-Type': 'multipart/form-data',
                  'X-CSRFToken': this.$cookies.get('csrftoken')
              }
          })
          .then(response => {
              console.log('User registered successfully:', response.data);
              if (response.data.image_data) {
              // Set the image of QR code
                  this.qrCodeImage = response.data.image_data;
              }
              // Clear form fields
              this.user.username = '';
              this.user.email = '';
              this.user.password1 = '';
              this.user.password2 = '';
              this.user.enable_2fa = false;
          })
          .catch(error => {
              if (error.response) {
                  console.error('Error registering user:', error.response.data);
              } else if (error.request) {
                  console.error('No response received:', error.request);
              } else {
                  console.error('Error setting up the request:', error.message);
              }
          });
      },
    },
  };
  </script>