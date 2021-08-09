<template>
	<div class="sidebar" :id="get_name">
		<div class="sidebar-content">		
			<slot></slot>
		</div>

		<button class="float-right cancel-button" @click="close_sidebar">
			<i class="fas fa-arrow-right text-white hover:text-gray-200"></i>
		</button>
	</div>
</template>

<script type="text/javascript">
	import {
		close_sidebar,
		on_click_overlay
	} from '/@/components/sidebar/sidebar.js'

	export default {
		name: 'SideBar',
		props: [
			'name'
		],
		computed: {
			get_name () {
				return this.name
			}
		},
		mounted () {
			on_click_overlay(this.get_name)
		},
		methods: {
			close_sidebar () {
				close_sidebar(this.get_name)
			}
		}
	}
</script>
