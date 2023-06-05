<!-- App.vue -->
<template>
  <div v-if="!status">
    <Login 
    @loginStatus="loginStatus"/>
  </div>
  <div class="sidebar-layout" v-else>
    <div class="sidebar" >
      <Projects
      @viewProject="viewProject"
      />
    </div>
    <div class="content" >
      <!-- Main content goes here -->
        <div class="container">
          <navbar 
          @loginStatus ="loginStatus"
          />
          <div class="">
            <router-view 
          :projectId="projectId"
          :projectIdForAddMember = "projectIdForAddMember"
          ></router-view>
          </div>
        </div>
    </div>
  </div>
</template>

<script>
import Navbar from "./components/Navbar.vue";
import Projects from "./components/Projects.vue";
import Login from "./components/Login.vue";

export default {
  mounted() {
    this.loginStatus()
  },
  data() {
    return {
      userId : localStorage.getItem("id"),
      projectId : -1,
      projectIdForAddMember : -1,
      status : false,
    }
  },
  components: {
    Navbar, Projects, Login
  },
  methods: {
    viewProject(id){
      this.projectId = id
      this.projectIdForAddMember = id
    },
    loginStatus() { 
      const login_status = localStorage.getItem("login_status")
      if (login_status ==="false"){
        this.status = false
        return
      }
      this.status = true
    },
  }
};
</script>

<style scoped>
.sidebar-layout {
  display: flex;
  height: 100%;
}

.sidebar {
  width: 350px;
  background-color: #f4f4f4;
  padding: 1rem;
}

.content {
  flex-grow: 1;
  padding: 1rem;
}

</style>