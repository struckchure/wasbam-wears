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
				<p>Orders </p>
			</div>

			<div class="divider"></div>

			<div class="grid grid-cols-1 md:grid-cols-6 md:gap-4">
				<div class="md:col-start-2 md:col-span-4">
					<div class="grid grid-cols-1">
						<!-- content -->
						<Orders
							:orders="get_orders"
						/>
					</div>
				</div>
			</div>
		</template>
	</Base>
</template>

<script type="text/javascript">
	import { mapGetters, mapActions } from 'vuex'
	import { GET_USER, GET_ALL_RECORDS } from '/@/store/types.js'

	export default {
		name: 'AdminOrders.vue',
		title () {
			return 'WasBam | Orders'
		},
		mounted () {
			this._get_user()
			this.redirectNotAdmin()
		},
		computed: {
			...mapGetters({
				_user: 'get_user',
				_all_records: 'get_all_records'
			}),
			get_orders () {
				return this._all_records
			}
		},
		methods: {
			...mapActions({
				_get_user: GET_USER,
				_get_all_records: GET_ALL_RECORDS
			}),
			redirectNotAdmin () {
				if (this._user.is_superuser) {
					this._get_all_records()
				} else {
					this.$router.push({name: 'Index'})
				}
			}
		}
	}
</script>
