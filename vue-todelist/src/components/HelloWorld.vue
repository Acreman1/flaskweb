<template>
  <div class="container" id="hello">
    <items-one></items-one>
    <h3>{{ workState }}</h3>
    <div class='well'>
      <div class='dao-timer'>
        <items-two></items-two>
      </div>
    </div>
  </div>
</template>

<script>

const WROK_STATES = {
        WORK:'工作中……',
        REST:'休息中……' 
      }
const WORKING_FEN = 25 
const RESITNG_MIAO = 5
const STATES = {
  STARTED:'started',
  STOPPED:'stopped',
  PAUSE:'pause'
}
var data = {
  minute:WORKING_FEN,
  second:0,
  workState:WROK_STATES.WORK,
  timestamp:0,
  state:STATES.STOPPED
}

Vue.component('Items-one', {
  el:function(){
    return "#hello"
  },
  data:function(){
    return data;
  },
  methods:{
    start:function(){
      this.state = STATES.STARTED
      clearInterval(this.interval)
      // this._tick()
      // 使用定时器，调用_tick函数
      this.interval = setInterval(this._tick,1000);
    },
    pause:function(){
      this.state = STATES.PAUSE
      clearInterval(this.interval)
    },
    stop:function(){
      this.state = STATES.STOPPED
      clearInterval(this.interval)
      this.workState = WROK_STATES.WORK
      this.minute = WORKING_FEN
      this.second = 0
    },
    // _tick这个函数用来判断时间
    _tick:function(){
      // second不是0，second减1
      if(this.second !== 0){
          this.second--;
          return;
      }
      // second是0,minute不是0,minute减1,second从0换59
      if(this.minute !== 0){
          this.minute--;
          this.second = 59;
          return;
      }
      // second是0，minute也是0，切换倒计时事件
      this.workState = this.workState===WROK_STATES.WORK?WROK_STATES.REST:WROK_STATES.WORK
      if(this.workState === WROK_STATES.WORK){
          this.minute = WORKING_FEN
      }else{
          this.minute = RESITNG_MIAO
      }
    }
  },
  template:'<h2>'+
  '<span>倒计时</span>'+
  '<button class="btn btn-default" :disabled="state === '+"'started'"+'" v-on:click="start()">'+
  '<span class="glyphicon glyphicon-play"></span>'+
  '</button>'+
  '<button class="btn btn-default" :disabled="state !== '+"'started'"+'" v-on:click="pause()">'+
  '<span class="glyphicon glyphicon-pause"></span>'+
  '</button>'+
  '<button class="btn btn-default" :disabled="state !== '+"'started'"+' && state !== '+"'pause'"+'" v-on:click="stop()">'+
  '<span class="glyphicon glyphicon-stop"></span>'+
  '</button>'+
  '</h2>'
})
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
