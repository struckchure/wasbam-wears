<template>
	<div class="calendar">
		<div class="month">
			<button @click="previous_month">
				<i class="fas fa-arrow-left"></i>
			</button>

			<label class="mx-1 w-full text-center bg-transparent">
				<span>{{ get_month }}</span>

				<span v-if="!get_is_date_picker">{{ year }}</span>
				<input
					v-else
					type="number"
					min="1800"
					:max="new Date().getFullYear()"
					v-model="year"
				/>
			</label>

			<button  @click="next_month">
				<i class="fas fa-arrow-right"></i>
			</button>
		</div>

		<div class="days-label">
			<label>s</label>
			<label>m</label>
			<label>t</label>
			<label>w</label>
			<label>t</label>
			<label>f</label>
			<label>s</label>
		</div>

		<div class="days">
			<label
				v-for="(day, index) in get_days"
				:key="index"
				@click="pick_date(day)"
			>
				{{ day }}
			</label>
		</div>
	</div>
</template>

<script type="text/javascript">
	import {
		days_in_month,
		get_first_day_of_month,
		day_keys,
		month_keys
	} from '/@/components/calendar/calendar.js'

	export default {
		name: 'Calendar',
		props: {
			is_date_picker: {
				type: Boolean
			}
		},
		data () {
			return {
				year: new Date().getFullYear(),
				month: new Date().getMonth() + 1
			}
		},
		computed: {
			start_day () {
				return get_first_day_of_month(this.get_year, this.month, 1)
			},
			get_days () {
				const days = days_in_month(this.get_year, this.month)

				const start_day = this.start_day
				const start_day_key = Object.values(day_keys).indexOf(start_day)
				const start_day_distance = start_day_key + 1

				for (var i = 1; i < start_day_distance; i++) {
					days.unshift("")
				}

				return days
			},
			get_month () {
				return month_keys[this.month - 1]
			},
			get_year () {
				return this.year
			},
			get_is_date_picker () {
				return this.is_date_picker
			}
		},
		methods: {
			pick_date (day) {
				if (day != "") {
					if (this.is_date_picker) {
						var date = new Date(this.year, this.month - 1, day)

						this.$emit('on_date_selected', date)
					}
				} 
			},
			previous_month () {
				if (this.month <= 1) {
					this.year -= 1
					this.month = 12
				} else {
					this.month -= 1
				}
			},
			next_month () {
				if (this.month >= 12) {
					this.year += 1
					this.month = 1
				} else {
					this.month += 1
				}
			}
		}
	}
</script>
