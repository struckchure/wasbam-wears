// sidebar

export function open_sidebar (element) {
	document.body.style.overflow = 'hidden'

	const sidebar = document.querySelector(`#${element}`)

	sidebar.style.display = 'block'

	setTimeout(
		() => {
			sidebar.style.right = '0'
		},
		20
	)

	sidebar.style.backgroundColor = 'rgba(0, 0, 0, .5)'
}

export function close_sidebar (element) {
	const sidebar = document.querySelector(`#${element}`)

	sidebar.style.backgroundColor = 'transparent'
	sidebar.style.right = "20%"

	setTimeout(
		() => {
			sidebar.style.right = "-200%"
		},
		200
	)

	setTimeout(
		() => {
			sidebar.style.display = 'none'
		},
		1000
	)

	document.body.style.overflow = 'auto'
}

export function on_click_overlay (element) {
	const sidebar = document.querySelector(`#${element}`)

	window.addEventListener(
		"click",
		(event) => {
			if (event.target == sidebar) {
				close_sidebar(element)
			}
		}
	)
}
