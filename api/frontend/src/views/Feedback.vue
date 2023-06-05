<template> 
    <div class="m-3">
      <form v-if="showForm" class="form-control" @submit.prevent="onSubmit">
          <div class="m-3">
            <label class="form-label p-2">Add Feedback</label>    
            <textarea class="form-control" name="feedback" id="text" v-model="text" cols="30" rows="10"></textarea>
          </div>
          <input type="submit" value="submit" class="btn btn-primary m-3">
      </form>
      <div class="accordion" id="accordionExample" v-for="(name, index) in list" :key="index">
        <div class="accordion-item">
          <h2 class="accordion-header" :id="'req-heading'+index">
            <button class="accordion-button" type="button" data-bs-toggle="collapse" 
              :data-bs-target="'#req-collapse'+index" @click="selected = selected === index ? null : index"
              :aria-expanded="selected === index" :aria-controls="'req-collapse'+index" @click.stop="displayItems(name.id)">
              {{ name.date_reviewed }}
            </button>
          </h2>
          <div :id="'req-collapse'+index" class="accordion-collapse collapse" :class="{ show: selected === index }" 
            :aria-labelledby="'req-heading'+index" data-bs-parent="#accordionExample">
            
            
            
            <div class="accordion-body" v-if="!name.editing">
                {{ name.text }}
            </div>
            

            <div v-else>
              <form @submit.prevent="updateItem(name)">
                <div class="m-3">
                  <p  class="form-label">Change Feedback</p>
                  <input class="form-control" name="text" type="text" v-model="name.text">
                </div>
                
                <input type="submit" value="submit" class="btn btn-primary m-3"> 
              </form>
            </div>

            <span class="m-3" v-if="showForm">
              <button v-if="!name.editing" class="btn btn-warning" @click="editItem(name)"> Edit</button>
              <button v-else class="btn btn-success" @click="cancelEditItem(name)">Cancel</button>
            </span>
            
            <span class="m-1" v-if="showForm">
              <button @click="deleteItemFromList(name.id)" class="btn btn-danger">Del</button>
            </span>

          </div>
        </div>
      </div>
    </div>
  </template>
  
    
  
  <script>
  import {getItem, delItem, postItem, putItem} from '../Api'
  
  export default{
    props: ['projectId','projectIdForAddMember'],
    data() {
        return {
            list : [],
            api_endpoint : "feedback",
            requestBody : {
              date_reviewed : "",
              text : "",
              project : this.projectId,
            },
            text: '',
            showForm : false
        };
    },
    methods: {
        async displayItems(){
            const project_id = localStorage.getItem("ProjectId")
            const items = await getItem(this.api_endpoint)
            this.list = items.filter(item => item.project==Number(project_id))
            this.list.forEach(item => item.date_reviewed =  this.formatDatetime(item.date_reviewed))
            if(localStorage.getItem('account_type') === 'E'){
              this.showForm = true
            } 
        },
        async updateList(newlist){
          this.list = newlist
          await this.displayItems()
        },
        async deleteItemFromList(id) { 
            await delItem(id, this.api_endpoint)
            this.list = this.list.filter(item => item.id !== id)
        },
        editItem(item) {
        item.editing = true
      },
      cancelEditItem(name){
        name.editing = false
      },
      async onSubmit() {
        if (!this.text){
          alert("Cannot leave text blank")
          return    
        }
        if(this.text.length>10000){
          alert("Cannot enter more than 10000 characters")
          return
        }
        this.requestBody.date_reviewed = new Date().toISOString()
        this.requestBody.text = this.text
        this.requestBody.project = localStorage.getItem("ProjectId")
        console.log(this.requestBody)
        const data = await postItem(this.requestBody, this.api_endpoint)
        this.text = ''
        this.list.push(data)
      },
      async updateItem(name){
        const id = name.id
        this.requestBody.date_reviewed = name.date_reviewed
        this.requestBody.text = name.text
        this.requestBody.project = name.project
        
        const res = await putItem(id, this.requestBody, this.api_endpoint)
        const index = this.list.findIndex(item => item.id === id)
        if (index >= 0) {
           this.list[index].text = this.requestBody.text
          }
        name.editing = false   
      },
      formatDatetime(datetimeString) {
        const date = new Date(datetimeString);
        const day = String(date.getDate()).padStart(2, '0');
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const year = date.getFullYear();
        const hours = String(date.getHours()).padStart(2, '0');
        const minutes = String(date.getMinutes()).padStart(2, '0');
        const seconds = String(date.getSeconds()).padStart(2, '0');

        return `${day}/${month}/${year} ${hours}:${minutes}:${seconds}`;  
      }

    },
    async created() {
      await this.displayItems()
    },
    async mounted() {
      await this.displayItems()  
    },
    watch: {
      projectId(newVal) {
        this.requestBody.project = newVal;
        this.displayItems();
      }
    },
  }
  </script>
  
