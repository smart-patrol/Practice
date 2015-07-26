#http://www.ats.ucla.edu/stat/r/examples/asa/asa_ch2_r.htm
# Survival Analysis Practice 

library(survival)
library(dplyr)
library(tidyr)
library(plyr)
library(lubridate)


hmohiv<-read.table("http://www.ats.ucla.edu/stat/r/examples/asa/hmohiv.csv", sep=",", header = TRUE) 

mini <- hmohiv[ID <= 5, ]
mini

attach(mini)
mini.surv <- survfit(Surv(time, censor) ~ 1 , conf.type="none")
summary(mini.surv)
plot(mini.surv , xlab="Time", ylab="Survival Prob.")

detach(mini)
attach(hmohiv)
hmohiv.surv <- survfit(Surv(time, censor)~1, conf.type="none")
summary(hmohiv.surv)
plot(hmohiv.surv , xlab="Time", ylab="Survival Prob.")

#using lifetable 
#install.packages("KMsurv")
library(KMsurv)
library(nlme)

t6m <- floor(time/6)
tall <- data.frame(t6m, censor)
die <- gsummary(tall, sum, groups=t6m)
total <- gsummary(tall, length, groups=t6m)
rm(t6m)
ltab.data <- cbind(die[,1:2], total[,2])
detach(hmohiv)
attach(ltab.data)

lt=length(t6m)
t6m[lt+1]=NA
nevent=censor
nlost=total[,2] - censor
mytable<-lifetab(t6m, 100, nlost, nevent)
mytable[,1:5]

plot(t6m[1:11], mytable[,5], type="s",xlab="Surviavl time",
     ylab="Propotion Surviving")

plot(t6m[1:11], mytable[,5], type="b",xlab="Surviavl time",
     ylab="Propotion Surviving")


library(survival) ; library(km.ci)

hmohiv.surv <- survfit( Surv(time, censor) ~ 1)
a <-km.ci(hmohiv.surv, conf.level=0.95, tl=NA, tu=NA, method="loghall")

par(cex=.8)
plot(a , lty=2, lwd=2)
time.conf <- survfit(Surv(time , censor) ~ 1)
lines(time.conf, lwd=2 , lty=1)
lines(time.conf, lwd=1 , lty=4 , conf.int=T)
linetype <- c(1,2,4)
legend(40, .9 , c("Kaplan-Meier", "Hall-Wellner", "Pointwise"), lty=(linetype))


detach()
attach(mini)
mini.surv <- survfit(Surv(time,  censor) ~1 , conf.type="none")
summary(mini.surv)
par(cex=.8)
plot(mini.surv, xlab="Time", ylab="Survival Probability")
lines(x=c(5,5),y=c(0,.6), lty=2) 
lines(x=c(8,8),y=c(0,.3), lty=2)
lines(x=c(0,22),y=c(.25,.25), lty=2) 
lines(x=c(0,8),y=c(.5,.5), lty=2)
lines(x=c(0,5),y=c(.75,.75), lty=2)


#cleaing up
rm(list=(ls()))
cat("\014") 

minitest<-read.table("http://www.ats.ucla.edu/stat/r/examples/asa/minitest.txt", header = TRUE) 
attach(minitest)
minitest

survdiff(Surv(time , censor) ~ drug, data=minitest, rho=0)
survdiff(Surv(time , censor) ~ drug, data=minitest, rho=1)

rm(list=ls()) #cleaning up 
cat("\014")
hmohiv<-read.table("http://www.ats.ucla.edu/stat/r/examples/asa/hmohiv.csv", sep=",", header = TRUE) 
attach(hmohiv)

survdiff(Surv(time, censor) ~ drug, rho=0)
survdiff(Surv(time, censor) ~ drug, rho=1)

agecat <- cut(age, c(19.9, 29, 34, 39, 54.1))
age.surv <- survfit(Surv(time, censor) ~ strata(agecat), conf.type="log-log")
age.surv

plot(age.surv , lty=c(6,1,4,3), xlab="Time", ylab="Survival Probability")
legend(40, 1.0, c("Group 1", "Group 2", "Group 3", "Group 4"), lty=c(6, 1, 4, 3))

survdiff(Surv(time, censor) ~ agecat, rho=0)
survdiff(Surv(time, censor) ~ agecat, rho=1)


