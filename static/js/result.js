var test_count=1;
var res=[];
function call(){
    // document.getElementById("test").innerHTML=test_count;
    // test_count=test_count+1;
 $.ajax({
     url: '/py/res',
 type: 'GET',
 // data:data,
 contentType: "application/json",
 success: function (result) {
     clearInterval(interval);
     console.log(result);
    //  array=result;
     // var json=JSON.stringify(result);
     // var arr=JSON.parse(result);
     res=result;
    loadData();
     
 },
 error: function(result){
     // console.log("result");
     console.log(result);
    
 } 
 });
};
var interval=setInterval(call,1000*5);

function loadData(){
    
    const head=document.getElementById("tag_container");
    var ele=String(res[0]).split("-");
    var element2="";
    ele.forEach(e=>{
        element2+=( e.charAt(0).toUpperCase() + e.slice(1)+" ");
    });
    head.innerHTML+=`<h4>${element2}</h4>
   <p class="text-muted">leetcode have ${res[1].length} problems and geeks for geeks have ${res[2].length} probelms</p>`;
    // document.getElementById("res").innerHTML=res[0].length+res[0][0].title+" | "+res[1][0].title;
    var page=Math.round(res[1].length/50)>1?Math.round(res[1].length/50):1;
    const table_container=document.getElementById("table_container");
    table_container.innerHTML+=`
     <ul class="nav nav-tabs" id="nav-bar">
                <li class="nav-item" id="nav_1"  >
                    <a role="button" class="nav-link text-dark" onclick="create_table(1)">Leetcode</a></li>
                <li class="nav-item" id="nav_2">
                    <a role="button" class="nav-link text-dark" onclick="create_table(2)">Geeksforgeeks</a></li>
            </ul>
            <table class="table  table-border">
                <thead class="table_head">
                    <td>#</td>
                    <td>Title</td>
                    <td>Difficulty</td>
                </thead>
                <tbody id="table_body">


                </tbody>
            </table>
            <ul class="pagination justify-content-center">
                <li class="page-item"><span class="material-icons"><a role="button" class="page-link text-secondary" onclick="pagination('previous')">
                arrow_left</a></span></li>
                <li class="page-item"><a role="button" class="page-link text-secondary" id="page-no">1/${page}Pages</a></li>
                <li class="page-item"><span class="material-icons"><a role="button" class="page-link text-secondary" onclick="pagination('next')">
                arrow_right</a></span></li>
            </ul>`;
    create_table(1);        
    
}
var current_active_site_index=1;
var current_pagination=[1,1];

function create_table(index){
    current_active_site_index=index;
    var nav=document.getElementById("nav_"+String(index));
    nav.setAttribute("style","background-color:#f2f2f2");
    for(var i=1;i<res.length;i++){
        if(i==index)
            continue;
        document.getElementById("nav_"+String(i)).removeAttribute("style")            
    }
    // console.log(current_active_site_index)
    const table=document.getElementById("table_body");
    table.innerHTML=``;
    var end=res[index].length<50?res[index].length:50;
    for(var i=0;i<end;i++){
        table.innerHTML+=`<tr>
        <td class="col-1">${i+1}</td>
        <td class="col-9"><a href="${res[index][i].link}">${res[index][i].title}</a></td>
        <td class="col-2" id="difficulty_col" >${res[index][i].difficulty}</td>
        </tr>`;
        var tag=table.rows[i].cells[2];
        var dif=res[index][i].difficulty;
        // tag.innerHTML=dif;
        if(dif=="Hard")
            tag.setAttribute("class","text-danger");
        else if(dif=="Medium")
            tag.setAttribute("class","text-warning");
        else if(dif=="Easy")
            tag.setAttribute("class","text-success");    
        else
            tag.setAttribute("class","text-info");    
        
    }
    if(res[index].length==0){
        table.innerHTML=`<tr><td></td><td><h4 class="text-danger">Code Unavailable,try another source.</h4></td><td></td></tr>`
    }    

}
function pagination(move){
    const table=document.getElementById("table_body");
    if(move=="next"){
        var site=current_active_site_index;
        var cur_page=current_pagination[site];
        var start=cur_page*50;
        var end=(cur_page+1)*50;
        end=res[site].length>=end?end:res[site].length;
    }
    else{
        
        var site=current_active_site_index;
        var cur_page=current_pagination[site];
        if(cur_page>1){
            var start=(cur_page-2)*50;
            var end=(cur_page-1)*50;
            current_pagination[site]=cur_page-1;
            document.getElementById("page-no").innerHTML=String(cur_page-1)+"/"+String(Math.round(res[1].length/50))+" Pages";
            table.innerHTML=``;
        }
        
    }    
        
        var i=0;
        for(start;start<end;start++){
            if(start==(cur_page*50)){
                current_pagination[site]=cur_page+1;
                document.getElementById("page-no").innerHTML=String(cur_page+1)+"/"+String(Math.round(res[1].length/50))+" Pages";
                table.innerHTML=``;
            }
            table.innerHTML+=`<tr>
            <td class="col-1">${start+1}</td>
            <td class="col-9"><a href="${res[site][start].link}">${res[site][start].title}</a></td>
            <td class="col-2" id="difficulty_col">${res[site][start].difficulty}</td>
            </tr>`;
            var tag=table.rows[i].cells[2];
            var dif=res[site][start].difficulty;
         
            if(dif=="Hard")
                tag.setAttribute("class","text-danger");
            else if(dif=="Medium")
                tag.setAttribute("class","text-warning");
            else if(dif=="Easy")
                tag.setAttribute("class","text-success");    
            else
                tag.setAttribute("class","text-info");  
            
            i=i+1;    
        }
        // console.log(current_pagination[site]);
    
        
}