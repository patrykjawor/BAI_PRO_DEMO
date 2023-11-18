<template>
    <div>
    <VueSidebarMenuAkahon 
        :isUsedVueRouter=true
        :isMenuOpen=true
        :isSearch=false
        iconsColor="#42b883"
        menuIcon="bi bi-list-check"
        menuTitle='Pages list'
        profileName="Patryk Jaworski"
        :menuItems="[{'link':'/dashboard/sqldemo', 'name':'Sql Injection', 'icon':'bi bi-database-fill-exclamation'},
                     {'link':'/dashboard/xssdemo', 'name':'XSS', 'icon':'bi bi-code-square'},
                     {'link':'/dashboard/csrfdemo', 'name':'CSRF', 'icon':'bi bi-shield-fill-exclamation'},
                     {'link':'/dashboard', 'name':'Index', 'icon':'bi bi-house-fill'}]"
        @button-exit-clicked="handleLogout"/>
    </div>
</template>

<script>
    import VueSidebarMenuAkahon from "vue-sidebar-menu-akahon";
    import api from "../getAxios";
export default{
    name: "SideMenu",
    components: {VueSidebarMenuAkahon},
    methods:{
        handleLogout() {
                const formDataLogout = new FormData();
                formDataLogout.append('csrfmiddlewaretoken', this.$cookies.get('csrftoken'))
                api.post('main/logout/', formDataLogout, {
                headers:{
                    'Content-Type': 'multipart/form-data',
                    'X-CSRFToken': this.$cookies.get('csrftoken')
                }
                }).then(response => {
                    console.log('Logged out successfully.', response.data);
                    this.$router.push("/login");
                })
                .catch(error => {
                console.error('Error logging out:', error);
                });
        },
    },
    mounted() {
        // Usuwa elementy tooltip psujące układ strony
        const elements = document.querySelectorAll('span.tooltip');
          for(var i = 0; i < elements.length; ++i)
            elements[i].remove();
    }
}
</script>