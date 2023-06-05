<!-- RequirementList.vue -->
<template> 
    <div class="">
      <ul class="list-group list-group-numbered " >
        <li class="list-group-item d-flex justify-content-between align-items-start" :class="{'completed' : name.resolution_status}" v-for="name in list">
          <div class="ms-2 me-auto">
            <div class="fw-bold" v-if="!name.editing">{{ name.bug_description }}</div>
            <div class="fw-bold" v-if="!name.editing">{{ name.bug_priority }}</div>
            <div class="fw-bold" v-if="!name.editing">{{ name.resolver }}</div>
              
            <div v-else>
              <form @submit.prevent="updateItem(name)" class="form-control">
                <div class="">
                  <div class="m-3">
                    <h3  class="form-label">Edit Bug Info</h3>
                    <label class="form-label p-2">New Bug Description</label>
                    <input class="form-control" type="text" v-model="name.bug_description">

                    <label class="form-label p-2">Assign to a project member</label>
                    <select v-model="name.resolver" class="form-select">
                      <option :value="member" v-for="member in memberList">{{ member }}</option>
                    </select>

                    <label class="form-label p-2">Assign New Priority</label>
                    <input class="form-control" type="range" min="1" max="5" v-model="name.bug_priority">
                    <label class="form-label p-2">Resolution status</label>
                    <input type="checkbox" class="btn btn-primary m-2" v-model="name.resolution_status" id="completed">
                  </div>
                  <input type="submit" value="submit" class="btn btn-primary m-3">
                </div>
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
      </ul>
    </div>
  </template>
  
  <script>
  import {delItem, getItem, putItem} from '../Api'
  

  export default{    
    data(){
      return {
        memberList : []
      }
    },
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
          this.$emit('item-deleted', id) // emit event with the deleted item's id
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
        if(!name.bug_description){
          this.$emit('displayItems')
          alert('Please add a bug description')
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