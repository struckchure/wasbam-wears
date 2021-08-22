// modal

export function open_modal (element) {
	const modal = document.querySelector(`#${element}`)

	modal.style.display = 'block'

	setTimeout(
		() => {
			modal.style.top = '0'
		},
		20
	)

	modal.style.backgroundColor = 'rgba(0, 0, 0, .5)'
}

export function close_modal (element) {
	const modal = document.querySelector(`#${element}`)

	modal.style.backgroundColor = 'transparent'
	modal.style.top = "20%"

	setTimeout(
		() => {
			modal.style.top = "-200%"
		},
		200
	)

	setTimeout(
		() => {
			modal.style.display = 'none'
		},
		1000
	)
}

export function on_click_overlay (element) {
	const modal = document.querySelector(`#${element}`)

	window.addEventListener(
		"click",
		(event) => {
			if (event.target == modal) {
				close_modal(element)
			}
		}
	)
}
