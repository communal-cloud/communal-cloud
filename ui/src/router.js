import Vue from 'vue'
import store from './store'
import Router from 'vue-router'
import { sync } from 'vuex-router-sync'

import Home from './views/Home.vue'
import Communities from './views/Communities.vue'
import CreateCommunity from './components/CreateCommunity.vue'
import CreateWorkflow from './components/CreateWorkflow.vue'
import CreateTask from './components/CreateTask.vue'
import DoTask from './components/DoTask.vue'

import SignIn from './components/SignIn.vue'

Vue.use(Router)

const router = createRouter()

sync(store, router)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/user/login',
    name: 'login',
    component: SignIn
  },
  {
    path: '/communities',
    name: 'community',
    component: Communities
  },
  {
    path: '/create',
    name: 'createCommunity',
    component: CreateCommunity
  },
  {
    path: '/createTask',
    name: 'createTask',
    component: CreateTask
  },
  {
    path: '/doTask',
    name: 'doTask',
    component: DoTask
  },
  {
    path: '/createWorkflow',
    name: 'createWorkflow',
    component: CreateWorkflow
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
  }
]

export default router

function createRouter () {
  const router = new Router({
    mode: 'history',
    routes,
    base:'/'
  })

  router.beforeEach(beforeEach)
  router.afterEach(afterEach)

  return router
}

async function beforeEach (to, from, next) {
  if (store.getters.token) {
    try {
      await store.dispatch('fetchUser')
    } catch (e) {
      console.log(e);
    }
  }else{
    console.log("logged out");
  }
  return next();
}

async function afterEach (to, from, next) {
  await router.app.$nextTick()
}