 <!-- ProjectTask.vue -->
 <template>
    <form class="form-control " @submit.prevent="onSubmit" >
      <div class="">
        <label class="form-label p-2">Task description</label>
        <input class="form-control" name="text" type="text" v-model="text">
        <label class="form-label p-2">Completetion status</label>
        <input type="checkbox" class="btn btn-primary m-2" v-model="completion_status" id="completed">
      </div>
      <input type="submit" value="submit" class="btn btn-primary m-3">
    </form>
  </template>
  
  <script>
  import { postItem } from '../Api'
  
  export default {
    props: {
      list: Object,
      api_endpoint: String,
      requestBody: Object,
    },
    data() {
      return {
        text: '',
        completion_status : false,
      }
    },
    methods: {
      async onSubmit() {
        this.requestBody.task_name = this.text
        this.requestBody.is_completed = this.completion_status
        this.requestBody.requirement = localStorage.getItem("requirementId")
        
        const data = await postItem(this.requestBody, this.api_endpoint)
        this.text = ''
        this.list.push(data)
        this.$emit('list-updated', this.list)
      }
    }
  }
  </script>
  