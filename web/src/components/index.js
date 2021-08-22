import { createApp } from 'vue'
import App from '/@/App.vue'

import Modal from '/@/components/modal/Modal.vue'
import Calendar from '/@/components/calendar/Calender.vue'
import SideBar from '/@/components/sidebar/SideBar.vue'
import Toast from '/@/components/toast/Toast.vue'

import Logo from '/@/components/Logo.vue'
import Base from '/@/components/Base.vue'
import Nav from '/@/components/nav/Nav.vue'
import NavContent from '/@/components/nav/NavContent.vue'
import Product from '/@/components/products/Product.vue'
import CartItem from '/@/components/cart/CartItem.vue'
import DeliveryItem from '/@/components/delivery/DeliveryItem.vue'
import Orders from '/@/components/orders/Orders.vue'

// components definitions

const components = [
	{
		name: 'Modal',
		component: Modal
	},
	{
		name: 'Calendar',
		component: Calendar
	},
	{
		name: 'SideBar',
		component: SideBar
	},
	{
		name: 'Toast',
		component: Toast
	},

	// custom

	{
		name: 'Logo',
		component: Logo
	},
	{
		name: 'Base',
		component: Base
	},
	{
		name: 'Nav',
		component: Nav
	},
	{
		name: 'NavContent',
		component: NavContent
	},
	{
		name: 'Product',
		component: Product
	},
	{
		name: 'CartItem',
		component: CartItem
	},
	{
		name: 'DeliveryItem',
		component: DeliveryItem
	},
	{
		name: 'Orders',
		component: Orders
	}
]

const app = createApp(App)

// global components registration

for (var i = 0; i < components.length; i++) {
	const component = components[i];
	app.component(component.name, component.component)
}

export default app
