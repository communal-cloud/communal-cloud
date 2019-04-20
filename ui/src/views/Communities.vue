
  <template>
  <div class="home">
   
    <b-container class="bv-example-row">
  
  <b-row>
    <community></community>
     <community></community>
      <community></community>
    </b-row>


  
</b-container>
  </div>
</template>

<script>
// @ is an alias to /src

import Community from '@/components/Community.vue'

export default {
  name: 'home',
  components: {
    Community
  }
}
</script>