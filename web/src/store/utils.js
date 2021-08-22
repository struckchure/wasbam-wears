import axios from 'axios'

// axios settings

const DEBUG_MODE = process.env.NODE_ENV
const DEVELOPMENT_URL = "http://localhost:8000"
const PRODUCTION_URL = "http://172.104.229.18/"

let API_URL;

switch(DEBUG_MODE) {
    case 'development':
        API_URL = DEVELOPMENT_URL
        break;
    case 'production':
        API_URL = PRODUCTION_URL
        break;
}

axios.defaults.baseURL = API_URL;
axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.responseEncoding = 'utf8'

export const api = axios.create({});

export function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

export class Storage {

    set(key, value) {
        localStorage.setItem(key, value)
    }

    get(key) {
        return localStorage.getItem(key)
    }

    remove(key) {
        localStorage.removeItem(key)
    }
}
