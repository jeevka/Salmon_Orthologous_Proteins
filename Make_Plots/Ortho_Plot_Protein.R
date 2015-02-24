library(ggplot2)
library(grid)
theme_set(theme_bw())
library(extrafont)

plot_plot<-function(dat1,out_file,qseq_length,Query)
{
    ##########################################################
    #
    ##########################################################
    c2 <- ggplot(dat1,aes(x=bps,y=Fish,colour=factor(Idn)))
    #c2 <- ggplot()
    c2 <- c2 + geom_point(aes(x=bps,y=Fish,colour=factor(Idn),size=1),dat1)
    #c2 <- c2 + geom_line(aes(x=R,y=Fish,group=Domain,size=2,colour="red"),DF)
    #c2 <- c2 + geom_text(aes(x=R,y=Fish,label=Domain),DF)
    #c2 <- c2 + geom_text(aes(label=Scaf))
    
    txt <- paste("Length of protein sequence (bps)",sep="")
    c2 <- c2 + xlab(txt) + ylab("Fish orthologous proteins")
    #c2 <- c2 + xlim(1,as.integer(qseq_length))
        

    ##########################################################
    # Other Plotting options
    ##########################################################
    c2 <- c2 +  theme(axis.title.x = element_text(size=25,face = "bold")) 
    c2 <- c2 +  theme(axis.title.y = element_text(size=25,face = "bold",angle = 90))
    
    c2 <- c2 + theme(axis.text.x=element_text(size=25,face = "bold"))
    #c2 <- c2 + theme(axis.text.y=element_blank()) #element_text(size=25,face = "bold"))
    c2 <- c2 + theme(axis.text.y=element_text(size=25,face = "bold"))
    #c2 <- c2 + scale_colour_discrete("Identity")
    #c2 <- c2 + scale_y_discrete(breaks=c("Stickle","Cod","Zebra","Trout","Salmon"))
    
    c2 <- c2 + theme(legend.title=element_text(size=20,face = "bold"))
    c2 <- c2 + theme(legend.text = element_text(size = 16))
    c2 <- c2 + theme(legend.key.size = unit(0.8, "cm"))
    c2 <- c2 + theme(legend.text.align=0)
    c2 <- c2 + theme(legend.position="none" )#c(0.05,0.80))
    
    png(out_file,width=680,height=600)
    print(c2)
    dev.off()

}


#######################################################################################
################################ MAIN PROGRAM #########################################
#######################################################################################
#args<-commandArgs(TRUE)

args <- commandArgs(trailingOnly = TRUE)

# Input File
input_file <- args[1]

#dat1<-read.csv(file="Formatted_For_Plot.csv",sep='\t',header=FALSE)
dat1<-read.csv(file=input_file,sep='\t',header=FALSE)
colnames(dat1)<-c("Fish","QID","bps","Idn","QL")

# Domain File
#DF <- read.csv(file="Domain.csv",sep="\t",header=FALSE)
#colnames(DF)<-c("Fish","ID","R","Domain")

# Output File 
Query <- unique(dat1$QID)
out_file <- paste(Query,".png",sep="")

qseq_length <- unique(dat1$QL)

dat2 <- subset(dat1,Idn==1)
#plot_plot(dat2,out_file,qseq_length,Query,DF)

#dat1$Fish<-factor(dat1$Fish, levels=c("Stickle","Cod","Zebra","Trout","Salmon"))
#dat1 <- within(dat1, Fish <- factor(Fish, levels = c("Stickle","Cod","Zebra","Trout","Salmon")))

plot_plot(dat2,out_file,qseq_length,Query)
