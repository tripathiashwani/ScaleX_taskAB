

<template>
  <nav class="py-10 px-8 border-b border-gray-200">
    <div class="max-w-7xl mx-auto">
        <div class="flex items-center justify-between">
            <div class="menu-left">
                <a href="#" class="text-xl">Wey</a>
            </div>
            <div v-if="userStore.user.isAuthenticated"></div>
            <div class="menu-center flex space-x-12"
             v-else>
                <RouterLink to="/" href="#" class="text-purple-700">
                    <!-- <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
                    </svg>                               -->
                </RouterLink>

            </div>

            <div class="menu-right">
                    <template v-if="userStore.user.isAuthenticated">
                        <!-- <RouterLink :to="{name: 'profile', params:{'id': userStore.user.id}}">
                            <img src="https://i.pravatar.cc/40?img=70" class="rounded-full">
                        </RouterLink> -->
                    </template>

                    <template v-else>
                        <RouterLink to="/login" class="mr-4 py-4 px-6 bg-gray-600 text-white rounded-lg">Log in</RouterLink>
                        <RouterLink to="/signup" class="py-4 px-6 bg-purple-600 text-white rounded-lg">Sign up</RouterLink>
                    </template>
            </div>
        </div>
    </div>
</nav>
<main px-8 py-6 bg-gray-100>
  
<RouterView />
</main>
  <Toast/>
</template>

<script>
    import axios from 'axios'
    import Toast from '@/components/Toast.vue'
    import { useUserStore } from '@/stores/user'
import { RouterLink } from 'vue-router'
    export default {
        setup() {
            const userStore = useUserStore()

            return {
                userStore
            }
        },

        components: {
            Toast
           
        },

        beforeCreate() {
            this.userStore.initStore()
            const token = this.userStore.user.access

            if (token) {
                axios.defaults.headers.common["Authorization"] = "Bearer " + token;
            } else {
                axios.defaults.headers.common["Authorization"] = "";
            }
        }
    }
</script>