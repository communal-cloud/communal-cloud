import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import Cookies from 'js-cookie'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: null,
    token: Cookies.get('token'),
    loading : false
  },
  getters: {
    user: state => state.user,
    token: state => state.token,
    check: state => state.user !== null,
    loading: state => state.loading
  },
  mutations: {
    save_token (state, { token, remember }) {
      state.token = token;
      Cookies.set('token', token, { expires: remember ? 365 : null })
    },

    fetch_user_success (state, { user }) {
      state.user = user
    },

    fetch_user_failure (state) {
      state.token = null
      Cookies.remove('token')

    },

    logout (state) {
      state.user = null
      state.token = null

      Cookies.remove('token')
    },

    update_user (state, { user }) {
      state.user = user
    },
    
    loading (state, new_state) {
      state.loading = new_state;
    }
  },
  actions: {
    saveToken ({ commit, dispatch }, payload) {
      commit("save_token", payload)
    },

    async fetchUser ({ commit }) {
      try {
        const { data } = await axios.get(process.env.VUE_APP_BASE_URL+'user/', {
          headers: {
            Authorization: 'token ' + this.state.token
          }
        })

        commit("fetch_user_success", { user: data })
      } catch (e) {
        commit("fetch_user_failure")
      }
    },

    updateUser ({ commit }, payload) {
      commit("update_user", payload)
    },

    async logout ({ commit }) {
      try {
        await axios.get(process.env.VUE_APP_BASE_URL+'user/logout/', {
          headers: {
            Authorization: 'token ' + this.state.token
          }
        })
      } catch (e) { }

      commit("logout")
    }
  }
})
