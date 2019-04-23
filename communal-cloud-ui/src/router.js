import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Communities from './views/Communities.vue'
import CreateCommunity from './components/CreateCommunity.vue'
import CreateWorkflow from './components/CreateWorkflow.vue'
import CreateTask from './components/CreateTask.vue'
import DoTask from './components/DoTask.vue'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
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
})
