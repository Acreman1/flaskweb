<template>
  <div>
    <div class='app-head'>
      <div class='app-head-inner'>
        <img src='./assets/logo.png'>
        <div class='head-nav'>
          <ul class='nav-list'>
            <li>登陆</li>
            <li class='nav-pile'>|</li>
            <li>注册</li>
            <li class='nav-pile'>|</li>
            <li>关于</li>
          </ul>
        </div>
      </div>
    </div>
    <div class='app-content'>
      <router-view></router-view>
    </div>
    <div class='app-footer'>
      <p>&copy; 1903c - 2020</p>
    </div>
  </div>
</template>

<script>
export default {
  
}
</script>

<style>
/* reset重置样式 */
html, body, div, span, object, iframe,
h1, h2, h3, h4, h5, h6, p, blockquote, pre,
abbr, address, cite, code,
del, dfn, em, img, ins, kbd, q, samp,
small, strong, sub, sup, var,
b, i,
dl, dt, dd, ol, ul, li,
fieldset, form, label, legend,
table, caption, tbody, tfoot, thead, tr, th, td,
article, aside, canvas, details, figcaption, figure, 
footer, header, hgroup, menu, nav, section, summary,
time, mark, audio, video {
    margin:0;
    padding:0;
    border:0;
    outline:0;
    font-size:100%;
    vertical-align:baseline;
    background:transparent;
    box-sizing:border-box;
}
body {
    line-height:1;
}
:focus {
    outline: 1;
}
article,aside,canvas,details,figcaption,figure,
footer,header,hgroup,menu,nav,section,summary { 
    display:block;
}
ul {
    list-style:none;
}
blockquote, q {
    quotes:none;
}
blockquote:before, blockquote:after,
q:before, q:after {
    content:'';
    content:none;
}
a {
    margin:0;
    padding:0;
    border:0;
    font-size:100%;
    vertical-align:baseline;
    background:transparent;
}
ins {
    background-color:#ff9;
    color:#000;
    text-decoration:none;
}
mark {
    background-color:#ff9;
    color:#000; 
    font-style:italic;
    font-weight:bold;
}
del {
    text-decoration: line-through;
}
abbr[title], dfn[title] {
    border-bottom:1px dotted #000;
    cursor:help;
}
table {
    border-collapse:collapse;
    border-spacing:0;
}
hr {
    display:block;
    height:1px;
    border:0;   
    border-top:1px solid #cccccc;
    margin:1em 0;
    padding:0;
}
input, select {
    vertical-align:middle;
}
/* Layout样式 */
body{
  background:#f0f2f5;
  font-size:14px;
  color:#444;
}
.app-head{
  background:#363636;
  color:#b2b2b2;
  height:90px;
  line-height:90px;
  width:100%;
}
.app-head-inner{
  width:1000px;
  margin:0 auto;
}
.app-head-inner img{
  float:left;
  width:50px;
  margin-top:20px;
}
.head-nav{
  float:right;
}
.head-nav li{
  float:left;
  cursor:pointer;
}
.nav-pile{
  padding:0 10px;
}
.app-footer{
  text-align:center;
  height:80px;
  line-height:80px;
  width:100%;
  background:#e3e4e8;
  margin-top:30px;
}
.app-content{
  width:1000px;
  margin:0 auto;
}
</style>
