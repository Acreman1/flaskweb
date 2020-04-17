<template>
    <div class="slider-wrapper" @mouseover="clearInv" @mouseout="runInv">
        <div v-show="nowIndex === index" class="slider-item" v-bind:class="['item'+[index+1]]" v-for="(imgUrl,index) in sliderImgList" v-bind:key="index">
            <a herf="">
                <img style="width:700px;height:300px" v-bind:src="imgUrl">
            </a>
        </div>

        <a v-on:click="preHandler" class="btn pre-btn" href="javascript:void(0)">&lt;</a>
        <a v-on:click="nextHandler" class="btn next-btn" href="javascript:void(0)">&gt;</a>

        <ul class="slider-dots">
            <li v-on:click="clickDtos(index)" v-for="(item,index) in sliderImgList" v-bind:key="index">{{ index+1 }}</li>
        </ul>
    </div>
</template>

<script>
export default {
    data() {
        return {
            nowIndex:0,
            sliderImgList:[
                require('../assets/pic1.jpg'),
                require('../assets/pic2.jpg'),
                require('../assets/pic3.jpg'),
                require('../assets/pic4.jpg')
            ]
        }
    },
    methods:{
        clickDtos(index){
            this.nowIndex = index
        },
        preHandler(){
            this.nowIndex--;
            if(this.nowIndex < 0){
                this.nowIndex = 3
            }
        },
        nextHandler(){
            this.autoPlay()
        },
        autoPlay(){
            this.nowIndex++;
            if(this.nowIndex > 3){
                this.nowIndex = 0
            }
        },
        runInv(){
            this.invId = setInterval(this.autoPlay,2000)
        },
        clearInv(){
            clearInterval(this.invId)
        }
    },
    created(){
        this.runInv()
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
        left:300px;
        top:225px;
        z-index:500;
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
        cursor: pointer;
        opacity:0.6;
    }
    .btn{
        display:inline-block;
        text-decoration:none;
        color:#ffffff;
        width:50px;
        height:50px;
        background:#000000;
        font-size:40px;
        text-align:center;
        line-height:50px;
        position:relative;
        top:125px;
        z-index:300;
    }
    .pre-btn{
        left:15px;
        opacity:0.6;
    }
    .next-btn{
        left:580px;
        opacity:0.6;
    }
</style>