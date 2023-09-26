import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

const router = createRouter({
	history: createWebHistory(),
	routes: [
		{
			path: '/',
			component: Home
		},
		{
			path: '/about',
			component: () => import('../views/About.vue')
		},
		{
			path: '/deposits',
			component: () => import('../views/Deposits.vue')
		},
		{
			path: '/withdrawals',
			component: () => import('../views/Withdrawals.vue')
		},
		{
			path: '/holdings',
			component: () => import('../views/Holdings.vue')
		}
	],
})

export default router