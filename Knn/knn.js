var training=[
{

x:0.5,lable:"-",
x:3  ,lable:"-",
x:4.5,lable:"+",
x:4.6,lable:"+",
x:4.9,lable:"+",
x:5.2,lable:"-",
x:5.3,lable:"-",
x:5.5,lable:"+",
x:7 ,lable:"-",
x:9.5 ,lable:"-", 
}
]

var point =5;
var distan=[];
training.forEach(item=>{
	if(point -item.x>0)
	{
		distan.push(point-item);
	}
	else
	{
		distan.push(-(point-item));
	}
console.log(distan)
})

