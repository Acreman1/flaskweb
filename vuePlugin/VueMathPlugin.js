export default {
    install:function(Vue){
        // 自定义指令square,v-square
        Vue.directive('square',function(el,binding){
            el.innerHTML = Math.pow(binding.value,3)
        });
        Vue.directive('sqrts',function(el,binding){
            el.innerHTML = Math.sqrt(binding.value)
        })
    }
}