const tag=document.getElementById("topic_tag");
const topic_tag=["array","string","dynamic-programming","math","greedy","depth-first-search","tree","hash-table",
"binary-search","sorting","breadth-first-Search","two-pointers","backtracking","stack","design","bit-manipulation",
"graph","trie","heap-priority-queue","linked-list","recursion","union-find","sliding-window","divide-and-conquer",
"ordered-set","segment-tree","queue","line-sweep","geometry","matrix","binary-indexed-tree","brainteaser","topological-sort",
"binary-search-tree","rolling-hash","database","binary-tree","prefix-sum","monotonic-stack",
"game-theory","segment-tree","hash-function","shortest-path","doubly-linked-list","merge-sort"];

topic_tag.forEach(element => {
    var ele=element.split("-");
    var element2="";
    ele.forEach(e=>{
        element2+=( e.charAt(0).toUpperCase() + e.slice(1)+" ");
    });
    tag.innerHTML+=`<a class="btn btn-sm" href="/py?category=${element}"  role="button">${element2}</a>`;
    
});