var express=require('express');

var app=express();
var fs=require('fs');
const expressLayouts = require('express-ejs-layouts')
const  bodyParser = require('body-parser')
 
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use('/static', express.static('static'))
app.use(expressLayouts)

app.set('layout', './layouts/main_layouts')
app.set('view engine', 'ejs');

app.get('/',(req,res)=>{
    res.render('result')
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
        data=JSON.parse(data)
          res.json(data);
        // res.send(data)
      }
  })
})
function get_code_geeks(req,res){
    var spawn = require("child_process").spawn;
  console.log(req.query.category);
    var process=spawn('python',["./scraper.py",req.query.category]);
    process.stdout.on('data', function(data) {
        console.log(data.toString());
        // res.send(data.toString());
    } )
    process.stderr.on('data',function(data){
      console.log(data.toString());
      // res.send(data.toString());
    });
     res.render('result');
    // 
    
}
app.listen(process.env.PORT||8000,()=>{console.log("listening on port 8000")})