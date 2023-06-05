<!-- PostRequirement.vue --> 
<template>
    <form class="form-control " @submit="onSubmit">
      <div class="m-3">
        <h3  class="form-label">Add Requirement</h3>
      </div>
      <div class="m-3">
        <label class="form-label p-2">Requirement description</label>
        <input class="form-control" name="text" type="text" v-model="text">
        <div id="passwordHelpBlock" class="form-text">
          Please enter your requirement here.Below you can add details such who the requirement is assigned to, priority and if it has been completed or not
        </div>
      </div>
      
      <div class="m-3">
        <label class="form-label p-2">Assign to a project member</label>
          <select v-model="assigned_to" class="form-select">
            <option :value="member" v-for="member in memberList">{{ member }}</option>
          </select>
      </div>

      <div class="m-3">
        <label class="form-label p-2">Priority</label>
        <input type="range" min="1" max="5" name="priority" v-model="priority">
      </div>
      <div class="m-3">
        <label class="form-label m-2">Has requirement been completed?</label>
        <input type="checkbox" class="btn btn-primary m-2" v-model="completed" id="completed">
      </div>
      <input type="submit" value="submit" class="btn btn-primary m-3">
    </form>
  </template>
  
<script>
import { postItem, getItem } from '../Api'

export default {
  props: {
    list: Object,
    title: String,
    api_endpoint: String,
    requestBody: Object,
    projectId : Number
  },
  data() {
      return {
        text: '',
        assigned_to: '',
        completed: false,
        priority: 1,
        memberList : []
      }
  },
  methods: {
    async onSubmit(e) {
        e.preventDefault()
        this.requestBody.requirement_description = this.text
        this.requestBody.priority_rating = this.priority
        this.requestBody.completion_status = this.completed
        this.requestBody.assigned_to = this.assigned_to
        this.requestBody.project = localStorage.getItem("ProjectId")
        if (this.requestBody.project==-1){
          alert("Please Select a project")
          return
        }
        if(!this.text || !this.requestBody.assigned_to){
            alert('Please add a requirement and/or assign a project member')
            return
        }

        const data = await postItem(this.requestBody, this.api_endpoint)
        
        this.text = ''
        this.list.push(data)
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
