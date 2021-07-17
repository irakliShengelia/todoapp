<template>
    <div class="flex justify-between gap-4 p-4 border-b bg-gray-50 hover:bg-gray-100 items-center" :class="{'opacity-25': task.completed && !editInProgress }">
       <div class="w-5/6 cursor-pointer" @click="startEdit">
        <span v-if="!editInProgress">
            {{task.title}}
        </span>
        <input v-if="editInProgress" v-model="updatedTask.title" class="p-4 w-full" @blur="updateTask"/>
        </div>
       <div class="w-1/6 text-right">
        <button class="ml-auto bg-green-400 hover:bg-green-500 text-white px-2 py-2 rounded-lg" @click="switchCompletion">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
        </button>
        <button class="bg-red-200 text-white px-2 py-2 rounded-lg hover:bg-red-600" @click="deleteTask">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
            </svg>
        </button>
       </div> 
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
    },
    data() {
        return {
            editInProgress: false,
            updatedTask: {
                title: '',
                completed: false
            }
        }
    },
    created() {
        this.updatedTask = {...this.task}
    },
    methods: {
        async deleteTask(){
            try{
                await this.$axios.delete(`http://localhost:8000/api/task-delete/${this.task.id}/`)
                this.$parent.$emit('task-changes')
                this.$toast.success("Task Removed Succesfully.")
            }catch(e){
                this.$toast.error("Something Went Wrong. " + e.message)
            }
        },
        async switchCompletion(){
            try{
                const data = new FormData();
                data.append("title", this.task.title)
                data.append("completed", !this.task.completed)
                await this.$axios.patch(`http://localhost:8000/api/task-update/${this.task.id}/`, data)
                this.$parent.$emit('task-changes')
                this.$toast.success("Task Updated Succesfully.")
            }catch(e){
                this.$toast.error("Something Went Wrong. " + e.message)
            }
        },
        async updateTask() {
            try{
                const data = new FormData();
                data.append("title", this.updatedTask.title)
                data.append("completed", this.updatedTask.completed)
                await this.$axios.patch(`http://localhost:8000/api/task-update/${this.task.id}/`, data)
                this.$parent.$emit('task-changes')
                this.$toast.success("Task Updated Succesfully.")
                this.editInProgress = false
            }catch(e){
                this.$toast.error("Something Went Wrong. " + e.message)
            }
        },
        startEdit() {
            this.editInProgress = true
        }
    }
}
</script>