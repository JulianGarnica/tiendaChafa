import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import CreateView from '../views/CreateView.vue'
import EditView from '../views/EditView.vue'
import usuariosView from '../views/usuariosView.vue'
import CreateUserView from '../views/CreateUserView.vue'
import EditarUsuario from '../views/EditarUsuario.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/crearFichaMedica',
    name: 'Crear Ficha Médica',
    component: CreateView
  },
  {
    path: '/editarFichaMedica/:id',
    name: 'Editar Ficha Médica',
    component: EditView
  }
  ,
  {
    path: '/usuarios',
    name: 'Usuarios',
    component: usuariosView
  },
  {
    path: '/crearUsuarios',
    name: 'Usuarios',
    component: CreateUserView
  },
  {
    path: '/editarUsuario/:id',
    name: 'Usuarios',
    component: EditarUsuario
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
