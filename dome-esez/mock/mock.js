import Mock from 'mockjs'

Mock.mock('/getPclist',{
    'list|5':[
        {
            url:'@url',
            title:'@ctitle(5,20)'
        }
    ]
})