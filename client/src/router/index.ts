import { createRouter, createWebHistory } from 'vue-router'

import Home from "@/components/Home.vue"
import Dataframe from "@/components/Dataframe.vue"
import Health from '@/components/Health.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/dataframe',
      name: 'dataframe',
      component: Dataframe
    },
    {
      path: '/health',
      name: 'health',
      component: Health
    },
  ]
})

export default router
