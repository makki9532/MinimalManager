<template>
  <PostProject
  :list="list"
  :title="title"
  :api_endpoint="api_endpoint"
  :requestBody = "requestBody"
  @list-updated="updateList"
  >
  </PostProject>
  <ProjectList 
  class="mt-3"
    :list="list"
    :api_endpoint="api_endpoint"
    :requestBody = "requestBody"
    :showEdit = "showEdit"
    :selected = "selected"
    @list-updated="updateList"
    @item-deleted="deleteItemFromList"
    @projectId = "projectId"
    @viewProject = "viewProject"
    @displayItems = "displayItems"
  >
  </ProjectList>
</template>

<script>
import ProjectList from './ProjectList.vue'
import PostProject from './PostProject.vue';
import {getItem} from '../Api'
export default{
  emits: ['viewProject','list-updated', 'viewProject', 'display'],
  props : {
    projectId : Number,
  },
  data() {
      return {
          list: {},
          api_endpoint : "project",
          title : "Add a project",
          requestBody : {
              project_name : "",
              user : [],
          },
          toggler : true,
          selected : -1
      };
  },
  methods: {
      async displayItems(){
        const user_id = localStorage.getItem("id") 
        const api_endpoint = `getProjectForUser/${user_id}`
        const items = await getItem(api_endpoint)
        this.list = items
        this.selected = Number(localStorage.getItem("ProjectId")) 
      },
      async deleteItemFromList(id) { 
        this.list = this.list.filter(item => item.id !== id)
        this.$emit('viewProject', -1)

      },
      showPostForm(){
          this.toggler = true
      },
      hidePostForm(){
          this.toggler = false
      },
      viewProject(id){
        this.$emit('viewProject', id)
      },
      async updateList(newlist){
        this.list = newlist
        await this.displayItems()
      } 
  },
  async created() {
      await this.displayItems()
  },
  watch: {
    userId(newVal) {
      this.requestBody.user = newVal;
      this.displayItems();
    },
  },
  components: { ProjectList, PostProject }
}
</script>

