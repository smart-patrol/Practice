#http://ramnathv.github.io/rCharts/


require(devtools)
install_github('rCharts', 'ramnathv')
library(rCharts)

#uses formulas to just like latice to generate plots

## example 1 facetted Scatterplot
data(iris)
names(iris) = gsub("\\.", "", names(iris))
rPlot(SepalLength ~ SepalWidth | Species, data = iris, color = 'Species', type = 'point')

## Example 2 Facetted Barplot
data(HairEyeColor)
hair_eye = as.data.frame(HairEyeColor)
rPlot(Freq ~ Hair | Eye , color = 'Eye', data= hair_eye, type='bar')

#using ploychart fomr javascript , based of ggplot2
r1 <- rPlot(mpg ~ wt | am + vs , data=mtcars, type="point",color="gear")
r1
# not that tooltips are acutmoatically embedded in charts

#adding inter
graph_chart1.addHandler(function(type, e){
  var data = e.evtData;
  if (type === 'click'){
    return alert("You clicked on car with mpg: " + data.mpg.in[0]);
  }
})

#######################
# Using MorrisJS
data(economics, package = "ggplot2")
econ <- transform(economics, date = as.character(date))
m1 <- mPlot(x = "date", y = c("psavert", "uempmed"), type = "Line", data = econ)
m1$set(pointSize = 0, lineWidth = 1)
m1$print("chart2")

#########################3
# Usiung NVD3
hair_eye_male <- subset(as.data.frame(HairEyeColor), Sex="Male")
n1 <- nPlot(Freq ~ Hair, group="Eye", data=hair_eye_male,
            type="multiBarChart")
n1$print("Chart3")

n1

#########################3
# Usiung xCharts
require(reshape2)
usexp <- melt(USPersonalExpenditure)
names(usexp)[1:2] = c("category", "year")
x1 <- xPlot(value ~ year, group = "category", 
            data= usexp, type="line-dotted")
x1










