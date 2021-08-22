<template>
	<Base>
		<template v-slot:nav>
			<div class="">
				<Nav />
			</div>
		</template>

		<template v-slot:body>
			<div class="breadcrumb">
				<p>Product / </p>
				<p>Manage</p>
			</div>

			<div class="divider"></div>
			        
            <div class="grid grid-cols-1 md:grid-cols-3">
                <Product
                    v-for="(product, index) in _products"
                    :key="index"
                    :product="product"
                    :can_edit="true"
                />
            </div>

            <Modal
            	name="product_modal"
            	header='Product | Add'
        	>
            	<template v-slot:body>
            		<form @submit.prevent="save_product">
            			<div>
            				<label>Name</label>
	            			<input type="text" v-model="name" />
            			</div>

            			<div>
            				<label>Image</label>
            				<input type="file" @change="image_upload($event)" />
            			</div>

            			<div>
            				<label>Description</label>
	            			<textarea v-model="description"></textarea>
            			</div>

            			<div>
            				<label>Price</label>
	            			<input type="number" v-model="price" />
            			</div>

            			<button class="mx-0 p-4-blue-700" type="submit">Submit</button>
            		</form>
            	</template>
            </Modal>

            <button
            	class="floating-button bg-gray-300"
            	@click="open_modal('product_modal')"
        	>
            	<i class="fas fa-plus"></i>
            </button>
		</template>
	</Base>
</template>

<script type="text/javascript">
	import { mapGetters, mapActions } from 'vuex'
	import { GET_PRODUCTS, CREATE_PRODUCT } from '/@/store/types.js'
	import { open_modal, close_modal } from '/@/components/modal/modal.js'

	export default {
		name: 'Products',
		title () {
		    return 'WasBam | Products | Manage'
		},
		mounted () {
		    this.get_products()
		},
		data () {
			return {
				name: '',
				image: '',
				description: '',
				price: ''
			}
		},
		computed: {
		    ...mapGetters({
		        _products: 'get_products'
		    })
		},
		methods: {
		    ...mapActions({
		        get_products: GET_PRODUCTS,
		        create_product: CREATE_PRODUCT
		    }),
		    open_modal,
		    close_modal,
		    image_upload (event) {
		    	this.image = event.target.files[0]
		    },
		    reset_product_form () {
		    	this.name = '',
				this.image = ''
				this.description = ''
				this.price = ''
		    },
		    save_product () {
		    	const payload = new FormData()

		    	payload.append('name', this.name)
		    	payload.append('image', this.image)
		    	payload.append('description', this.description)
		    	payload.append('price', this.price)

		    	this.create_product(payload)
		    	this.get_products()

		    	this.reset_product_form()

		    	close_modal('product_modal')
		    }
		}
	}
</script>
