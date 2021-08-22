import { getCookie, api, Storage } from '/@/store/utils.js'
import {
	GET_RECORDS,
	SET_RECORDS,
	CREATE_RECORD,
	CONFIRM_ORDER_RECIEVED,
	DELETE_COMPLETED_ORDERS,
	GET_ALL_RECORDS,
	SET_ALL_RECORDS,
	GET_USER_RECORDS,
	SET_USER_RECORDS,
	SET_ERROR
} from '/@/store/types.js'
import { router } from '/@/router/index.js'


const storage = new Storage()


const state = {
	records: [],
	all_records: [],
	user_records: []
}

const getters = {
	get_records (state) {
		return state.records
	},
	get_all_records (state) {
		return state.all_records
	},
	get_user_records (state) {
		return state.user_records
	}
}

const mutations = {
	[SET_RECORDS] (state, records) {
		state.records = records
	},
	[SET_ALL_RECORDS] (state, all_records) {
		state.all_records = all_records
	},
	[SET_USER_RECORDS] (state, user_records) {
		state.user_records = user_records
	}
}

const actions = {
	async [GET_RECORDS] (context) {
		await api({
			method: 'get',
			url: '/records',
			headers: {
				'Content-Type': 'application/json',
				'Authorization': `Token ${storage.get('token')}`
			}
		})
		.then(
			function (response) {
				context.commit(SET_RECORDS, response.data)
			}
		)
		.catch(
			function (error) {
				context.commit(SET_ERROR, error.response.data)
			}
		)
	},
	async [CREATE_RECORD] (context, item_data) {
		await api({
			method: 'post',
			url: '/records/create/',
			headers: {
				'Content-Type': 'application/json',
				'Authorization': `Token ${storage.get('token')}`,
				'X-CSRFToken': getCookie('csrftoken')
			}
		})
		.then(
			function (response) {
				context.dispatch(GET_RECORDS)
				router.push({name: 'Delivery'})
			}
		)
		.catch(
			function (error) {
				context.commit(SET_ERROR, error.response.data)
			}
		)
	},
	async [CONFIRM_ORDER_RECIEVED] (context, record_slug) {
		await api({
			method: 'get',
			url: `/records/${record_slug}/confirm-order/`,
			headers: {
				'Content-Type': 'application/json',
				'Authorization': `Token ${storage.get('token')}`
			}
		})
		.then(
			function (response) {
				context.dispatch(GET_RECORDS)
			}
		)
		.catch(
			function (error) {
				context.commit(SET_ERROR, error.response.data)
			}
		)
	},
	async [DELETE_COMPLETED_ORDERS] (context) {
		await api({
			method: 'get',
			url: '/records/delete-completed/',
			headers: {
				'Content-Type': 'application/json',
				'Authorization': `Token ${storage.get('token')}`
			}
		})
		.then(
			function (response) {
				context.dispatch(GET_RECORDS)
			}
		)
		.catch(
			function (error) {
				context.commit(SET_ERROR, error.response.data)
			}
		)
	},
	async [GET_ALL_RECORDS] (context) {
		await api({
			method: 'get',
			url: '/records/user-groups/',
			headers: {
				'Content-Type': 'application/json',
				'Authorization': `Token ${storage.get('token')}`
			}
		})
		.then(
			function (response) {
				context.commit(SET_ALL_RECORDS, response.data)
			}
		)
		.catch(
			function (error) {
				context.commit(SET_ERROR, error.response.data)
			}
		)
	},
	async [GET_USER_RECORDS] (context, username) {
		await api({
			method: 'get',
			url: `/records/${username}/all`,
			headers: {
				'Content-Type': 'applications/json',
				'Authorization': `Token ${storage.get('token')}`,
				'X-CSRFToken': getCookie('csrftoken')
			}
		})
		.then(
			function (response) {
				context.commit(SET_USER_RECORDS, response.data)
			}
		)
		.catch(
			function (error) {
				context.commit(SET_ERROR, error.response.data)
			}
		)
	}
}

export default {
	state,
	getters,
	mutations,
	actions
}
