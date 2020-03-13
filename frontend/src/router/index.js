import Vue from 'vue';
import VueRouter from 'vue-router';


Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    pathToRegexpOptions: { strict: true },
    component: () => import('../views/Home'),
    props: true,
  },
  {
    path: '/worker/',
    name: 'Worker',
    pathToRegexpOptions: { strict: true },
    component: () => import('../views/Worker'),
    props: true,
  },
  {
    path: '/registered/',
    name: 'Registered',
    pathToRegexpOptions: { strict: true },
    component: () => import('../views/Registered'),
    props: true,
  },
  {
    path: '/signin/',
    name: 'SignIn',
    pathToRegexpOptions: { strict: true },
    component: () => import('../views/SignIn'),
    props: true,
  },
  {
    path: '/manager/',
    name: 'Manager',
    pathToRegexpOptions: { strict: true },
    component: () => import('../views/Manager'),
    props: true,
  },

];

const router = new VueRouter({
  routes,
});

export default router;
