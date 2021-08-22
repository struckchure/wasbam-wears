<template>
	<Base>
		<template v-slot:nav>
			<div class="">
				<Nav />
			</div>
		</template>

		<template v-slot:body>
			<div class="breadcrumb w-full">
				<p>Cart / </p>
				<p>List</p>
			</div>

			<div class="divider"></div>

			<!-- cart items -->

			<div class="grid grid-cols-1 md:grid-cols-6 md:gap-4">
				<div class="md:col-start-2 md:col-span-4">
					<div class="grid grid-cols-1">
					    <div class="rounded-md bg-gray-300 w-full p-4 grid grid-cols-5">
					    	<button class="col-span-1" @click="check_out">
					    		Check out
					    	</button>
					    	<p class="col-span-4 p-4 font-bold text-right text-bold w-full">
					    		Total {{ _cart.total_price }}
					    	</p>
					    </div>
					    <CartItem
					        v-for="(cart_item, index) in _cart.items"
					        :key="index"
					        :cart_item="cart_item"
					    />
					</div>
				</div>
			</div>

			<Modal
				name="cart_checkout_success"
				header="Alert"
			>
				<template v-slot:body>
					<p>{{ get_check_out_message }}</p>
					<button @click="close_modal('cart_checkout_success')">Ok</button>
				</template>
			</Modal>
		</template>
	</Base>
</template>

<script type="text/javascript">
	import { mapGetters, mapActions } from 'vuex'
	import { GET_CART, CHECKOUT_CART } from '/@/store/types.js'
	import { open_modal, close_modal } from '/@/components/modal/modal.js'

	export default {
		name: 'Cart',
		title () {
			return 'WasBam | Cart | List'
		},
		mounted () {
			this._get_cart()
		},
		computed: {
			...mapGetters({
				_cart: 'get_cart',
				_check_out: 'get_check_out'
			}),
			get_check_out_message () {
				if (this._check_out.success) {
					return this._check_out.success[0]
				} else {
					return 'Checkout failed'
				}
			}
		},
		methods: {
			...mapActions({
				_get_cart: GET_CART,
				_check_out_cart: CHECKOUT_CART
			}),
			close_modal,
			check_out () {
				this._check_out_cart()
				open_modal('cart_checkout_success')
			}
		}

	}
</script>
