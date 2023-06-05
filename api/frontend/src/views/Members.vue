 <!-- AddMember -->
 <template>
    <form class="form-control mt-3" @submit.prevent="onSubmit">
      <div class="m-3">
        <h3 class="form-label">Add Member to the Project</h3>
        <input class="form-control" name="text" type="text" v-model="username">
      </div>
      <input type="submit" value="Add User" class="btn btn-primary m-3">
  </form>

  <ol class="list-group list-group-numbered mt-3" >
        <li class="list-group-item d-flex justify-content-between align-items-start" v-for="name in list">
          <div class="ms-2 me-auto">
            <div class="fw-bold" >{{ name }}</div>
            
            <span class="m-1">
              <button @click="del(name)" class="btn btn-danger">Del</button>
            </span>
          </div>
        </li>
    </ol>
</template>

<script>
import { postItem } from '../Api'
import { getItem } from '../Api'

export default {
    props: ['projectId', 'projectIdForAddMember'],
    data() {
        return{
            list : [],
            username : "",
        }
    },
    methods : {
        async onSubmit(){
            const requestBody = {
                project_id : localStorage.getItem('ProjectId'),
                username : this.username,
            }
            const data = await postItem(requestBody, 'addUserToProject')
            if (!data.found){
                alert("You have entered a user name that does not exist on the system")
                return
            }
            this.list = data.members
        },
        async displayItems(){
            const project_id = localStorage.getItem('ProjectId')
            const data = await getItem(`getUsersForProject/${project_id}`)
            this.list = data.members
        },
        async del(name){
            const requestBody = {
                project_id : localStorage.getItem('ProjectId'),
                member : name,
            } 
            const res = await postItem(requestBody, 'deleteUsersForProject')
            if (res.removed) {
                this.list = this.list.filter(item => item !== name)
            }
        },
    },
    async created() {
      await this.displayItems()
    },
    watch: {
        projectId(newVal) {
            this.project = newVal;
            this.displayItems();
        }
    }
}
</script>