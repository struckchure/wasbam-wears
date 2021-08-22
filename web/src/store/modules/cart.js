import { getCookie, api, Storage } from '/@/store/utils.js'
import {
	SET_CART,
	GET_CART,
	SET_CART_ITEM,
	GET_CART_ITEM,
	ADD_CART_ITEM,
	SET_CART_ITEM_EXISTS,
	UPDATE_CART_ITEM,
	DELETE_CART_ITEM,
	FILTER_CART_ITEM_BY_PRODUCT,
	CHECKOUT_CART,
	CHECKOUT_FAILED,
	CHECKOUT_SUCCESS,
	SET_ERROR
} from '/@/store/types.js';
import { router } from '/@/router/index.js'


const storage = new Storage();


const state = {
	cart: {},
	cart_item: {},
	cart_item_exists: false,
	cart_check_out: {}
}

const getters = {
	get_cart (state) {
		return state.cart
	},
	get_cart_item (state) {
		if (Object.keys(state.cart_item).length > 0) {
			return state.cart_item
		} else {
			return null
		}
	},
	get_cart_item_exists (state) {
		return state.cart_item_exists
	},
	get_check_out (state) {
		return state.cart_check_out
	}
}

const mutations = {
	[SET_CART] (state, cart) {
		state.cart = cart
	},
	[SET_CART_ITEM] (state, item) {
		state.cart_item = item
	},
	[SET_CART_ITEM_EXISTS] (state, exists) {
		state.cart_item_exists = exists
	},
	[CHECKOUT_FAILED] (state, payload) {
		state.cart_check_out = payload
	},
	[CHECKOUT_SUCCESS] (state, payload) {
		state.cart_check_out = payload
	}
}

const actions = {
	async [GET_CART] (context) {
		await api({
			method: 'get',
			url: '/cart/',
			headers: {
				"Content-Type": "application/json",
				'Authorization': `Token ${storage.get('token')}`
			}
		})
		.then(
			function(response) {
				context.commit(SET_CART, response.data)
			}
		)
		.catch(
			function(error) {
				context.commit(SET_ERROR, error.response.data)
			}
		)
	},
	async [GET_CART_ITEM] (context, cart_item_slug) {
		await api({
			method: 'get',
			url: `/cart/${cart_item_slug}/details/`,
			headers: {
				"Content-Type": "application/json",
				'Authorization': `Token ${storage.get('token')}`
			}
		})
		.then(
			function (response) {
				context.commit(SET_CART_ITEM, response.data)
			}
		)
		.catch(
			function (error) {
				context.commit(SET_ERROR, error.response.data)
			}
		)
	},
	[FILTER_CART_ITEM_BY_PRODUCT] (context, product_slug) {
		return new api(
			{
				method: 'get',
				url: `/cart/${product_slug}/filter/`,
				headers: {
					"Content-Type": "application/json",
					'Authorization': `Token ${storage.get('token')}`
				}
			})
			.then(
				function(response) {
					context.commit(SET_CART_ITEM, response.data)

					return response.data
				}
			)
			.catch(
				function(error) {
					return error.data
				}
			)
	},
	async [ADD_CART_ITEM] (context, item) {
		await api({
			method: 'post',
			url: '/cart/add-item/',
			headers: {
				"Content-Type": "application/json",
				"X-CSRFToken": getCookie('csrftoken'),
				'Authorization': `Token ${storage.get('token')}`
			},
			data: item
		})
		.then(
			function(response) {
				context.commit(SET_CART_ITEM, response.data)
			}
		)
		.catch(
			function(error) {
				context.commit(SET_ERROR, error.response.data)
			}
		)
	},
	async [UPDATE_CART_ITEM] (context, slug, item) {
		await api({
			method: 'post',
			url: `/cart/${slug}/update/`,
			headers: {
				"Content-Type": "application/json",
				"X-CSRFToken": getCookie('csrftoken'),
				'Authorization': `Token ${storage.get('token')}`
			},
			data: item
		})
		.then(
			function(response) {
				context.commit(SET_CART_ITEM, response.data)
				context.dispatch(GET_CART)
			}
		)
		.catch(
			function(error) {
				context.commit(SET_ERROR, error.response.data)
			}
		)
	},
	async [DELETE_CART_ITEM] (context, slug) {
		await api({
			method: 'get',
			url: `/cart/${slug}/delete/`,
			headers: {
				"Content-Type": "application/json",
				'Authorization': `Token ${storage.get('token')}`
			}
		})
		.then(
			function(response) {
				context.dispatch(GET_CART)
			}
		)
		.catch(
			function(error) {
				context.commit(SET_ERROR, error.response.data)
			}
		)
	},
	async [CHECKOUT_CART] (context) {
		await api({
			method: 'get',
			url: '/cart/check-out/',
			headers: {
				'Content-Type': 'application/json',
				'Authorization': `Token ${storage.get('token')}`
			}
		})
		.then(
			function (response) {
				context.commit(CHECKOUT_SUCCESS, response.data)
				router.push({name: 'Delivery'})
			}
		)
		.catch(
			function (error) {
				context.commit(CHECKOUT_FAILED, error.response)
			}
		)
		context.dispatch(GET_CART)
	}
}

export default {
	state,
	getters,
	mutations,
	actions
}
