<template>
    <h3 class="m-3">Welcome to minimal manager, {{ user }}</h3>
    <p class="m-3">Continue from your last project get or started by creating a new one</p>
  </template>
  
  <script>
    export default {
      data() {
        return {
          user : localStorage.getItem('username')
        };
      },
    };
  </script>
  