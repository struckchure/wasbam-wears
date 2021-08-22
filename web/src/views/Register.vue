<template>
	<div class="auth-form">
		<form @submit.prevent="register_user">
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
				<label>E-Mail</label>
				<input type="email" v-model="email" required />
			</div>

			<div>
				<label>Phone number <br><small>starts with 234</small></label>
				<input type="number" v-model="phone_number" required />
			</div>

			<div>
				<label>Password</label>
				<input type="password" v-model="password1" required />
			</div>

			<div>
				<label>Password (Again)</label>
				<input type="password" v-model="password2" required />
			</div>

			<div>
				<button>Register</button>
			</div>

			<div>
				<p>
					Already have an account?<router-link :to="{name: 'Login'}">login</router-link>
				</p>
			</div>

			<Modal
				name="register_error_modal"
				header="Alert"
			>
				<template v-slot:body>
					<p>{{ get_error }}</p>
					<div>
						<button @click="close_modal('register_error_modal')">Ok</button>
					</div>
				</template>
			</Modal>
		</form>
	</div>
</template>

<script type="text/javascript">
	import { mapActions } from 'vuex'
	import { AUTH_REGISTER } from '/@/store/types.js'
	import { open_modal, close_modal } from '/@/components/modal/modal.js'

	export default {
		name: 'Register',
		title () {
			return 'WasBam | Register'
		},
		data () {
			return {
				username: '',
				email: '',
				phone_number: '',
				password1: '',
				password2: '',
				error: ''
			}
		},
		computed: {
			get_error () {
				return this.error
			}
		},
		methods: {
			...mapActions({
				_register_user: AUTH_REGISTER
			}),
			close_modal,
			register_user () {
				if (this.password1 == this.password2) {
					const user_data = {
						username: this.username,
						email: this.email,
						phone_number: this.phone_number,
						password: this.password1
					}

					this._register_user(user_data)
				} else {
					this.error = 'Passwords mismatch'
					open_modal('register_error_modal')
				}
			}
		}
	}
</script>
