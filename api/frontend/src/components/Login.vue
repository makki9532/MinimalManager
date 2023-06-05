<template>
    <div class="container mt-3 justify-content-center align-items-center">
      <h1 class="align-center">Login</h1>
      <form action="" method=POST class="form-control">
        <div class="mb-3">
          <label for="exampleInputEmail1" class="form-label">username</label>
          <input type="text" class="form-control" v-model="username" aria-describedby="emailHelp">
        </div>
        <div class="mb-3">
          <label for="exampleInputPassword1" class="form-label">Password</label>
          <input type="password" class="form-control" v-model="password">
        </div>
        <button @click="login" type="submit" class="btn btn-primary">Submit</button>
      </form>
      <p>If you don't have an account sign up <a href="http://127.0.0.1:8000/api/signup">here</a>
      </p>
    </div>
</template>

<script>
export default{  
  data(){
        return{
            username : '',
            password : '',
        }
    },
    methods: {
        async login(e) {
            e.preventDefault()
            const auth = {
              username : this.username,
              password : this.password,
              }
            const res = await fetch('http://127.0.0.1:8000/api/login',
                    {method: 'POST',
                    headers: {
                    'Content-Type' : 'application/json',
                    },
                    body: JSON.stringify(auth),
                    credentials: "include",
                    mode: "cors",
                    referrerPolicy: "no-referrer",
                    })
            const data = await res.json()
            if (!data.success){
              alert(data.message)
              return
            }
            console.log(document.cookie)
            localStorage.setItem("login_status", data.success)
            localStorage.setItem("token", data.token)
            localStorage.setItem("id", data.id)
            localStorage.setItem("username", data.username)
            localStorage.setItem("account_type", data.account_type)
            this.$emit('loginStatus')
            location.reload();
        },
    }
}
</script>