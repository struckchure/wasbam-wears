<template>
	<div class="cart-item" v-if="get_delivery_item">
		<div class="cart-item-image">
			<img :src="get_delivery_item.product.image" alt="N/A">
		</div>

		<div class="cart-item-content">
			<p>
				{{ get_delivery_item.product.name }}
			</p>
			<br>
			<small>
				{{ get_delivery_item.product.description }}
			</small>
			<br>
			<label
				class="mt-2 rounded-md p-2 text-white"
				:class="[get_delivery_item.status ? 'bg-green-400' : 'bg-blue-700']"
			>
				{{ get_delivery_status }}
			</label>
		</div>

		<div class="cart-item-price">
			<small>Qty</small>
			<small>Per unit</small>
			<small>Total</small>
			<p>
				X {{ get_delivery_item.quantity }}
				<br>
			</p>

			<p>
				&#8358; {{ get_delivery_item.product.price }}
				<br>
			</p>

			<p>
				&#8358; {{ get_delivery_item_total }}
				<br>
			</p>
		</div>

		<Modal
			:name="`confirm_delivery_item_done_${get_delivery_item.slug}`"
			header="Confirming Request"
		>
			<template v-slot:body>
				<p>				
					Are you confirming you have recieved your {{ get_delivery_item.product.name }}?
				</p>

				<div>
					<button @click="confirm_order_recieved">Yes</button>
					<button @click="close_modal(`confirm_delivery_item_done_${get_delivery_item.slug}`)">No</button>
				</div>
			</template>
		</Modal>

		<button
			v-if="get_can_edit"
			class="cart-item-delete"
			:class="[get_delivery_item.status ? 'bg-gray-200' : 'bg-green-800']"
			:disabled="get_delivery_item.status"
			@click="open_modal(`confirm_delivery_item_done_${get_delivery_item.slug}`)"
		>
			<i class="fas fa-check"></i>
		</button>
	</div>
</template>

<script type="text/javascript">
	import { mapActions } from 'vuex'
	import {
		CONFIRM_ORDER_RECIEVED
	} from '/@/store/types.js'
	import { open_modal, close_modal } from '/@/components/modal/modal.js'

	export default {
		name: 'DeliveryItem',
		props: {
			delivery_item: Object,
			can_edit: Boolean
		},
		computed: {
			get_delivery_item () {
				if (this.delivery_item.product) {
					return this.delivery_item
				}
			},
			get_can_edit () {
				return this.can_edit
			},
			get_delivery_item_total () {
				return this.get_delivery_item.quantity * this.get_delivery_item.product.price
			},
			get_delivery_status () {
				if (this.get_delivery_item.status) {
					return 'Delivered'
				} else {
					return 'In Progress'
				}
			}
		},
		methods: {
			...mapActions({
				_confirm_order_recieved: CONFIRM_ORDER_RECIEVED
			}),
			open_modal,
			close_modal,
			confirm_order_recieved () {
				this._confirm_order_recieved(this.get_delivery_item.slug)

				close_modal(`confirm_delivery_item_done_${this.get_delivery_item.slug}`)
			}
		}
	}
</script>
