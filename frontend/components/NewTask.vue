<template>
    <div class="rounded-lg overflow-hidden my-2 shadow w-1/2 mx-auto flex">
        <input v-model="task.title" type="text" name="company-website" class="flex-1 block w-full rounded-none rounded-r-md sm:text-sm border-gray-300 p-4 focus:outline-none" placeholder="Take a note..." />
        <button type="button" class="bg-purple-600 text-white font-bold p-4" @click="saveTask">Save</button>
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
                const data = new FormData();
                data.append("title", this.task.title)
                await this.$axios.post('http://127.0.0.1:8000/api/task-create/', data)
                this.task.title = ''
                this.$toast.success("Task Saved.")
        },

    }
}
</script>