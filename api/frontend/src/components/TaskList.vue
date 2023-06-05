  <!-- TaskList.vue -->
  <template> 
    <div class="">
      <ol class="list-group list-group-numbered " >
        <li class="list-group-item d-flex justify-content-between align-items-start"   v-for="name in list" :class="{'completed' : name.is_completed}">
          <div class="ms-2 me-auto">
            <div class="fw-bold" v-if="!name.editing">{{ name.task_name }}</div>
              
            <div v-else>
              <form @submit.prevent="updateItem(name)">
                <div class="m-3">
                  <label class="form-label p-2">New Task Name</label>
                  <input class="form-control" name="text" type="text" v-model="name.task_name">
                  <label class="form-label p-2">Change completion status</label>
                  <input type="checkbox" class="btn btn-primary m-2" v-model="name.is_completed" id="completed">
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
      requestBody: Object
    },
    data() {
      return {
        project_name : "",
      }
    },
    methods: {
      async del(id){
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
      },
      //separate into different componenet
      async updateItem(name){
        const id = name.id
        this.requestBody.task_name = name.task_name
        this.requestBody.is_completed = name.is_completed
        this.requestBody.requirement = localStorage.getItem("requirementId")
        
        const res = await putItem(id, this.requestBody, this.api_endpoint)
        const index = this.list.findIndex(item => item.id === id)
        if (index >= 0) {
           this.list[index].task_name = this.requestBody.task_name
          }
        name.editing = false
        this.$emit('list-updated', this.list)    
        },
      } 
  }
  </script>
  
 
 <style scoped>
 .completed {
   background-color: rgba(144, 238, 144, 0.5);
 }
 </style>