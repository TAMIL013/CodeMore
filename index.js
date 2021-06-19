var express=require('express');
// const { spawn } = require('child_process');
var app=express();
var fs=require('fs');
app.set('view engine', 'ejs');
app.get('/',(req,res)=>{
    res.send("hello world")
})
app.get('/py',get_code_geeks)
app.get('/py/res',(req,res)=>{
    
//   res.send("hello");
  fs.readFile('result_geeks.txt', (err, data) => {
      if (err)
      {
        //   res.send(err.toString());
          res.status('404').send(err.toString());
      }
      else{
        //   console.log(data.toString());
          res.send(data.toString());

      }
  })
})
function get_code_geeks(req,res){
    url = "https://practice.geeksforgeeks.org/explore/?page=1&category%5B%5D=Kadane"
    var spawn = require("child_process").spawn;
 
    spawn('python',["./scraper.py",req.query.category]);
    // process.stdout.on('data', function(data) {
    //     console.log(data.toString());
    // } )
     res.render('result');
    // 
    
}
app.listen(process.env.PORT,()=>{console.log("listening on port 8000")})