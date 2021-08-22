<template>
	<div class="w-full h-screen bg-white p-0 m-0">
		<slot name="nav">
			<div class="nav bg-blend-color md:bg-blend-normal bg-gray-500 md:bg-white h-5/6">
				<Nav />

				<div class="container mx-auto p-4 pt-0 h-full">
					<p class="text-white md:text-black md:w-4/6 text-3xl w-full h-full flex items-center font-cursive">
						Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
						tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
						quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
						consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
						cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
						proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
					</p>
				</div>
			</div>
		</slot>

		<div class="container p-4 md:mx-auto">
			<slot name="body">
			</slot>
		</div>

		<slot name="footer">
			<footer class="bottom-0 py-2">
				<p class="w-full text-center">WasBam | Copyrights</p>
				<p class="w-full text-center text-gray-600">{{ year }}</p>
			</footer>
		</slot>
	</div>
</template>

<script type="text/javascript">
	export default {
		name: 'Base',
		computed: {
		    year () {
		        const current_date = new Date()
		        return current_date.getFullYear()
		    }
		}
	}
</script>
