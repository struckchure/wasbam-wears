import { createApp } from 'vue'
import App from '/@/App.vue'

import Logo from '/@/components/Logo.vue'
import Modal from '/@/components/modal/Modal.vue'
import Calendar from '/@/components/calendar/Calender.vue'
import SideBar from '/@/components/sidebar/SideBar.vue'

// components definitions

const components = [
	{
		name: 'Logo',
		component: Logo
	},
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
	}
]

const app = createApp(App)

// global components registration

for (var i = 0; i < components.length; i++) {
	const component = components[i];
	app.component(component.name, component.component)
}
// app.component('Logo', Logo)

export default app
