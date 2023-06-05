<!-- RequirementList.vue --> 
<template> 

  <div class="">
    <!-- Entire List -->
    <ol class="list-group list-group-numbered " >
      <!-- Each list item -->
      <li class="list-group-item d-flex justify-content-between align-items-start" :class="{'completed' : name.completion_status}" v-for="name in list">
        <div class="ms-2 me-auto">
          <!-- Each item in one list -->
          <div class="fw-bold" v-if="!name.editing">{{ name.requirement_description }}</div>
          <div class="fw-bold" v-if="!name.editing">{{ name.priority_rating }}</div>
          <div class="fw-bold" v-if="!name.editing">{{ name.assigned_to }}</div>
          <!-- Form to edit -->
          <div v-else>
            <form @submit.prevent="updateItem(name)" class="form-control">
              <div class="">
                <div class="m-3">
                  <p  class="form-label">New Requirement description</p>
                  <input class="form-control" type="text" v-model="name.requirement_description">
                  <br>

                  <label class="form-label p-2">Assign to a project member</label>
                  <select v-model="name.assigned_to" class="form-select">
                    <option :value="member" v-for="member in memberList">{{ member }}</option>
                  </select>
                  <br>
                  <p  class="form-label">Set Priority</p>

                  <input class="form-control" type="range" min="1" max="5" v-model="name.priority_rating">
                  <br>

                  <p  class="form-label">Completion status</p>
                  <input type="checkbox" class="btn btn-primary m-2" v-model="name.completion_status" id="completed">
                </div>
                <input type="submit" value="submit" class="btn btn-primary m-3">
              </div>
            </form>

          </div>
          <!-- Edit button that loads the form and del button that deletes it -->
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
import {delItem, getItem, putItem} from '../Api'

export default{    

  props: {
    list: Object,
    api_endpoint: String,
    requestBody: Object,
    projectId : Number

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
      this.$emit('displayItems')
      name.editing = false
    },
    async updateItem(name){
      if(!name.requirement_description){
        this.$emit('displayItems')
        alert('Please add a requirement')
        return
      }
      const id = name.id
      for (const key in this.requestBody){
        this.requestBody[key] = name[key]
      }
      const res = await putItem(id, this.requestBody, this.api_endpoint)
      name.editing = false
      this.$emit('list-updated', this.list)    
      },
      async displayItems(){
        const project_id = localStorage.getItem('ProjectId')
        const data = await getItem(`getUsersForProject/${project_id}`)
        this.memberList = data.members
      },
  },
  async created(){
    await this.displayItems()
  },
  watch: {
      projectId(newVal) {
        
        this.requestBody.project = newVal;
        this.displayItems();
      }
    }
}
</script>

<style scoped>
.completed {
  background-color: rgba(144, 238, 144, 0.5);
}
</style>