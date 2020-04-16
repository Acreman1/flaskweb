<template>
  <div id='app'>
    <h1>{{ WROK_STATES.WORK }}</h1>
  </div>
</template>

<script>

export default {
  name: 'app',
  data () {
    return {
      WROK_STATES:{
        WORK:'工作中……',
        REST:'休息中……' 
      },
      WORKING_FEN:25,
      RESITNG_MIAO:5,
      STATES:{
        STARTED:'started',
        STOPPED:'stopped',
        PAUSE:'pause'
      },
      data:{
        minute:this.WORKING_FEN,
        second:0,
        workState:this.WROK_STATES.WORK,
        timestamp:0,
        state:this.STATES.STOPPED
      }
    }
  }
}
</script>

<style></style>
