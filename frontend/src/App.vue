<script setup>
import Footer from './components/Footer.vue';
import api from './getAxios';
import SideMenu from './components/SideMenu.vue';


</script>
<template>
    <SideMenu v-if="showSidebar()"></SideMenu>
    <router-view></router-view>
    <Footer></Footer>
</template>

<script>

export default {
  name: "App",
  //TODO: Sprawdzić czy faktycznie działą
  data () {
    return {
    }
  },

  setup() {
  },
  methods:{
    showSidebar() {
      const show = ((this.$route.path !== '/login') && (this.$route.path !== '/register'))
        if(!show){
          document.body.style.paddingLeft = '0px';
          
        }
        return show;
      }
  },
  mounted() {
    api.get('main/islogin/')
      .then(response => {
        return response.data
      })
      .then(data => {
        if (!data.authenticated && this.$route.path !== '/login')
          this.$router.push('/login')
      })
      .catch(error => {
        console.error(error)
      })
  },
  computed: {
      
  }
}
</script>
