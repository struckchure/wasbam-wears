import app from '/@/components/index.js'

import '/@/assets/css/style.css'
import '/@/assets/css/widgets.css'
import '/@/assets/css/all.css'

import { store } from '/@/store/index.js'
import { router } from '/@/router/index.js'
import { mixins } from '/@/mixins/index.js'

app.use(store)
app.use(router)
mixins.forEach((mixin) => {app.mixin(mixin)})

app.mount('#app')
