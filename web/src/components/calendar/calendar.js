export const day_keys = {
	0: 'Sunday',
	1: 'Monday',
	2: 'Tuesday',
	3: 'Wednesday',
	4: 'Thursday',
	5: 'Friday',
	6: 'Saturday'
}

export const month_keys = {
	0: 'January',
	1: 'February',
	2: 'March',
	3: 'April',
	4: 'May',
	5: 'June',
	6: 'July',
	7: 'August',
	8: 'September',
	9: 'October',
	10: 'November',
	11: 'December'
}

export function days_in_month(year, month) {
	const date = new Date(year, month, 0).getDate()
	const days = new Array()

	for (var i = 1; i <= date; i++) {
		days.push(i)
	}

	return days
}

export function get_first_day_of_month(year, month, day) {
	if (month <= 0) {
		month = 1
	}
	month -= 1

	const date = new Date(year, month, day)

	return day_keys[date.getDay()]
}
