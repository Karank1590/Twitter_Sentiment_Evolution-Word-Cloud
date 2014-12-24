function main(){

	keyword = $("#text-select").val();
	visualize(keyword);
	
	$("#text-select" ).change(function () {

	keyword = $("#text-select").val();
	$("svg").remove();
	visualize(keyword);
	
	});

}

function visualize(csvname){
var fill = d3.scale.category20();
minimum = 10000000;
maximum = 0;
path="data/"+csvname+".csv";
d3.csv(path, function(data) {
  data.forEach(function(d) {
    d.size = +d.count;
    d.text = d.name;
    if(d.size < minimum)
    	minimum = d.size;
    if(d.size > maximum)
    	maximum = d.size;
    //d.text = d.name;
  });
  //alert(minimum);
  //alert(maximum);
  
  
  d3.layout.cloud().size([1600, 800])
      .words(data)
      .padding(5)
      .rotate(function() { return ~~(Math.random() * 2) * 90; })
      .font("Impact")
      //.fontSize(function(d) { return Math.max(8, Math.min(d.size, 24)); })
      .fontSize(function(d) { return (10 + ((d.size-minimum)*(100-10)/(maximum - minimum))); })
      .on("end", draw)
      .start();

  function draw(words) {
    d3.select("body").append("svg")
        .attr("width", 1600)
        .attr("height", 800)
      .append("g")
        .attr("transform", "translate(800,400)")
      .selectAll("text")
        .data(data)
      .enter().append("text")
        .style("font-size", function(d) { return d.size + "px"; })
        .style("font-family", "Impact")
        .style("fill", function(d, i) { return fill(i); })
        .attr("text-anchor", "middle")
        .attr("transform", function(d) {
          return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
        })
        .text(function(d) { return d.text; });
  }
});

}

$(document).ready(main);