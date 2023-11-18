<template>
<div class="min-vh-100">
    <h1 class="text-center mt-3 mb-2 pb-2 border-bottom border-2">SQL Injection demo</h1>
    <input v-model="names" class="shadow rounded position-relative start-50 translate-middle-x mt-3 mb-3 p-1" placeholder="Search for product name"/>
    <input v-model="safe" class="position-relative" id="checkbox" type="checkbox"/>
    <label for="checkbox">&nbsp;Safe search</label>
    <br/>
    <label class="position-relative start-50 translate-middle-x mt-2 mb-3">Current SQL string: <i>{{ sql }}</i></label>
    <div>
        <Product v-for="product in products" :name="product.name" :price="product.price" :thumbnail="product.thumbnail"/>
    </div>

</div>


</template>

<script>
import Product from "../components/Product.vue";
import api from '../getAxios.js';
export default {
        name: "Dashboard",
        components: { Product},
        data() {
            return {
                products: [],
                names: '',
                safe: false,
                sql: ''
            }
        },

        methods: {
            
        getProducts() {
            api.get('main/sqldemo/', {
                params: {
                    name: this.names,
                    safe: this.safe
                }
            })
            .then(response => {
                return response.data
            })
            .then(data => {
                this.products = data.products
                this.sql = data.query
            })
            .catch(error => {
                console.warn(error)
            })
        }

  },
  mounted() {
    this.getProducts()
  },
  watch: {
    names(val) {
        this.getProducts()
    },
    safe(val){
        this.getProducts()
    }

  }
}
</script>