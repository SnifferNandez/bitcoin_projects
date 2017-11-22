#!/usr/bin/env Rscript
#from http://estebanmoro.org/2015/12/temporal-networks-with-r-and-igraph-updated/
#remember create the folder "animation"
#edgesTime=300 -> ~3000 images
#this version of the script has been tested on igraph 1.0.1

#load libraries
if (!require("igraph")) {
  install.packages("igraph")
  library(igraph)
}
if (!require("RColorBrewer")) {
  install.packages("RColorBrewer")
  library(RColorBrewer)
}

#load the edges with time stamp
#there are three columns in edges (space separator): id1 id2 time
edges <- read.table("edges.txt",header=T)

#generate the full graph
g <- graph.data.frame(edges,directed=F)

#generate a cool palette for the graph (darker colors = older nodes)
YlOrBr.pal <- colorRampPalette(brewer.pal(8,"YlOrRd"))
#colors for the nodes are chosen from the very beginning
V(g)$color <- rev(YlOrBr.pal(vcount(g)))[as.numeric(V(g)$name)]

#time in the edges goes from 1 to 300. We kick off at time 3
ti <- 1
#remove edges which are not present
gt <- delete_edges(g,which(E(g)$time > ti))
#generate first layout using graphopt with normalized coordinates. This places the initially connected set of nodes in the middle.
layout.old <- norm_coords(layout.graphopt(gt), xmin = -1, xmax = 1, ymin = -1, ymax = 1)
#If you use fruchterman.reingold it will place that initial set in the outer ring.
#layout.old <- layout_with_fr(gt)
             
#total time of the dynamics
total_time <- max(E(g)$time)+1
#This is the time interval for the animation. In this case is taken to be 1/10 
#of the time (i.e. 10 snapshots) between adding two consecutive nodes 
dt <- 0.1
#Output for each frame will be a png with HD size 1600x900 :)
png(file="animation/example%03d.png", width=1600,height=900)
#Time loop starts
for(time in seq(1,total_time-dt,dt)){
  #remove edges which are not present
  gt <- delete_edges(g,which(E(g)$time > time))
  #with the new graph, we update the layout a little bit
  layout.new <- layout_with_fr(gt,coords=layout.old,niter=10,start.temp=0.05,grid="nogrid")
  #plot the new graph #https://stackoverflow.com/questions/39039667/fruchterman-reingold-algorithm-in-r
  plot(gt,layout=layout.new,vertex.label="",vertex.size=1+2*log(degree(gt)),vertex.frame.color=V(g)$color,edge.width=1.5,asp=9/16,margin=-0.15)
  #use the new layout in the next round
  layout.old <- layout.new 
}
dev.off()

#finally you can produce the video using the ffmpeg tool
#ffmpeg -r 10 -i example%03d.png -b:v 20M output.mp4
#The first -r 10 flag controls the rate of frames per second (fps), 10 in this case, while the -b:v 20M sets the bitrate in the output.
