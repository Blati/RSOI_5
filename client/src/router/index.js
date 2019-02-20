import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Users from '@/components/Users'
import User from '@/components/User'
import Bookings from '@/components/Bookings'
import Adding from '@/components/Adding'
import Login from '@/components/Login'
import Register from '@/components/Register'
import Profile from '@/components/Profile'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/users',
      name: 'Users',
      component: Users
    },
    {
      path: '/users/:id',
      name: 'User Info',
      component: User
    },
    {
      path: '/users/:id/bookings',
      name: 'Bookings',
      component: Bookings
    },
    {
      path: '/users/:id/bookings/add/:date',
      name: 'Adding',
      component: Adding
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/profile',
      name: 'Profile',
      component: Profile
    }
  ]
})
