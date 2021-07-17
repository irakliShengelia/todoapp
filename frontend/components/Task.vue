<template>
    <div class="flex p-4 border-b bg-gray-50 hover:bg-gray-100">
       <div class="w-5/6">{{task.title}}</div>
       <div class="w-1/6">{{task.completed}}</div> 
    </div>
</template>

<script>
export default {
    props: {
        task: {
            type: Object,
            default: () => {
                return {
                    title: 'Loading...',
                    completed: false
                }
            }
        }
    }
}
</script>