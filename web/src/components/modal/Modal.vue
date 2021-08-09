<template>
	<div class="modal" :id="get_name">
		<div class="modal-content">
			<div class="modal-header">
				<div>
					<slot name="header">
						<b>{{ get_header }}</b>
					</slot>
				</div>

				<div>
					<button
						class="cancel-button"
						@click="close_modal(get_name)"
					>
						<i class="fas fa-arrow-up"></i>
					</button>
				</div>
			</div>

			<div class="modal-body">
				<slot name="body"></slot>
			</div>

			<div class="modal-footer">
				<slot name="footer">
					{{ get_footer }}
				</slot>
			</div>
		</div>
	</div>
</template>

<script type="text/javascript">
	import {
		close_modal,
		on_click_overlay
	} from '/@/components/modal/modal.js'

	export default {
		name: 'Modal',
		props: [
			'name',
			'header',
			'footer'
		],
		mounted () {
			on_click_overlay(this.get_name)
		},
		computed: {
			get_name () {
				return this.name
			},
			get_header () {
				return this.header
			},
			get_footer () {
				return this.footer
			}
		},
		methods: {
			close_modal
		}
	}
</script>
