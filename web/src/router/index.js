import { createRouter, createWebHistory } from 'vue-router'

import Index from '/@/views/Index.vue'
import Products from '/@/views/Products.vue'
import Cart from '/@/views/Cart.vue'
import Delivery from '/@/views/Delivery.vue'
import Login from '/@/views/Login.vue'
import Register from '/@/views/Register.vue'
import Logout from '/@/views/Logout.vue'
import AdminOrders from '/@/views/AdminOrders.vue'
import UserOrders from '/@/views/UserOrders.vue'

import { Storage } from '/@/store/utils.js'


export const router = createRouter({
	history: createWebHistory(),
	routes: [
		{
			name: 'Index',
			path: '/',
			component: Index
		},
		{
			name: 'Products',
			path: '/products',
			component: Products
		},
		{
			name: 'Cart',
			path: '/cart',
			component: Cart,
			meta: {
				loginRequired: true
			}
		},
		{
			name: 'Delivery',
			path: '/delivery',
			component: Delivery,
			meta: {
				loginRequired: true
			}
		},
		{
			name: 'AdminOrders',
			path: '/admin-orders',
			component: AdminOrders,
			meta: {
				loginRequired: true,
				adminRequired: true
			}
		},
		{
			name: 'UserOrders',
			path: '/admin-orders/:username',
			component: UserOrders,
			props: true,
			meta: {
				loginRequired: true,
				adminRequired: true
			}
		},
		{
			name: 'Login',
			path: '/accounts/login',
			component: Login
		},
		{
			name: 'Register',
			path: '/accounts/register',
			component: Register
		},
		{
			name: 'Logout',
			path: '/accounts/logout',
			component: Logout
		}
	]
})

router.beforeEach((to, from, next) => {
	const storage = new Storage()
	const is_authenticated = storage.get('token')
	const login_required = to.matched.some(record => record.meta.loginRequired)

	if (!is_authenticated && login_required) {
		next({name: 'Login'})
	} else {
		next()
	}
})
