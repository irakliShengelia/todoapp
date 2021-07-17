<template>
  <App :tasks="tasks" @task-changes="refreshTasks"/>
</template>

<script>
export default {
  async asyncData({ $axios}) {
    try{
      const tasks = await $axios.$get('http://localhost:8000/api/task-list/')
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
  methods: {
    async refreshTasks() {
      try{
        const tasks = await this.$axios.$get('http://localhost:8000/api/task-list/')
        this.tasks = tasks
      }catch(e){
        return {e}
      }
    }
  }
}
</script>

