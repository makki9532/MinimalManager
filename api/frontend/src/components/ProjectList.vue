  <!-- ProjectList.vue -->
  <template> 
    <div class="">
      <ol class="list-group list-group-numbered " >
        <li class="list-group-item d-flex justify-content-between align-items-start"   v-for="name in list" :class="{'selected' : selected===name.id}">
          <div class="ms-2 me-auto">
            <div class="fw-bold" v-if="!name.editing">{{ name.project_name }}</div>
              
            <div v-else>
              <form @submit.prevent="updateItem(name)">
                <div class="m-3">
                  <p  class="form-label">New Project Name</p>
                  <input class="form-control" name="text" type="text" v-model="name.project_name">
                </div>
                
                <input type="submit" value="submit" class="btn btn-primary m-3"> 
              </form>
            </div>
          
  
            <span class="m-1">
              <button v-if="!name.editing" class="btn btn-warning" @click="editItem(name)"> Edit</button>
              <button v-else class="btn btn-success" @click="cancelEditItem(name)">Cancel</button>
            </span>
            
            <span class="m-1">
              <button @click="del(name.id)" class="btn btn-danger">Del</button>
            </span>

            <span class="m-1">
              <button @click="loadProject(name)" class="btn btn-primary">Select</button>
            </span>
            
          </div>
        </li>
      </ol>
    </div>
  </template>
  
  <script>
  import {delItem, putItem} from '../Api'

  export default{    
    props: {
      list: Object,
      api_endpoint: String,
      requestBody: Object,
      selected : Number
    },
    data() {
      return {
        project_name : "",
        user : [],
      }
    },
    methods: {
      async del(id){
        const confirmed = confirm("Are you sure you want to delete the project? Please remember to select a new project if answered yes.");
        if (!confirmed) {
          return;
        }
        const res = await delItem(id, this.api_endpoint)
        if (res.ok) {
          this.$emit('item-deleted', id)
        }
      },
      editItem(item) {
        item.editing = true
      },
      cancelEditItem(name){
        name.editing = false
        this.$emit('displayItems')
      },
      //separate into different componenet
      async updateItem(name){
        const id = name.id
        if (!name.project_name.trim()) {
          this.$emit('displayItems')
          alert("cannot submit empty form")
          return;
        }
        const projectName = name.project_name.trim()
        if (projectName.length > 50) {
            alert("Project name cannot exceed 50 characters.")
            return;
        }
        this.requestBody.project_name = name.project_name
        this.requestBody.user = name.user
        
        const res = await putItem(id, this.requestBody, this.api_endpoint)
        const index = this.list.findIndex(item => item.id === id)
        if (index >= 0) {
           this.list[index].project_name = this.requestBody.project_name
          }
        name.editing = false
        this.$emit('list-updated', this.list)    
        },
        //separate into different componenet
        loadProject(name){
          localStorage.setItem('ProjectId', name.id)
          this.$emit('viewProject', name.id)
          this.$emit('displayItems')
        }
      } 
  }
  </script>
  
  <style scoped>
      .list-group-item:hover {
        background-color: rgba(189, 218, 250, 0.2);
      }
      .selected {
        background-color: rgba(0, 123, 255, 0.2);
      }
  </style>