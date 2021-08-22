<template>
	<div class="product">
		<div class="product-image">
			<img :src="get_product.image">
		</div>
		<div class="product-description">
			<label>{{ get_product.name }}</label>
			<small>{{ get_product.description }}</small>
		</div>
		<div class="product-price">
			<small>&#8358; {{ get_product.price }}</small>
		</div>
		<div class="product-actions">
			<Toast :name="`cart_item_${this.get_product.slug}`">
				<template v-slot:body>
					<p>{{ get_cart_item_message }}</p>
				</template>
			</Toast>

			<Modal
				:name="`confirm_delete_product_${get_product.slug}`"
				header="Requesting Confirmation"
			>
				<template v-slot:body>
					<p>
						Are you sure you want to delete {{ get_product.name }}
					</p>
					<div>
						<button @click="delete_product">Yes</button>
						<button @click="close_modal(`confirm_delete_product_${get_product.slug}`)">No</button>
					</div>
				</template>
			</Modal>

            <Modal
            	:name="get_product.slug"
            	:header="`Product | Update | ${get_product.name}`"
        	>
            	<template v-slot:body>
            		<form @submit.prevent="save_product">
            			<div>
            				<label>Name</label>
	            			<input
	            				type="text"
	            				v-model="get_product.name"
	            				@input="event => this.name = event.target.value"
            				/>
            			</div>

            			<div>
            				<label>Image</label>
            				<input
            					type="file"
            					@change="handle_image($event)"
        					/>
            			</div>

            			<div>
            				<label>Description</label>
	            			<textarea
	            				v-model="get_product.description"
	            				@input="event => this.description = event.target.value"
            				></textarea>
            			</div>

            			<div>
            				<label>Price</label>
	            			<input
	            				type="number"
	            				v-model="get_product.price"
	            				@input="event => this.price = event.target.value"
            				/>
            			</div>

            			<button class="mx-0 p-4-blue-700" type="submit">Submit</button>
            		</form>
            	</template>
            </Modal>

            <button @click="buy_now">
            	Buy now
            </button>

            <button
            	@click="add_cart_item"
            	v-bind:class="{
            		'bg-red-500': _get_carted,
            		'text-white': _get_carted,
            		'border-none': _get_carted
            	}"
            >
            	<i class="fas fa-cart-plus"></i>
            </button>

			<div v-if="get_can_edit == true">
				<button @click="update_product">
					<i class="fas fa-edit"></i>
				</button>

				<button @click="confirm_delete_product">
					<i class="fas fa-trash"></i>
				</button>
			</div>
		</div>
	</div>
</template>

<script type="text/javascript">
	import { mapGetters, mapActions } from 'vuex'
	import {
		GET_PRODUCTS,
		DELETE_PRODUCT,
		UPDATE_PRODUCT,
		GET_CART,
		ADD_CART_ITEM,
		DELETE_CART_ITEM,
		FILTER_CART_ITEM_BY_PRODUCT
	} from '/@/store/types.js'
	import { open_modal, close_modal } from '/@/components/modal/modal.js'
	import { open_toast } from '/@/components/toast/toast.js'
	import { redirectNotAuthenticated } from '/@/store/decorators.js'

	export default {
		name: 'Product',
		props: {
			product: Object,
			can_edit: Boolean
		},
		data () {
			return {
				name: '',
				image: '',
				description: '',
				price: '',

				// cart
				_cart_item: {},
				_carted: '',
				cart_item_message: '',
				quantity: 1
			}
		},
		mounted () {
			this._set_cart_item()
		},
		computed: {
			...mapGetters({
				_cart_item_exists: 'get_cart_item_exists'
			}),
			_get_cart_item () {
				return this._cart_item
			},
			_added () {
				if (this._get_carted) {
					return 'removed from'
				} else {
					return 'added to'
				}
			},
			_get_carted () {
				return this._carted
			},
			get_product () {
				return this.product
			},
			get_can_edit () {
				return this.can_edit
			},
			get_cart_item_message () {
				return this.cart_item_message
			}
		},
		methods: {
			...mapActions({
				// products
				_get_products: GET_PRODUCTS,
				_delete_product: DELETE_PRODUCT,
				_update_product: UPDATE_PRODUCT,

				// cart
				_get_cart: GET_CART,
				_add_cart_item: ADD_CART_ITEM,
				_delete_cart_item: DELETE_CART_ITEM,
				_filter_cart_item_by_product: FILTER_CART_ITEM_BY_PRODUCT
			}),
			close_modal,
			_set_cart_item () {
				if (!redirectNotAuthenticated(false)) {
					this._filter_cart_item_by_product(this.get_product.slug)
						.then((response) => {
							this._cart_item = response
							if (this._cart_item) {
								if (this._cart_item.product) {
									this._carted = true;
								} else {
									this._carted = false;
								}
							} else {
								return false
							}
						})
				}
			},
			add_cart_item () {
				if (!redirectNotAuthenticated(false)) {
					const payload = {
						product: this.get_product.slug,
						quantity: this.quantity
					}

					// add cart item

					this._add_cart_item(payload)
					this.cart_item_message = `${this.get_product.name} has been ${this._added} cart`
					open_toast(`cart_item_${this.get_product.slug}`)
				} else {
					this.$router.push({name: 'Login'})
				}

			},
			buy_now () {
				redirectNotAuthenticated()
			},
			confirm_delete_product () {
				redirectNotAuthenticated()

				open_modal(`confirm_delete_product_${this.get_product.slug}`)
			},
			delete_product () {
				redirectNotAuthenticated()

				this._delete_product(this.get_product.slug)
				close_modal(`confirm_delete_product_${get_product.slug}`)
			},
			update_product () {
				redirectNotAuthenticated()

				open_modal(this.get_product.slug)
			},
			handle_image (event) {
				this.image = event.target.files[0]
			},
			save_product () {
				redirectNotAuthenticated()

				const payload = new FormData()
				const data = {
					name: this.name,
					image: this.image,
					description: this.description,
					price: this.price
				}

				Object.keys(data).forEach(
					(key) => {
						if (data[key].length > 0) {
							payload.append(key, data[key])
						} else {
							delete data[key]
						}
					}
				)

				this._update_product(
					this.get_product.slug,
					payload
				)

				close_modal(this.get_product.slug)

				this._get_products()
			}
		}
	}
</script>
