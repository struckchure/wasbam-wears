<template>
    <div>
        <router-view></router-view>
        <Modal
            name="app_error_modal"
            header="Message"
            :persistent="true"
        >
            <template v-slot:body>
                <p
                    v-for="(error, index) in get_error"
                    :key="index"
                >{{ error }}</p>
                <div>
                    <button @click="close_modal">Ok</button>
                </div>
            </template>
        </Modal>    
    </div>
</template>

<script type="text/javascript">
    import {
        mapGetters,
        mapMutations,
        mapActions
    } from 'vuex'
    import {
        CLEAR_ERROR,
        AUTH_LOGIN
    } from '/@/store/types.js'
    import {
        open_modal,
        close_modal
    } from '/@/components/modal/modal.js'

    export default {
        name: 'App',
        computed: {
            ...mapGetters({
                _error: 'get_error'
            }),
            get_error () {
                var error = []
                if (this._error && typeof this._error === 'object') {
                    Object.keys(this._error)
                        .forEach(
                            (error_message_key) => {
                                error.push(this._error[error_message_key][0])
                            }
                        )
                } else {
                    error.push(this._error)
                }

                return error
            }
        },
        methods: {
            ...mapMutations({
                _clear_error: CLEAR_ERROR
            }),
            close_modal () {
                close_modal('app_error_modal')

                this._clear_error()
            }
        }
    }
</script>
