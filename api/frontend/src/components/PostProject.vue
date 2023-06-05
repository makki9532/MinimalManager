 <!-- ProjectList.vue -->
<template>
  <form class="form-control " @submit.prevent="onSubmit">
    <div class="m-3">
      <h3 class="form-label">{{ title }}</h3>
    </div>
    <div class="">
      <div class="m-3">
        <h3 class="form-label">Project Name</h3>
        <input class="form-control" name="text" type="text" v-model="text">
      </div>
      <input type="submit" value="submit" class="btn btn-primary m-3">
    </div>
  </form>
</template>

<script>
import { onErrorCaptured } from 'vue';
import { postItem } from '../Api'

export default {
  props: {
    list: Object,
    title: String,
    api_endpoint: String,
    requestBody: Object,
  },
  data() {
    return {
      text: ''
    }
  },
  methods: {
    async onSubmit() {
      const project_id = localStorage.getItem("ProjectId")
      if (!this.text.trim()) {
          this.$emit('displayItems')
          alert("cannot submit empty form")
          return;
      }
      
      const projectName = this.text.trim()
      if (projectName.length > 50) {
          alert("Project name cannot exceed 50 characters.")
          return;
      }

      this.requestBody.project_name = projectName
      this.requestBody.user = [localStorage.getItem("id")]
      
      const data = await postItem(this.requestBody, this.api_endpoint)
      this.text = ''
      this.list.push(data)
      this.$emit('list-updated', this.list)
    }
  }
}
</script>
