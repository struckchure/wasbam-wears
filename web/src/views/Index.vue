<template>
    <Base>
        <template v-slot:body>
            <div class="divider"></div>
        
            <div class="grid grid-cols-1 md:grid-cols-3">
                <Product
                    v-for="(product, index) in products"
                    :key="index"
                    :product="product"
                />
            </div>
        </template>
    </Base>
</template>

<script type="text/javascript">
    import { mapGetters, mapActions } from 'vuex'
    import { GET_PRODUCTS } from '/@/store/types.js'

    export default {
        name: 'Index',
        title () {
            return 'WasBam | Welcome'
        },
        mounted () {
            this.get_products()
        },
        computed: {
            ...mapGetters({
                products: 'get_products'
            })
        },
        methods: {
            ...mapActions({
                get_products: GET_PRODUCTS
            })
        }
    }
</script>
