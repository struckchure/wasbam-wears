import { createRouter, createWebHistory } from 'vue-router'

import Index from '/@/views/Index.vue'

// patients

import PatientRecords from '/@/views/patients/PatientRecords.vue'

export const router = createRouter({
	history: createWebHistory(),
	routes: [
		{
			name: 'Index',
			path: '/',
			component: Index
		}
	]
})
