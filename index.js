var express=require('express');
// const { spawn } = require('child_process');
var app=express();
var fs=require('fs');

app.get('/',(req,res)=>{
    res.send("hello world")
})
app.get('/py',get_code_geeks)
function get_code_geeks(req,res){
    url = "https://practice.geeksforgeeks.org/explore/?page=1&category%5B%5D=Kadane"
    var spawn = require("child_process").spawn;
 
    spawn('python',["./scraper.py",req.query.category]);
    fs.readFile('./geeks.txt', 'utf8' , (err, data) => {
        if (err) {
          console.error(err)
          return
        }
        console.log(data)
        res.send(data)
      })
    
}
app.listen( process.env.PORT,()=>{console.log("listening on port 8000")})