import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import signupView from '../views/signupView.vue'
import loginView from '../views/loginView.vue'
import feedView from '../views/feedView.vue'
const guard = function(to, from, next) {
  if(localStorage.getItem('user.access')){
    next()
  }else{
    next('/login')
  }
}

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      beforeEnter: (to, from, next) => {
        guard(to, from, next)
      }
    },
    {
      path: '/signup',
      name: 'signup',
      component: signupView
    },
    {
      path: '/login',
      name: 'login',
      component: loginView
    },
    {
      path: '/feed',
      name: 'feed',
      component: feedView,
      beforeEnter: (to, from, next) => {
        guard(to, from, next)
      }
    },

  ]
})

export default router