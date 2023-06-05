<template>
  <nav class="navbar navbar-expand-lg bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Minimal Manager</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'Home'}">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'Requirements'}">Requirements</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'Members'}">Members</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'BugTracker'}">BugTracker</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'TaskPlanner'}">TaskPlanner</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'Feedback'}">Feedback</router-link>
          </li>
        </ul>
        <div class="d-flex">
          <button class="btn btn-light" @click="logout">Logout</button>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
 import { getItem } from '../Api'
 export default {
    methods: {
      async logout() {
        const token = localStorage.getItem("token")
        const id = localStorage.getItem("id")
        
        const user_id = {
          "id" : id
        }
        
        const res = await getItem('logout')
        
        localStorage.removeItem("token")
        localStorage.removeItem("id")
        localStorage.setItem("login_status", false)
        this.$emit('loginStatus')
        location.reload();
      }
    }
  }
</script>
