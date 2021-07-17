<!-- Please remove this file from your project -->
<template>
  <div class="w-full min-h-screen bg-gray-100 sm:items-center sm:pt-0">
    <Logo class="mx-auto text-center p-4" />
    <hr>
    <div class="max-w-4xl mx-auto sm:px-6 lg:px-8">
      <NewTask />
      <div class="rounded-lg bg-white shadow ">
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