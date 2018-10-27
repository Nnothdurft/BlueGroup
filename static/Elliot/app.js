// The code for the chart is wrapped inside a function that
// automatically resizes the chart
function makeResponsive() {

  // if the SVG area isn't empty when the browser loads,
  // remove it and replace it with a resized version of the chart
  var svgArea = d3.select("body").select("svg");

  // clear svg is not empty
  if (!svgArea.empty()) {
    svgArea.remove();
  }

  // SVG wrapper dimensions are determined by the current width and
  // height of the browser window.
  var svgWidth = window.innerWidth;
  var svgHeight = window.innerHeight;

  var margin = {
    top: 5,
    bottom: 100,
    right: 50,
    left: 75
  };

  var height = svgHeight - margin.top - margin.bottom;
  var width = svgWidth - margin.left - margin.right;

  // Append SVG element
  var svg = d3
    .select(".chart")
    .append("svg")
    .attr("height", svgHeight)
    .attr("width", svgWidth);

  // Append group element
  var chartGroup = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);

  // Read CSV
  // d3.csv("S&P.csv")
  //   .then(function(PriceData) {
      PriceData = JSON.parse(csvData);
      // create date parser
      var dateParser = d3.timeParse("%d-%b-%Y");

      // parse data
      PriceData.forEach(function(data) {
        data.Date = Date.parse(data.Date);
        data.Price = +data.Price;
        console.log(data);
      });
      // create scales
      var xTimeScale = d3.scaleTime()
        .domain(d3.extent(PriceData, d => d.Date))
        .range([0, width]);

      var yLinearScale = d3.scaleLinear()
        .domain([0, d3.max(PriceData, d => d.Price)])
        .range([height, 0]);

      // create axes
      var xAxis = d3.axisBottom(xTimeScale).tickFormat(d3.timeFormat("%b-%Y"));
      var yAxis = d3.axisLeft(yLinearScale).ticks(8);

      // append axes
      chartGroup.append("g")
        .attr("transform", `translate(0, ${height})`)
        .call(xAxis);

      chartGroup.append("g")
        .call(yAxis);

      // line generator
      var line = d3.line()
        .x(d => xTimeScale(d.Date))
        .y(d => yLinearScale(d.Price));

      // append line
      chartGroup.append("path")
        .data([PriceData])
        .attr("d", line)
        .attr("fill", "none")
        .attr("stroke", "red");
      // console.log(PriceData.price[2]);
      // append circles
      var circlesGroup = chartGroup.selectAll("circle")
        .data(PriceData)
        .enter()
        .append("circle")
        .attr("cx", d => xTimeScale(d.Date))
        .attr("cy", d => yLinearScale(d.Price))
        .attr("r", "1")
        .attr("fill", "red");

      //Add X-Axis Label
      chartGroup.append("text")
        .attr("transform", `translate(${width/2-70}, ${height})`)
        .attr("x", 0)
        .attr("y", 60)
        .attr("value", "dates")
        .classed("active", true)
        .text("4.8 Years of Historical Data");


      //Add Y-Axis Label
      chartGroup.append("text")
        .attr("transform", "rotate(-90)")    
        .attr("y", 0 - margin.left)
        .attr("x", 0 - (height/2))
        .attr("dy", "1em")
        .attr("value", "price")
        // .classed("axis-text", true)
        .classed("active", true)
        .text("S&P 500 Price");



      // Date formatter to display dates nicely
      var dateFormatter = d3.timeFormat("%d-%b-%Y");

      //currency format
      const USD = new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
        minimumFractionDigits: 2
      })

      // Step 1: Initialize Tooltip
      var toolTip = d3.tip()
        .attr("class", "tooltip")
        .offset([80, -60])
        .html(function(d) {
          return (`<strong>${dateFormatter(d.Date)}<strong><hr>${USD.format(d.Price)}
          close price`);
        });

      // Step 2: Create the tooltip in chartGroup.
      chartGroup.call(toolTip);

      // Step 3: Create "mouseover" event listener to display tooltip
      circlesGroup.on("mouseover", function(d) {
        toolTip.show(d, this);
      })
      // Step 4: Create "mouseout" event listener to hide tooltip
        .on("mouseout", function(d) {
          toolTip.hide(d);
        });
    // });
}

// When the browser loads, makeResponsive() is called.
makeResponsive();

// When the browser window is resized, makeResponsive() is called.
d3.select(window).on("resize", makeResponsive);
