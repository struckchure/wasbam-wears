import { getCookie, api, Storage } from '/@/store/utils.js'
import {
	AUTH_LOGIN,
	AUTH_LOGOUT,
	AUTH_REGISTER,
	AUTH_SUCCESS,
	AUTH_FAILED,
	GET_USER,
	SET_ERROR
} from '/@/store/types.js'
import { router } from '/@/router/index.js'
import { redirectNotAuthenticated } from '/@/store/decorators.js'


const storage = new Storage();


const state = {
	user: {}
}

const getters = {
	get_user () {
		return state.user
	},
	get_is_authenticated () {
		if (storage.get('token')) {
			return true
		} else {
			return false
		}
	}
}

const mutations = {
	[AUTH_SUCCESS] (state, payload) {
		state.user = payload.user
		storage.set('token', payload.token)
	},
	[AUTH_FAILED] (state, payload) {}
}

const actions = {
	async [AUTH_LOGIN] (context, user_data) {
		await api({
			method: 'post',
			url: '/accounts/login/',
			headers: {
				'Content-Type': 'application/json',
				'X-CSRFToken': getCookie('csrftoken')
			},
			data: user_data
		})
		.then(
			function (response) {
				context.commit(AUTH_SUCCESS, response.data)

				router.push({name: 'Index'})
			}
		)
		.catch(
			function (error) {
				// context.commit(AUTH_FAILED, error.response.data)
				context.commit(SET_ERROR, error.response.data)
			}
		)
	},
	[AUTH_LOGOUT] (context) {
		storage.remove('token')
		context.commit(AUTH_FAILED, null)

		router.push({name: "Login"})
	},
	async [AUTH_REGISTER] (context, user_data) {
		await api({
			method: 'post',
			url: '/accounts/register/',
			headers: {
				'Content-Type': 'application/json',
				'X-CSRFToken': getCookie('csrftoken')
			},
			data: user_data
		})
		.then(
			function (response) {
				context.commit(AUTH_SUCCESS, response.data)

				router.push({name: 'Index'})
			}
		)
		.catch(
			function (error) {
				// context.commit(AUTH_FAILED, error.response.data)
				context.commit(SET_ERROR, error.response.data)
			}
		)
	},
	async [GET_USER] (context) {
		if (storage.get('token')) {
			await api({
				method: 'get',
				url: '/accounts/',
				headers: {
					'Content-Type': 'application/json',
					'X-CSRFToken': getCookie('csrftoken'),
					'Authorization': `Token ${storage.get('token')}`
				}
			})
			.then(
				function (response) {
					context.commit(AUTH_SUCCESS, response.data)
				}
			)
			.catch(
				function (error) {
					// context.commit(AUTH_FAILED, error.response.data)
					context.commit(SET_ERROR, error.response.data)
				}
			)
		} else {
			context.commit(AUTH_FAILED, null)
		}
	}
}


export default {
	state,
	getters,
	mutations,
	actions
}
