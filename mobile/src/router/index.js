import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import Tags from '../views/Tags.vue'
import Profile from '../views/Profile.vue'
import Auth from '../views/Auth.vue'
import EditInfo from '../views/EditInfo.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  }, {
    path: '/login',
    name: 'Login',
    component: Login
  }, {
    path: '/register',
    name: 'Register',
    component: Register
  }, {
    path: '/tags',
    name: 'Tags',
    component: Tags,
    meta: {
      requireAuth: true
    }
  }, {
    path: '/profile',
    name: 'Profile',
    component: Profile,
    meta: {
      requireAuth: true
    }
  }, {
    path: '/auth',
    name: 'Auth',
    component: Auth,
    meta: {
      requireAuth: true
    }
  }, {
    path: '/editInfo',
    name: 'EditInfo',
    component: EditInfo,
    meta: {
      requireAuth: true
    }
  }
]

const router = new VueRouter({
  // mode: 'history',
  // base: process.env.BASE_URL,
  routes
})


router.beforeEach((to, from, next) => {
  if (to.matched.some((r) => r.meta.requireAuth)) {
    let isLogin = JSON.parse(localStorage.getItem('isLogin'));
    if (isLogin) {   //判断是否已经登录
      next();
    } else {
      next({
        path: '/login',
        // query: { redirect: to.fullPath }   //登录成功后重定向到当前页面
      });
    }
  } else {
    next();
  }
  //如果本地 存在 token 则 不允许直接跳转到 登录页面
  if (to.fullPath === "/login") {
    if (JSON.parse(localStorage.getItem('isLogin'))) {
      next({
        path: from.fullPath
      });
    } else {
      next();
    }
  }
});

export default router