<template>
	<Base>
		<template v-slot:nav>
			<div class="">
				<Nav />
			</div>
		</template>

		<template v-slot:body>
			<div class="breadcrumb w-full">
				<p>Delivery /</p>
				<p>List </p>
			</div>

			<div class="divider"></div>

			<div class="grid grid-cols-1 md:grid-cols-6 md:gap-4">
				<div class="md:col-start-2 md:col-span-4">
					<div class="grid grid-cols-1">
						<!-- content -->
						<div class="w-full p-4">
							<button
								class="bg-red-700 text-white border-none"
								@click="delete_completed"
							>
								Delete Completed
							</button>
						</div>

						<DeliveryItem
							v-for="(delivery_item, index) in get_deliveries"
							:key="index"
							:delivery_item="delivery_item"
							:can_edit="true"
						/>
					</div>
				</div>
			</div>
		</template>
	</Base>
</template>

<script type="text/javascript">
	import { mapGetters, mapActions } from 'vuex'
	import { GET_RECORDS, DELETE_COMPLETED_ORDERS } from '/@/store/types.js'

	export default {
		name: 'Delivery',
		title () {
			return 'WasBam | Deliveries'
		},
		mounted () {
			this._get_records()
		},
		computed: {
			...mapGetters({
				_deliveries: 'get_records'
			}),
			get_deliveries () {
				return this._deliveries
			}
		},
		methods: {
			...mapActions({
				_get_records: GET_RECORDS,
				_delete_completed: DELETE_COMPLETED_ORDERS
			}),
			delete_completed () {
				this._delete_completed()
			}
		}
	}
</script>
