
var margin = {top: 50, right: 10, bottom: 100, left:100},
    width = 700 - margin.right - margin.left,
    height = 500 - margin.top - margin.bottom;


// define x and y scales
var xScale = d3.scale.ordinal()
    .rangeRoundBands([0,width], 0.2, 0.2);

var yScale = d3.scale.linear()
    .range([height, 0]);

// define x axis and y axis
var xAxis = d3.svg.axis()
    .scale(xScale)
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(yScale)
    .orient("left");



// Adds the svg canvas
var	chart1 = d3.select("body")
	.append("svg")
		.attr("width", width + margin.left + margin.right)
		.attr("height", height + margin.top + margin.bottom)
	.append("g")
		.attr("transform", "translate(" + margin.left + "," + margin.top + ")");
		
		
var	chart2 = d3.select("body")
	.append("svg")
		.attr("width", width + margin.left + margin.right)
		.attr("height", height + margin.top + margin.bottom)
	.append("g")
		.attr("transform", "translate(" + margin.left + "," + margin.top + ")");
var	chart3 = d3.select("body")
	.append("svg")
		.attr("width", width + margin.left + margin.right)
		.attr("height", height + margin.top + margin.bottom)
	.append("g")
		.attr("transform", "translate(" + margin.left + "," + margin.top + ")");
d3.json("dataJSON.json", function(error,data) {
  if(error) console.log("Error: data not loaded!");
  


  data.forEach(function(d) {
    d.Ime = d.Ime;
    d.Nadmorska_visina = +d.Nadmorska_visina;       
    console.log(d.Nadmorska_visina);   
  });

  // prikaz nadmorske visine
  data.sort(function(a,b) {
    return b.Nadmorska_visina - a.Nadmorska_visina;
  });

  // Specify the domains of the x and y scales
  xScale.domain(data.map(function(d) { return d.Ime; }) );
  yScale.domain([0, d3.max(data, function(d) { return d.Nadmorska_visina; } ) ]);
  chart1.selectAll('rect')
    .data(data)
    .enter()
    .append('rect')
    .attr("height", 0)
    .attr("y", height)
    .transition().duration(3000)
    .delay( function(d,i) { return i * 200; })
    // attributes can be also combined under one .attr
    .attr({
      "x": function(d) { return xScale(d.Ime); },
      "y": function(d) { return yScale(d.Nadmorska_visina); },
      "width": xScale.rangeBand(),
      "height": function(d) { return  height - yScale(d.Nadmorska_visina); }
    })
    .style("fill", function(d,i) { return 'rgb(20, 20, ' + ((i * 30) + 100) + ')'});


    chart1.selectAll('text')
        .data(data)
        .enter()
        .append('text')
		.text(function(d){return d.Nadmorska_visina;})
        .attr({
            "x": function(d){ return xScale(d.Ime) +  xScale.rangeBand()/2; },
            "y": function(d){ return yScale(d.Nadmorska_visina)+ 12; },
            "font-family": 'sans-serif',
            "font-size": '13px',
            "font-weight": 'bold',
            "fill": 'white',
            "text-anchor": 'middle'
			});

    // Draw xAxis and position the label
    chart1.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis)
        .selectAll("text")
        .attr("dx", "-.8em")
        .attr("dy", ".25em")
        .attr("transform", "rotate(-60)" )
        .style("text-anchor", "end")
        .attr("font-size", "10px");

	 chart1.append("g")
        .attr("class", "y axis")
        .call(yAxis)
        .append("text")
        .attr("transform", "rotate(-90)")
		.attr("y",0 - margin.left)
        .attr("x",0 -(height/2))
        .attr("dy", "0.71em")
        .style("text-anchor", "middle")
        .text("Nadmorska visina (m)");

   
});
//Prikaz povrsine
d3.json("dataJSON.json", function(error,data) {
  if(error) console.log("Error: data not loaded!");
  

//pretvorba vrijednosti izrazenih u stringu u brojeve
  data.forEach(function(d) {
    d.Ime = d.Ime;
    d.Velicina = +d.Velicina;       
    console.log(d.Velicina);   
  });

  //sortiranje prema velicini
  data.sort(function(a,b) {
    return b.Velicina - a.Velicina;
  });

  
  xScale.domain(data.map(function(d) { return d.Ime; }) );
  yScale.domain([0, d3.max(data, function(d) { return d.Velicina; } ) ]);

  chart2.selectAll('rect')
    .data(data)
    .enter()
    .append('rect')
    .attr("height", 0)
    .attr("y", height)
    .transition().duration(3000)
    .delay( function(d,i) { return i * 200; })
    .attr({
      "x": function(d) { return xScale(d.Ime); },
      "y": function(d) { return yScale(d.Velicina); },
      "width": xScale.rangeBand(),
      "height": function(d) { return  height - yScale(d.Velicina); }
    })
    .style("fill", function(d,i) { return 'rgb(20, 20, ' + ((i * 30) + 100) + ')'});


        chart2.selectAll('text')
            .data(data)
            .enter()
            .append('text')



            .text(function(d){
                return d.Velicina;
            })
            .attr({
                "x": function(d){ return xScale(d.Ime) +  xScale.rangeBand()/2; },
                "y": function(d){ return yScale(d.Velicina); },
                "font-family": 'sans-serif',
                "font-size": '13px',
                "font-weight": 'bold',
                "fill": 'black',
                "text-anchor": 'middle'
            });

   
    chart2.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis)
        .selectAll("text")
        .attr("dx", "-.8em")
        .attr("dy", ".25em")
        .attr("transform", "rotate(-60)" )
        .style("text-anchor", "end")
        .attr("font-size", "10px");


   chart2.append("g")
        .attr("class", "y axis")
        .call(yAxis)
        .append("text")
        .attr("transform", "rotate(-90)")
		.attr("y",0 - margin.left)
        .attr("x",0 -(height/2))
        .attr("dy", "0.71em")
        .style("text-anchor", "middle")
        .text("Površina grada (km^2)");
  
});



//Prikaz broja stanovnika


d3.json("dataJSON.json", function(error,data) {
  if(error) console.log("Error: data not loaded!");
  

 
  data.forEach(function(d) {
    d.Ime = d.Ime;
    d.Broj_stanovika = +d.Broj_stanovika;       
    console.log(d.Broj_stanovika);   
  });

  
  data.sort(function(a,b) {
    return b.Broj_stanovika - a.Broj_stanovika;
  });

  
  xScale.domain(data.map(function(d) { return d.Ime; }) );
  yScale.domain([0, d3.max(data, function(d) { return d.Broj_stanovika; } ) ]);

  chart3.selectAll('rect')
    .data(data)
    .enter()
    .append('rect')
    .attr("height", 0)
    .attr("y", height)
    .transition().duration(3000)
    .delay( function(d,i) { return i * 200; })
    .attr({
      "x": function(d) { return xScale(d.Ime); },
      "y": function(d) { return yScale(d.Broj_stanovika); },
      "width": xScale.rangeBand(),
      "height": function(d) { return  height - yScale(d.Broj_stanovika); }
    })
    .style("fill", function(d,i) { return 'rgb(20, 20, ' + ((i * 30) + 100) + ')'});


		chart3.selectAll('text')
            .data(data)
            .enter()
            .append('text')
            .text(function(d){
                return d.Broj_stanovika;
            })
            .attr({
                "x": function(d){ return xScale(d.Ime) +  xScale.rangeBand()/2; },
                "y": function(d){ return yScale(d.Broj_stanovika)+12; },
                "font-family": 'sans-serif',
                "font-size": '13px',
                "font-weight": 'bold',
                "fill": 'white',
                "text-anchor": 'middle'
            });

   
    chart3.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis)
        .selectAll("text")
        .attr("dx", "-.8em")
        .attr("dy", ".25em")
        .attr("transform", "rotate(-60)" )
        .style("text-anchor", "end")
        .attr("font-size", "10px");


   
    chart3.append("g")
        .attr("class", "y axis")
        .call(yAxis)
        .append("text")
        .attr("transform", "rotate(-90)")
		.attr("y",0 - margin.left)
        .attr("x",0 -(height/2))
        .attr("dy", "0.71em")
        .style("text-anchor", "middle")
        .text("Broj stanovnika");
	
	
});