<template>
	<div class="toast" :id="get_name">
		<div class="toast-content">
			<slot name="body">
			</slot>
		</div>
	</div>
</template>

<script type="text/javascript">
	export default {
		name: 'Toast',
		props: [
			'name'
		],
		computed: {
			get_name () {
				return this.name
			}
		}
	}
</script>
