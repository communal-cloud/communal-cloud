<template>

<div class="card" style="width: 22rem;">
  <div class="card-body">
    <h5 class="card-title">{{name}}</h5>
     <h6 class="card-subtitle mb-2 text-muted">{{purpose}}</h6>
    <p class="card-text">{{description}}</p>
    <a href="#" class="btn btn-primary">Explore</a>
  </div>
</div>

</template>

<script>
  export default {
    
    data() {
      return {
        name: 'Bird Watchers',
        purpose:'Watch and record birds',
        description:'Bird wathers gather together to record birds pictures and locations'
      }
    }
  }
</script>