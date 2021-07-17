<!-- Please remove this file from your project -->
<template>
  <div class="w-full min-h-screen bg-gray-100 sm:items-center sm:pt-0">
    <Logo class="mx-auto text-center p-4" />
    <hr>
    <div class="max-w-4xl mx-auto sm:px-6 lg:px-8 mb-4">
      <NewTask />
      <div class="rounded-lg bg-yellow-200 shadow my-2 p-4">
        <p>Welcome to the task manager. You can add the tasks above</p>
        <p>Editing Tasks is possible inline, just click the task, make changes and click somewhere outside</p>
      </div>
      <div class="rounded-lg overflow-hidden bg-white shadow ">
        <Task v-for="task in tasks" :key="task.id" :task="task" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    tasks: {
      type: Array,
      default: () => []
    }
  },
}
</script>