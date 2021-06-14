var express=require('express');
// const { spawn } = require('child_process');
var app=express();


app.get('/',(req,res)=>{
    res.send("hello world")
})
app.get('/py',get_code_geeks)
function get_code_geeks(req,res){
    url = "https://practice.geeksforgeeks.org/explore/?page=1&category%5B%5D=Kadane"
    var spawn = require("child_process").spawn;
 
    var process = spawn('python',["./scraper.py",req.query.category]);
    process.stdout.on('data', function(data) {
        var d=data.toString();
        res.send(d);
    } )
    // res.send(process)
}
app.listen(process.env.PORT,()=>{console.log("listening on port 8000")})