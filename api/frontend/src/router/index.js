//router/index.js
import {createRouter, createWebHistory} from 'vue-router'
import Home from '../views/Home.vue'
import Requirements from '../views/Requirements.vue'
import Members from '../views/Members.vue'
import BugTracker from '../views/BugTracker.vue'
import TaskPlanner from '../views/TaskPlanner.vue'
import Feedback from '../views/Feedback.vue'





const routes = [
    {path: '/', name: 'Home', component: Home},
    {path: '/requirements', name: 'Requirements', component: Requirements},
    {path: '/members', name: 'Members', component: Members},
    {path: '/bugs', name: 'BugTracker', component: BugTracker},
    {path: '/taskplanner', name: 'TaskPlanner', component: TaskPlanner},
    {path: '/feedback', name: 'Feedback', component: Feedback},
]

const router = createRouter({
    history: createWebHistory(),
    routes
})
 


export default router