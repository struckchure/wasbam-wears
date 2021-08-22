import { router } from '/@/router/index.js'
import { store } from '/@/store/index.js'
import { Storage } from '/@/store/utils.js'


const storage = new Storage();


export function redirectNotAuthenticated(redirect=true) {
	if (!storage.get('token')) {
		if (redirect) {
			router.push({name: 'Login'})
		}

		return true
	} else {
		return false
	}
}
