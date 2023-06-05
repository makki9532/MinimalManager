<template>
  <div>
    <div class="d-flex justify-content-between align-items-center mb-3 mt-3">
      <button @click="showPostForm" class="btn btn-success">Show Form</button>
      <button @click="hidePostForm" class="btn btn-dark">Hide Form</button>
    </div>    

    <PostRequirement
      v-if="toggler"
      :list="list"
      :title="title"
      :api_endpoint="api_endpoint"
      :projectId="requestBody.project"
      :requestBody="requestBody"
    />

    <div class="d-flex justify-content-between align-items-center mb-3 mt-3">
      <button @click="filterCompleted(true)" class="btn btn-success">Completed</button>
      <button @click="filterByPriorityAsc" class="btn btn-info">Priority Ascend</button>
      <button @click="filterCompleted(false)" class="btn btn-light">Not Completed</button>
      <button @click="filterByPriorityDesc" class="btn btn-info">Priority Descend</button>
      <button @click="displayItems" class="btn btn-dark">Get All</button>
    </div>

    <RequirementList
      :list="list"
      :api_endpoint="api_endpoint"
      :requestBody="requestBody"
      :projectId="requestBody.project"
      @item-deleted="deleteItemFromList"
      @displayItems = "displayItems"
    />
  </div>
</template>

<script>
import RequirementList from "../components/RequirementList.vue";
import PostRequirement from "../components//PostRequirement.vue";
import { getItem } from "../Api";

export default{
  props: ["projectId", "projectIdForAddMember"],
  data() {
    return {
      list: {},
      api_endpoint: "requirements",
      title: "Add a requirement",
      requestBody: {
        requirement_description: "",
        priority_rating: 1,
        completion_status: true,
        assigned_to: "",
        project: this.projectId,
      },
      toggler: true,
    };
  },
  methods: {
    async displayItems() {
      const project_id = localStorage.getItem("ProjectId");
      const api_endpoint = `getRequirementsForProject/${project_id}`;
      const items = await getItem(api_endpoint);
      this.list = items;
      this.list = items;
    },
    async deleteItemFromList(id) {
      this.list = this.list.filter((item) => item.id !== id);
      this.list = this.list.filter((item) => item.id !== id);
    },
    showPostForm() {
      this.toggler = true;
    },
    hidePostForm() {
      this.toggler = false;
    },
    filterCompleted(isCompleted) {
      this.list = this.list.filter(
        (item) => item.completion_status === isCompleted
      );
    },
    filterByPriorityAsc() {
      this.list = this.list.sort((a, b) =>
        a.priority_rating > b.priority_rating ? 1 : -1
      );
    },
    filterByPriorityDesc() {
      this.list = this.list.sort((a, b) =>
        a.priority_rating < b.priority_rating ? 1 : -1
      );
    },
  },
  async created() {
    await this.displayItems();
  },
  watch: {
    projectId(newVal) {
      this.requestBody.project = newVal;
      this.displayItems();
    },
  },
  components: { RequirementList, PostRequirement },
};
</script>
