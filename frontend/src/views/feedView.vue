

<template>
    <main class="px-8 py-6 bg-gray-100">
           <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
               <div class="main-center col-span-3 space-y-4">
                   <div class="bg-white border border-gray-200 rounded-lg">
                       <form v-on:submit.prevent="submitform" method="post">
                       <div class="p-4">  
                           <textarea v-model="body" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="paste your address here"></textarea>
                       </div>

                       <div class="p-4 border-t border-gray-100 flex justify-between">
                           <button class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg">Post</button>
                       </div>
                      </form>

                   </div>


                   <div class="p-4 bg-white border border-gray-200 rounded-lg"
                      >
                       <div class="mb-6 flex items-center justify-between">
                           <div class="flex items-center space-x-6">
                               <p><strong> price native {{ this.price_native}}</strong></p>
                               <p><strong> price USD {{ this.price_usd}}</strong></p>
                               
                               <div class="mb-6 flex items-center justify-between" 
                               v-for="(k,v) in volumes">
                               <p><strong> {{ k }}</strong></p>
                               <p><strong> {{ v }}</strong></p>
                               </div>
                           </div>
                       </div>
                   </div>
               </div>

           </div>
       </main>
</template>
<script>
import axios from 'axios'
import { useUserStore } from '@/stores/user'

export default{
   name:'feedview',
   data() {
       return {
           price_native:'',
           price_usd:'',
           volumes:{},
           body: '',
       }
   },

   methods: {
       submitform(){
           axios
               .post('/get_data/',{'body':this.body})
               .then(response => {
                   console.log('data', response.data)
                //    this.posts.push(response.data)
                   this.price_native=response.data.price_native
                    this.price_usd=response.data.price_usd
                    this.volumes=response.data.volume
                    // console.log('price_native',this.price_native)
                   this.body=''
               })
               .catch(error => {
                   console.log('error', error)
               })
       }
   }
}
</script>