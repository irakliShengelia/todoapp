<template>
    <div class="rounded-lg overflow-hidden my-2 shadow w-full mx-auto flex">
        <input v-model="task.title" type="text" name="company-website" class="flex-1 block w-full rounded-none rounded-r-md sm:text-sm border-gray-300 p-4 focus:outline-none" placeholder="Take a note..." @keyup.enter="saveTask" />
        <button type="button" class="flex items-center gap-4 bg-purple-600 hover:bg-purple-500 text-white font-bold p-4" @click="saveTask">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-3m-1 4l-3 3m0 0l-3-3m3 3V4" />
            </svg>
            Save
        </button>
    </div>
</template>

<script>
export default {
    data() {
        return {
            task: {
                title: '',
                completed: false
            }
        }
    },
    methods: {
        async saveTask() {
            try{
                const data = new FormData();
                data.append("title", this.task.title)
                await this.$axios.post('http://localhost:8000/api/task-create/', data)
                this.task.title = ''
                this.$parent.$emit('task-changes')
                this.$toast.success("Task Saved.")
            }catch(e){
                this.$toast.error("Something Went Wrong. " + e.message)
            }
        },

    }
}
</script>