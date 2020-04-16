<template>
    <div class='index-wrapper'>
        <div class='index-left'>
            <div class='index-left-block'>
                <h2>全部产品</h2>
                <template v-for='plist in productList'>
                    <h3>{{ plist.title }}</h3>
                    <ul>
                        <li v-for='item in plist.list'>
                            <a v-bind:href='item.url'>{{ item.title }}</a>
                            <span class='hot-tag' v-if='item.hot'>HOT</span>
                        </li>
                    </ul>
                    <div class='hr' v-if='plist.hr'></div>
                </template>   
            </div>
            <!-- 最新消息 -->
            <div class='index-left-block lastest-news'>
                <h2>最新消息</h2>
                <ul>
                    <li v-for="news in latestNews">
                        <a v-bind:href='news.url'>{{ news.title }}</a>
                    </li>
                </ul>
            </div>
        </div>
        <div class='index-right'>
            <slider-component></slider-component>
            <div class='index-border-list'>
                <div class='index-border-item' v-for="item in boardList">
                    <div class='index-border-item-inner'>
                        <h2>{{ item.title }}</h2>
                        <p>{{ item.description }}</p>
                        <div v-if="item.saleout" class='index-border-buttom'>
                            立即购买
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import SliderComponent from '../components/slidercomponent'
export default {
    components:{
        SliderComponent
    },
    mounted(){
        axios.get('api/getLatestNews')
        // => 函数可以理解为匿名函数
        .then((res) => {
            console.log(res)
            this.latestNews = res.data.list
        })
        .catch((error) => {
            comsole.log(error)
        });

        axios.get('api/getProductList')
        .then((res) => {
            console.log(res)
            this.productList = res.data
        })
        .catch((error) => {
            comsole.log(error)
        });
        
        axios.get('api/getBoardList')
        .then((res) => {
            console.log(res)
            this.boardList = res.data
        })
        .catch((error) => {
            comsole.log(error)
        })
    },
    data() {
        return {
            productList:null,
            latestNews:[],
            boardList:null
        }
    },
}
</script>

<style scoped>
    .index-wrapper{
        display:flex;
    }
    .index-left{
        width:30%;
    }
    .index-right{
        width:70%;
    }
    .index-left-block{
        margin: 15px;
        background:#ffffff;
        border-radius:10px;
        box-shadow:0 0 1px #dddddd;
    }
    .index-left-block .hr{
        border-bottom:1px solid #444;
        margin: 20px 0;
    }
    .index-left-block h2{
        background:#4fc08d;
        color:#ffffff;
        padding:10px 15px;
        margin-bottom:20px;
    }
    .index-left-block h3{
        color:#222;
        font-weight:bolder;
        padding:0 15px 5px 15px;
    }
    .index-left-block ul{
        padding:10px 15px;
    }
    .index-left-block ul li{
        padding:5px;
    }
    .index-border-list{
        display:flex;
        flex-wrap:wrap;
        margin-top:20px;
        justify-content:space-between;
    }
    .index-border-item{
        box-sizing:border-box;
        width:49%;
        height:125px;
        background:#ffffff;
        box-shadow: 0 0 1px #ddd;
        margin-bottom:20px;
        border-radius: 0 0 10px 10px;
        padding:20px;
    }
    .index-border-item-inner{
        height:125px;
        padding-left:180px;
        background-image:url(../assets/logo.png);
        background-repeat:no-repeat;
        background-size:30%;
    }
    .index-border-item-inner h2{
        font-size:18px;
        font-weight:bolder;
        color:#000;
        margin-bottom:15px;
    }
    .index-border-item-inner p{
        margin-bottom:15px;
    }
    .index-border-buttom{
        width:80px;
        height:35px;
        background:#4fc08d;
        color:#ffffff;
        border-radius:5px;
        text-align:center;
        line-height:40px;
    }
    .index-border-item:nth-child(1),.index-border-item:nth-child(3){
        margin-right:2%;
    }
    .index-left-block ul li a{
        text-decoration:none;
        color:black;
    }
    .hot-tag{
        color:#ffffff;
        background:#c04fb1;
        padding:0 10px;
    }

    .tongtong{
        box-sizing:border-box;
        width:700px;
        height:300px;
        background:#7e79f2;
        margin:15px auto 0;
    }
</style>