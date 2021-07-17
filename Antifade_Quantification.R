


library(viridis)
library(ggplot2)
library(dplyr)
library(ggthemes)
library(gridExtra)
library(tidyr)
library(reshape2)

antifade_data <- read.csv(file = "INPUT_FILE_HERE.csv", header = TRUE)
antifade_data

#This script can only handle one transcript at a time. Break out the data by transcript to plot each individually.




p <- ggplot(data=antifade_data, aes(x=Stack_No, y=Norm_avg_Mean, group=Antifade)) +
  geom_line(aes(color=Antifade))+
  geom_ribbon(aes(ymin=Norm_avg_Mean-Norm_SEM_Mean, ymax=Norm_avg_Mean+Norm_SEM_Mean, fill = Antifade), alpha=0.1, linetype = 0) +
  scale_colour_colorblind() +
  scale_fill_colorblind() +
  scale_x_continuous(limits=c(0,100), expand = c(0,0)) +
  scale_y_continuous(limits=c(0,1), expand = c(0,0)) +
  theme_classic() + theme(legend.position="bottom") + 
  #scale_color_brewer(palette = "Set1") +
  theme(panel.grid.major.y = element_line(colour = "grey60")) + 
  theme(panel.grid.major.x = element_line(colour = "grey80"))

p



