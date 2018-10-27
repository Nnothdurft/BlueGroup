allData = JSON.parse(all_data);
for(let i = 0; i < allData[0].length;i++){

}
console.log(allData[27].Longitude);
d3.select("body").selectAll("p")
    .data(allData)
    .enter()
    .append("p")
    .text(function(d){return d.Longitude});