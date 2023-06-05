<template> 
  <div class="m-3">
    <h3>Requirements</h3>
    <div class="accordion" id="accordionExample" v-for="(name, index) in requirementList" :key="index">
      <div class="accordion-item">
        <h2 class="accordion-header" :id="'req-heading'+index">
          <button class="accordion-button" type="button" data-bs-toggle="collapse" 
            :data-bs-target="'#req-collapse'+index" @click="selected = selected === index ? null : index"
            :aria-expanded="selected === index" :aria-controls="'req-collapse'+index" @click.stop="displayTasks(name.id)">
            {{ name.requirement_description }}
          </button>
        </h2>
        <div :id="'req-collapse'+index" class="accordion-collapse collapse" :class="{ show: selected === index }" 
          :aria-labelledby="'req-heading'+index" data-bs-parent="#accordionExample">
          <div class="accordion-body">
            <h4>Tasks</h4>
            <PostTask
            :list="list"
            :api_endpoint="api_endpoint"
            :requestBody = "requestBody"
            @list-updated="updateList"
            >
            </PostTask>
            <TaskList 
              :list="list"
              :api_endpoint="api_endpoint"
              :requestBody = "requestBody"
              @list-updated="updateList"
              @item-deleted="deleteItemFromList"
              @projectId = "projectId"
              @displayItems = "displayItems"
            >
            </TaskList>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

  

<script>
import {getItem} from '../Api'
import PostTask from '../components/PostTask.vue';
import TaskList from '../components/TaskList.vue';


export default{
  emits : ['list-updated'],
  props: ['projectId'],
  components : {PostTask, TaskList},
  data() {
      return {
          list : [],
          requirementList: [],
          api_endpoint : "tasks",
          project : this.projectId,
          selected: null,
          requestBody : {
            task_name : "",
            is_completed : false,
            requirement : -1
          },
          viewPost : false
      };
  },
  methods: {
      async displayItems(){
          const project_id = localStorage.getItem("ProjectId")
          const api_endpoint = `getRequirementsForProject/${project_id}`
          const items = await getItem(api_endpoint)
          const user = localStorage.getItem("username")
          this.requirementList = items.filter(item => item.assigned_to === user)
      },
      async updateList(newlist){
        this.list = newlist
        await this.displayItems()
      },
      async displayTasks(id) {
        localStorage.setItem('requirementId', id);
        const data = await getItem(this.api_endpoint)
        this.list = data.filter(item => item.requirement===id)
      },
      async deleteItemFromList(id) { 
        this.list = this.list.filter(item => item.id !== id)
      },
  },
  async created() {
    await this.displayItems()
    await this.displayTasks()
  },
  async mounted() {
    await this.displayItems()
    this.displayTasks()

  },
  watch: {
    projectId(newVal) {
      this.project = newVal;
      this.displayItems();
      this.displayTasks()
    }
  },
}
</script>
