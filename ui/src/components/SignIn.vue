<template>
  <div>
    
    <b-input-group 
    prepend="e-mail" 
    class="mt-3"
    id="fieldset1"
    description="Let us know your email."
    label="Enter your email"
    label-for="input1"
    :invalid-feedback="invalidFeedback"
    :valid-feedback="validFeedback"
    :state="state">
    <b-form-input />
   
  </b-input-group>
   <b-input-group 
    prepend="Password" 
    class="mt-3"
    id="fieldset1"
    label="Enter your password"
    label-for="input1"
    :invalid-feedback="invalidFeedback"
    :valid-feedback="validFeedback"
    :state="state">
    <b-form-input type="password" />
   
  </b-input-group>
  </div>
</template>

<script>
  export default {
    computed: {
      state() {
        return this.name.length >= 4 ? true : false
      },
      invalidFeedback() {
        if (this.name.length > 4) {
          return ''
        } else if (this.name.length > 0) {
          return 'Enter at least 4 characters'
        } else {
          return 'Please enter something'
        }
      },
      validFeedback() {
        return this.state === true ? 'Thank you' : ''
      }
    },
    data() {
      return {
        name: ''
      }
    }
  }
</script>