data = {};
$.getJSON("http://127.0.0.1:5000/", function(tempData){
    data = JSON.parse(tempData);
});
console.log(data);
// d3.json("http:127.0.0.1:5000/").then( function(data){
//     console.log(data);
// });
// console.log(JSON.parse(data_js));