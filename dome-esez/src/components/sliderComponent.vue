<template>
    <div class="slider-wrapper" @mouseover="clearInv" @mouseout="runInv">
        <div v-show="nowIndex === index" class="slider-item" v-bind:class="['item'+[index+1]]" v-for="(item,index) in sliderImgList" v-bind:key="index">
            <a herf="">
                <img style="width:700px;height:300px" v-bind:src="item.imgUrl">
            </a>
        </div>

        <h2 class="slider-title">{{ sliderImgList[nowIndex].title }}</h2>

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
                {
                    imgUrl:require('../assets/pic1.jpg'),
                    title:"第一张图片"
                },
                {
                    imgUrl:require('../assets/pic2.jpg'),
                    title:"第二张图片"
                },
                {
                    imgUrl:require('../assets/pic3.jpg'),
                    title:"第三张图片"
                },
                {
                    imgUrl:require('../assets/pic4.jpg'),
                    title:"第四张图片"
                }
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
        top:200px;
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
    .slider-title{
        background:#000000;
        color:white;
        width:180px;
        height:30px;
        position:relative;
        top:260px;
        left:10px;
        z-index:400;
        font-size:30px;
        text-align:center;
        line-height:30px;
        opacity:0.6;
    }
</style>