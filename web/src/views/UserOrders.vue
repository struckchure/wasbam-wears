<template>
	<Base>
		<template v-slot:nav>
			<div class="">
				<Nav />
			</div>
		</template>

		<template v-slot:body>
			<div class="breadcrumb w-full">
				<p>Admin /</p>
				<router-link :to="{name: 'AdminOrders'}">
					<p>Orders /</p>
				</router-link>
				<p>{{ get_username }}</p>
			</div>

			<div class="divider"></div>

			<div class="grid grid-cols-1 md:grid-cols-6 md:gap-4">
				<div class="md:col-start-2 md:col-span-4">
					<div class="grid grid-cols-1">
						<DeliveryItem
							v-for="(delivery_item, index) in get_deliveries"
							:key="index"
							:delivery_item="delivery_item"
							:can_edit="false"
						/>
					</div>
				</div>
			</div>
		</template>
	</Base>
</template>

<script type="text/javascript">
	import { mapGetters, mapActions } from 'vuex'
	import { GET_USER_RECORDS } from '/@/store/types.js'

	export default {
		name: 'UserOrders',
		title () {
			return `WasBam | Orders | ${this.get_username}`
		},
		props: {
			username: String
		},
		mounted () {
			this._get_user_records(this.get_username)
		},
		computed: {
			...mapGetters({
				_user_records: 'get_user_records'
			}),
			get_username () {
				return this.username
			},
			get_deliveries () {
				return this._user_records
			}
		},
		methods: {
			...mapActions({
				_get_user_records: GET_USER_RECORDS
			})
		}
	}
</script>
