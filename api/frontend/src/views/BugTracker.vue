BugTracker.vue


<template>
  
  <div class="d-flex justify-content-between align-items-center mb-3 mt-3">
      <button @click="showPostForm" class="btn btn-success">Show Form</button>
      <button @click="hidePostForm" class="btn btn-dark">Hide Form</button>
    </div>

  <PostBug
  v-if="toggler"
  :list="list"
  :title="title"
  :api_endpoint="api_endpoint"
  :projectId = "requestBody.project"
  :requestBody = "requestBody"
  >
  </PostBug>

  <div class="d-flex justify-content-between align-items-center mb-3 mt-3">
      <button @click="filterCompleted(true)" class="btn btn-success">Completed</button>
      <button @click="filterByPriorityAsc" class="btn btn-info">Priority Ascend</button>
      <button @click="filterCompleted(false)" class="btn btn-light">Not Completed</button>
      <button @click="filterByPriorityDesc" class="btn btn-info">Priority Descend</button>
      <button @click="displayItems" class="btn btn-dark">Get All</button>
    </div>
  <BugList 
    :list="list"
    :api_endpoint="api_endpoint"
    :requestBody = "requestBody"
    :projectId = "requestBody.project"
    @item-deleted="deleteItemFromList"
    @displayItems="displayItems"
  >
  </BugList>
</template>

<script>
import BugList from '../components/BugList.vue'
import PostBug from '../components//PostBug.vue';
import {getItem} from '../Api'
export default{
  props: ['projectId', 'projectIdForAddMember'],
  emits : ['updateList'],
  async mount() {
    await this.displayItems()
  },
  data() {
      return {
          list: [],
          api_endpoint : "bugs",
          title : "Add A Bug",
          requestBody : {
            bug_description : "",
            bug_priority : 1,
            resolution_status : true,
            resolver : "",
            project : this.projectId
          },
          toggler : true,
      };
  },
  methods: {
      async displayItems(){
          const project_id = localStorage.getItem("ProjectId")
          const api_endpoint = `getBugsForProject/${project_id}`
          const items = await getItem(api_endpoint)
          this.list = items
      },
      async deleteItemFromList(id) { 
        this.list = this.list.filter(item => item.id !== id)
      },
      showPostForm(){
          this.toggler = true
      },
      hidePostForm(){
          this.toggler = false
      },
      filterCompleted(isCompleted) {
      this.list = this.list.filter(
        (item) => item.resolution_status === isCompleted
      );
    },
    filterByPriorityAsc() {
      this.list = this.list.sort((a, b) =>
        a.bug_priority > b.bug_priority ? 1 : -1
      );
    },
    filterByPriorityDesc() {
      this.list = this.list.sort((a, b) =>
        a.bug_priority < b.bug_priority ? 1 : -1
      );
    },
  },
  async created() {
    await this.displayItems()
  },
  watch: {
    projectId(newVal) {
    
      this.requestBody.project = newVal;
      this.displayItems();
    }
  },
  components: { BugList, PostBug }
}
</script>

<style scoped>
  .bug-tracker {
  background-image: url('../assets/bug-svgrepo-com.svg');
  background-size: contain; 
  background-repeat: no-repeat; 
}
</style>
