import Vue from 'vue'
import store from './store'
import Router from 'vue-router'

import Home from './views/Home.vue'
import Communities from './views/Communities.vue'
import Workflows from './views/Workflows.vue'
import Tasks from './views/Tasks.vue'

import CreateCommunity from './components/CreateCommunity.vue'
import CreateWorkflow from './components/CreateWorkflow.vue'
import CreateTask from './components/CreateTask.vue'
import ExecuteTask from './components/ExecuteTask.vue'

import SignIn from './components/auth/SignIn.vue'
import SignUp from './components/auth/SignUp.vue'
import Activation from './components/auth/Activation.vue'
import Forgot from './components/auth/Forgot.vue'
import CommunityDetails from './views/CommunityDetails'
import MyCommunities from './views/MyCommunities'
import SearchCommunities from './views/SearchCommunities'

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
    },
    {
        path: '/user/register',
        name: 'register',
        component: SignUp
    },
    {
        path: '/user/forgot',
        name: 'forgot',
        component: Forgot
    },
    {
        path: '/user/activation/:token',
        name: 'activation',
        component: Activation
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
        path: '/communities/my',
        name: 'mycommunities',
        component: MyCommunities,
        meta: {
            requiresAuth: true
        }
    },
    {
        path: '/search/communities/',
        name: 'searchcommunities',
        component: SearchCommunities,
        meta: {
            requiresAuth: true
        }
    },
    {
        path: '/search/communities/:keyword',
        name: 'searchcommunities',
        component: SearchCommunities,
        meta: {
            requiresAuth: true
        }
    },
    {
        path: '/community/create',
        name: 'createCommunity',
        component: CreateCommunity,
        meta: {
            requiresAuth: true
        }
    },
    {
        path: '/community/:community_id',
        name: 'communityDetails',
        component: CommunityDetails,
        meta: {
            requiresAuth: true
        }
    },
    {
        path: '/community/:community_id/workflows',
        name: 'workflows',
        component: Workflows,
        meta: {
            requiresAuth: true
        }
    },
    {
        path: '/community/:community_id/workflow/create',
        name: 'createWorkflow',
        component: CreateWorkflow,
        meta: {
            requiresAuth: true
        }
    },
    {
        path: '/community/:community_id/workflow/:workflow_id/tasks',
        name: 'tasks',
        component: Tasks,
        meta: {
            requiresAuth: true
        }
    },
    {
        path: '/community/:community_id/workflow/:workflow_id/task/create',
        name: 'createTask',
        component: CreateTask,
        meta: {
            requiresAuth: true
        }
    },
    {
        path: '/execute',
        name: 'Execute',
        component: ExecuteTask,
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

const router = new Router({
    mode: 'history',
    routes,
    base: '/'
})

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresAuth) && !store.getters.check) {
        if (store.getters.token) {
            try {
                store.dispatch('fetchUser')

                return next()
            } catch (e) {
                console.log(e)
            }
        }

        return next('/user/login')
    }

    return next()
})

/*router.afterEach ((to, from) => {
  return router.app.$nextTick()
})*/

export default router
