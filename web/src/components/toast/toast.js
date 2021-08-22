// toast

export function open_toast (element) {
	const toast = document.querySelector(`#${element}`)

	toast.style.display = 'block'

	setTimeout(
		() => {
			toast.style.top = '0'
		},
		20
	)
	close_toast(element)
}

export function close_toast (element) {
	const toast = document.querySelector(`#${element}`)

	setTimeout(
		() => {
			toast.style.top = "-100%"
		},
		10000
	)

	setTimeout(
		() => {

			toast.style.display = 'none'
		},
		500
	)
}
