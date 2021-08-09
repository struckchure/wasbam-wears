<template>
	<div class="flex justify-center">
		<i class="fas fa-hospital-symbol text-white" :class="get_class"></i>
	</div>
</template>

<script type="text/javascript">
	export default {
		name: 'Logo',
		props: [
			'class'
		],
		computed: {
			get_class () {
				if (this.class) {
					return this.class
				} else {
					return "text-5xl"
				}
			}
		}
	}
</script>
