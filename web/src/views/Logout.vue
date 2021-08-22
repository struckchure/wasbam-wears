<template>
	<div>
		<Modal
			name="confirm_logout"
			header="Confirming Request"
			:persistent="true"
		>
			<template v-slot:body>
				<p>				
					Are you sure you want to end your session?
				</p>

				<div>
					<button @click="logout_user">Yes</button>
					<button @click="cancel_request">No</button>
				</div>
			</template>
		</Modal>
	</div>
</template>

<script type="text/javascript">
	import { open_modal, close_modal } from '/@/components/modal/modal.js'
	import { AUTH_LOGOUT } from '/@/store/types.js'
	import { mapActions } from 'vuex'

	export default {
		name: 'Logout',
		title () {
			return 'WasBam | Logout'
		},
		mounted () {
			open_modal('confirm_logout')
		},
		methods: {
			...mapActions({
				_logout: AUTH_LOGOUT
			}),
			cancel_request () {
				close_modal('confirm_logout')

				history.back()
			},
			logout_user () {
				close_modal('confirm_logout')

				this._logout()
			}
		}
	}
</script>
