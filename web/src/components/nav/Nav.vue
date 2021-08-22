<template>
	<nav class="top-0 sticky p-2 h-auto">
		<slot>
			<NavContent
				:user="_user"
				:is_authenticated="_is_authenticated"
				:is_admin="_is_admin"
			/>
		</slot>
	</nav>
</template>

<script type="text/javascript">
	import { mapGetters, mapActions } from 'vuex'
	import { GET_USER } from '/@/store/types.js'

	export default {
		name: 'Nav',
		mounted () {
			this._get_user()
		},
		computed: {
			...mapGetters({
				_is_authenticated: 'get_is_authenticated',
				_user: 'get_user'
			}),
			_is_admin () {
				if (this._user && this._is_authenticated) {
					return this._user.is_superuser
				} else {
					return false
				}
			}
		},
		methods: {
			...mapActions({
				_get_user: GET_USER
			})
		}
	}
</script>
