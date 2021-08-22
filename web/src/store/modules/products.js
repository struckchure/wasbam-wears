import { getCookie, api, Storage } from '/@/store/utils.js'
import {
    GET_PRODUCTS,
    SET_PRODUCTS,
    CREATE_PRODUCT,
    DELETE_PRODUCT,
    UPDATE_PRODUCT,
    SET_ERROR
} from '/@/store/types.js'


const storage = new Storage();


const state = {
    products: []
}

const getters = {
    get_products (state) {
        return state.products
    }
}

const mutations = {
    [SET_PRODUCTS] (state, payload) {
        state.products = payload
    }
}

const actions = {
    async [GET_PRODUCTS] (context) {
        await api({
            method: 'get',
            url: '/products/list/',
            headers: {
                "Content-Type": "application/json"
            }
        })
        .then(
            function(response) {
                context.commit(SET_PRODUCTS, response.data)
            }
        )
        .catch(
            function(error) {
                context.commit(SET_ERROR, error.response.data)
            }
        )
    },
    async [CREATE_PRODUCT] (context, payload) {
        await api({
            method: 'post',
            url: '/products/create/',
            headers: {
                "Content-Type": "multipart/form-data",
                "X-CSRFToken": getCookie('csrftoken'),
                'Authorization': `Token ${storage.get('token')}`
            },
            data: payload
        })
        .then(
            function(response) {
                context.dispatch(GET_PRODUCTS)
            }
        )
        .catch(
            function(error) {
                context.commit(SET_ERROR, error.response.data)
            }
        )
    },
    async [DELETE_PRODUCT] (context, slug) {
        await api({
            method: 'get',
            url: `/products/${slug}/delete/`,
            headers: {
                "Content-Type": "application/json",
                'Authorization': `Token ${storage.get('token')}`
            },
        })
        .then(
            function(response) {
                console.log(response.data)
            }
        )
        .catch(
            function(error) {
                context.commit(SET_ERROR, error.response.data)
            }
        )
    },
    async [UPDATE_PRODUCT] (context, slug, payload) {
        await api({
            method: 'post',
            url: `/products/${slug}/update/`,
            headers: {
                "Content-Type": "multipart/form-data",
                "X-CSRFToken": getCookie('csrftoken'),
                'Authorization': `Token ${storage.get('token')}`
            },
            data: payload
        })
        .then(
            function(response) {
                context.dispatch(GET_PRODUCTS)
            }
        )
        .catch(
            function(error) {
                context.commit(SET_ERROR, error.response.data)
            }
        )
    }
}

export default {
    state,
    getters,
    mutations,
    actions
}
