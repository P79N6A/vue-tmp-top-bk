import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/home'
import Examination from '@/pages/bk_examination/examination'
Vue.use(Router);

let router = new Router({
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        }, {
            path: '/examination',
            name: 'examination',
            component: Examination
        },
    ]
});

router.beforeEach((to, from, next) => {
    if (to.matched.length === 0) {
        from.name ? next({name: from.name}) : next('/');
    } else {
        next();
    }
});
export default router
