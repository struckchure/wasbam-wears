<template>
	<div class="grid grid-cols-2 gap-4">
		<!-- right -->
		
		<div class="col-start-1 col-end-3">
			<router-link
				class="hover:text-gray-200 w-8 text-2xl text-white font-bold transition duration-200 inline-block align-middle"
				:to="{name: 'Index'}"
			>
				WasBam
			</router-link>
		</div>

		<!-- left -->

		<div class="col-end-7 col-span-2">
			<button
				class="bg-gray-300 rounded-full w-10 h-10 p-2 transition duration-200 hover:shadow-lg"
				@click="open_sidebar('account')"
			>
				<i class="fas fa-bars"></i>
			</button>
		</div>

		<!-- menubar -->

		<SideBar :name="'account'">
			<div class="grid grid-rows-5">
				<div class="row-span-1">
					<div class="border-0 border-b-2 border-gray-300 border-solid p-4">
						<label class="text-gray-600 text-lg">{{ get_full_name }}</label>
						<br>
						<small>{{ get_user.phone_number }}</small>
						<br>
						<small>{{ get_user.email }}</small>
					</div>
				</div>

				<div class="row-span-4">
					<div class="grid grid-cols-1 m-0 p-0">
						<router-link :to="{name: 'Index'}" class="p-0 m-0">
							<button class="menu-button">
								<span><i class="fas fa-home"></i></span>
								<p class="px-2">Home</p>
							</button>
						</router-link>

						<router-link v-if="get_is_admin" :to="{name: 'AdminOrders'}" class="p-0 m-0">
							<button class="menu-button">
								<span><i class="fas fa-user-lock"></i></span>
								<p class="px-2">Admin</p>
							</button>
						</router-link>
						
						<router-link :to="{name: 'Cart'}" class="p-0 m-0">
							<button class="menu-button">
								<span><i class="fas fa-shopping-cart"></i></span>
								<p class="px-2">Cart</p>
							</button>
						</router-link>

						<router-link :to="{name: 'Delivery'}" class="p-0 m-0">
							<button class="menu-button">
								<span><i class="fas fa-shuttle-van"></i></span>
								<p class="px-2">Deliveries</p>
							</button>
						</router-link>

						<router-link v-if="get_is_admin" :to="{name: 'Products'}" class="p-0 m-0">
							<button class="menu-button">
								<span><i class="fas fa-gifts"></i></span>
								<p class="px-2">Products</p>
							</button>
						</router-link>

						<router-link :to="{name: 'Logout'}" class="p-0 m-0">
							<button class="menu-button">
								<span><i class="fas fa-sign-out-alt"></i></span>
								<p class="px-2">Logout</p>
							</button>
						</router-link>
					</div>
				</div>
			</div>
		</SideBar>
	</div>
</template>

<script type="text/javascript">
	import { open_sidebar } from '/@/components/sidebar/sidebar.js'

	export default {
		name: 'NavContent',
		props: {
			user: Object,
			is_authenticated: Boolean,
			is_admin: Boolean
		},
		methods: {
			open_sidebar
		},
		computed: {
			get_user () {
				return this.user
			},
			get_is_authenticated () {
				return this.is_authenticated
			},
			get_is_admin () {
				return this.is_admin
			},
			get_full_name () {
				if (this.get_is_authenticated) {
					return this.get_user.username
				} else {
					return 'You need to login'
				}
			}
		}
	}
</script>
