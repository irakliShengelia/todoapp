<template>
  <App :tasks="tasks" />
</template>

<script>
export default {
  async asyncData({ $axios}) {
    try{
      const tasks = await $axios.$get('http://127.0.0.1:8000/api/task-list')
      return {tasks}
    }catch(e){
      const tasks = []
      return {e, tasks}
    }
  },
  head() {
    return{
      title: "Get things done"
    }
  },
}
</script>

