import Vue from 'vue'
import store from './store'
import Router from 'vue-router'

import Home from './views/Home.vue'
import Communities from './views/Communities.vue'
import CreateCommunity from './components/CreateCommunity.vue'
import CreateWorkflow from './components/CreateWorkflow.vue'
import CreateTask from './components/CreateTask.vue'
import DoTask from './components/DoTask.vue'

import SignIn from './components/SignIn.vue'
import SignUp from './components/SignUp.vue'

Vue.use(Router)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/user/login',
    name: 'login',
    component: SignIn
  },  {
    path: '/user/register',
    name: 'register',
    component: SignUp
  },
  {
    path: '/communities',
    name: 'community',
    component: Communities,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/create',
    name: 'createCommunity',
    component: CreateCommunity,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/createTask',
    name: 'createTask',
    component: CreateTask,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/doTask',
    name: 'doTask',
    component: DoTask,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/createWorkflow',
    name: 'createWorkflow',
    component: CreateWorkflow,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ './views/About.vue'),
    meta: {
      requiresAuth: true
    }
  }
]

export default  new Router({
  mode: 'history',
  routes,
  base:'/',
  beforeEach,
  afterEach
})


async function beforeEach (to, from, next) {
  /*if (store.getters.token) {
    try {
      await store.dispatch('fetchUser')
    } catch (e) {
      console.log(e);
    }
  }else{
    console.log("logged out");
  }
  return next();*/
  if (to.matched.some(record => record.meta.requiresAuth) && !store.getters.check)
    this.$router.push('login')

  return next()
}

async function afterEach (to, from, next) {
  await router.app.$nextTick()
}