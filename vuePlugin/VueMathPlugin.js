export default {
    install:function(Vue){
        // 自定义指令square,v-square
        Vue.directive('square',function(el,binding){
            el.innerHTML = Math.pow(binding.value,3)
        });
        Vue.directive('sqrts',function(el,binding){
            el.innerHTML = Math.sqrt(binding.value)
        })
        Vue.directive('coss',function(el,binding){
            el.innerHTML = Math.cos(binding.value*Math.PI/180)
        })
        Vue.directive('sins',function(el,binding){
            el.innerHTML = Math.sin(binding.value*Math.PI/180)
        })
        Vue.directive('tans',function(el,binding){
            el.innerHTML = Math.tan(binding.value*Math.PI/180)
        })
    }
}