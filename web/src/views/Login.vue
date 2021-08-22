<template>
	<div class="auth-form">
		<form @submit.prevent="login_user">
			<div>
				<router-link :to="{name: 'Index'}" class="text-2xl mx-0">
					WasBam
				</router-link>
			</div>

			<div class="divider my-4"></div>

			<div>
				<label>Username</label>
				<input type="text" v-model="username" required />
			</div>

			<div>
				<label>Password</label>
				<input type="password" v-model="password" required />
			</div>

			<div class="grid grid-cols-6 p-0 py-2">
				<input class="col-span-1 m-0" type="checkbox" v-model="remember_me" />
				<label class="col-span-5">Remember me</label>
			</div>

			<div>
				<button>Login</button>
			</div>

			<div>
				<p>
					Don't have an account?<router-link :to="{name: 'Register'}">register</router-link>
				</p>
			</div>
		</form>
	</div>
</template>

<script type="text/javascript">
	import { mapActions } from 'vuex'
	import { AUTH_LOGIN } from '/@/store/types.js'

	export default {
		name: 'Login',
		title () {
			return 'WasBam | Login'
		},
		data () {
			return {
				username: '',
				password: '',
				remember_me: false
			}
		},
		methods: {
			...mapActions({
				_login_user: AUTH_LOGIN
			}),
			login_user () {
				const user_data = {
					username: this.username,
					password: this.password
				}

				this._login_user(user_data)
			}
		}
	}
</script>
