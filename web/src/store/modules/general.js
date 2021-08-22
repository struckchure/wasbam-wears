import {
	TOGGLE_LOADING,
	SET_BUSY,
	SET_DONE,
	SET_ERROR,
	CLEAR_ERROR
} from '/@/store/types.js'
import { open_modal } from '/@/components/modal/modal.js'


const state = {
	is_loading: false,
	error: {}
};

const getters = {
	get_is_loading (state) {
		return state.is_loading
	},
	get_error (state) {
		if (Object.keys(state.error).length > 0) {
			return state.error
		}

		return null
	}
};

const mutations = {
	[TOGGLE_LOADING] (state, status) {
		state.is_loading = status
	},
	[SET_ERROR] (state, error) {
		state.error = error
		open_modal('app_error_modal')
	},
	[CLEAR_ERROR] (state) {
		state.error = {}
	}
};

const actions = {
	[SET_BUSY] (context) {
		context.dispatch(TOGGLE_LOADING, true)
	},
	[SET_DONE] (context) {
		context.dispatch(TOGGLE_LOADING, false)
	}
};

export default {
	state,
	getters,
	mutations,
	actions
};
