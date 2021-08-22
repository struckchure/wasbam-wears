import { createStore } from 'vuex'

import general from '/@/store/modules/general.js'
import products from '/@/store/modules/products.js'
import cart from '/@/store/modules/cart.js'
import accounts from '/@/store/modules/accounts.js'
import records from '/@/store/modules/records.js'


export const store = createStore(
	{
		modules: {
			general,
			products,
			cart,
			accounts,
			records
		}
	}
)
