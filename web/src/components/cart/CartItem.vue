<template>
	<div class="cart-item" v-if="get_cart_item">
		<div class="cart-item-image">
			<img :src="get_cart_item.product.image" alt="N/A">
		</div>

		<div class="cart-item-content">
			<p>
				{{ get_cart_item.product.name }}
			</p>
			<br>
			<small>
				{{ get_cart_item.product.description }}
			</small>
		</div>

		<div class="cart-item-price">
			<small>Qty</small>
			<small>Per unit</small>
			<small>Total</small>
			<p>
				X {{ get_cart_item.quantity }}
				<br>
			</p>

			<p>
				&#8358; {{ get_cart_item.product.price }}
				<br>
			</p>

			<p>
				&#8358; {{ get_cart_item_total }}
				<br>
			</p>
		</div>

		<Modal
			name="confirm_delete_cart_item"
			header="Confirming Request"
			:persistent="true"
		>
			<template v-slot:body>
				<p>				
					Are you sure you want to delete {{ get_cart_item.name }}?
				</p>

				<div>
					<button @click="delete_cart_item">Yes</button>
					<button @click="close_modal('confirm_delete_cart_item')">No</button>
				</div>
			</template>
		</Modal>

		<button class="cart-item-delete"
			@click="open_modal('confirm_delete_cart_item')"
		>
			<i class="fas fa-trash"></i>
		</button>
	</div>
</template>

<script type="text/javascript">
	import { mapActions } from 'vuex'
	import {
		DELETE_CART_ITEM
	} from '/@/store/types.js'
	import { open_modal, close_modal } from '/@/components/modal/modal.js'

	export default {
		name: 'CartItem',
		props: {
			cart_item: Object
		},
		computed: {
			get_cart_item () {
				if (this.cart_item.product) {
					return this.cart_item
				}
			},
			get_cart_item_total () {
				return this.get_cart_item.quantity * this.get_cart_item.product.price
			}
		},
		methods: {
			...mapActions({
				_delete_cart_item: DELETE_CART_ITEM
			}),
			open_modal,
			close_modal,
			delete_cart_item () {
				this._delete_cart_item(this.get_cart_item.slug)

				close_modal('confirm_delete_cart_item')
			}
		}
	}
</script>
