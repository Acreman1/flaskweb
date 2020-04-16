<template>
    <div class="slider-wrapper" @mouseover="clearInv" @mouseout="runInv">
        <div class="slider-item item1">1</div>
        <div class="slider-item item2">2</div>
        <div class="slider-item item3">3</div>
        <div class="slider-item item4">4</div>

        <ul class="slider-dots">
            <li>&lt;</li>
            <li>1</li>
            <li>2</li>
            <li>3</li>
            <li>4</li>
            <li>&gt;</li>
        </ul>
    </div>
</template>

<script>
export default {
    props:{
        inv:{
            type:Number,
            default:1000
        }
    },
    data() {
        return {
            
        }
    },
    methods:{
        runInv(){
            setInterval(()=>{

            },this.Inv)
        },
        clearInv(){

        }
    }
}
</script>

<style>
    .slider-wrapper{
        width:700px;
        height:300px;
        background:red;
        margin-top:15px;
    }
    .slider-item{
        width:700px;
        height:300px;
        text-align:center;
        line-height:300px;
        font-size:40px;
        position:absolute;
    }
    .item1{
        z-index:100;
    }
    .item2{
        z-index:90;
    }
    .item3{
        z-index:80;
    }
    .item4{
        z-index:70;
    }
    .slider-dots{
        position:relative;
        top:270px;
        left:250px;
    }
    .slider-dots li{
        width:15px;
        height:15px;
        border-radius:50%;
        background:#ffffff;
        text-align:center;
        line-height:15px;
        float:left;
        margin:0 10px;
        opacity:0.6;
    }
</style>