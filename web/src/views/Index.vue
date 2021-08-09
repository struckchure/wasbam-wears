<template>
    <div class="w-full h-screen border-0 border-t-8 border-solid border-blue-800">
    	<div class="mx-auto container h-full">
            <div class="flex flex-col items-center justify-center h-full">
                <div class="text-center">
                    <p class="text-4xl color-text-secondary">Overal X</p>
                    <label>Hospital Management System</label>
                    <div class="divider"></div>

                    <div class="grid grid-rows-2 gap-1">
                        <div class="grid grid-cols-2 gap-1 m-0">
                            <router-link :to="{ name: 'Login' }">
                                <button>Login</button>
                            </router-link>

                            <router-link :to="{ name: 'Register' }">
                                <button>Register</button>
                            </router-link>
                        </div>

                        <div class="grid grid-cols-1 gap-1 m-0">
                            <router-link class="no-underline" :to="{ name: 'Dashboard' }">
                                <button class="flex flex-row items-center justify-center p-0 px-2">
                                    <p>Go to dashboard</p>
                                    <i class="fas fa-arrow-right"></i>
                                </button>
                            </router-link>
                        </div>
                    </div>
                </div>

                <div class="flex">
                    <label class="text-gray-400">(c) Copyright {{ date }} | Overal X</label>
                </div>
            </div>
        </div>
    </div>
</template>

<script type="text/javascript">
    export default {
        name: 'Index',
        computed: {
            date () {
                const current_date = new Date()
                return current_date.getFullYear()
            }
        }
    }
</script>
