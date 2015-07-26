#http://anson.ucdavis.edu/~hiwang/teaching/10fall/R_tutorial%201.pdf
rm(list = ls(all = TRUE))
#install.packages("OIsurv")
library(OIsurv)

 
data(aids)
head(aids)

data("tongue")
?tongue

attach(tongue)
surv_obj <- Surv(time[type==1], delta[type==1])
surv_obj
detach(tongue)

#kaplan - Meir estitamte and pointwise bounds
attach(tongue)
surv_obj <- Surv(time[type==1], delta[type==1])
survfit(surv_obj ~ 1) # log default
survfit(surv_obj ~ 1, conf.type = "log-log")
survfit(surv_obj ~ 1, conf.type = "plain")
survfit(surv_obj ~ 1, conf.int = 0.90)

fit <- survfit(surv_obj ~ 1)
summary(fit)$surv # Kaplan Meier Estimates
summary(fit)$time
summary(fit)$n.risk
summary(fit)$std.err 
str(fit)

plot(fit
     ,main = "Kaplan-Meier Esitmate with 95% Confidence Bounds"
     ,xlab = "time"
     ,ylab = "survival function")

# regressing on a group variable - strata
fit2 <- survfit( Surv( time, delta) ~ type)
summary(fit2)$strata

detach(tongue)

# Simultaneous confidence bands

data(bmt)
attach(bmt)
?bmt
surv_obj <- Surv(t2[group == 1], d3[group == 1])
cb <- confBands(surv_obj, confLevel = 0.95, type = "hall")

plot(survfit(surv_obj ~ 1)
     ,xlim = c(100,600)
     ,xlab = "time"
     ,ylab = "Estimated Survival Function"
     ,main = "Reproducing Confidence Bands")
lines(cb$time, cb$lower, lty=3, type = "s")
lines(cb$time, cb$upper, lty=3, type = "s")
legend(100, 0.3
       ,legend = c("K-M Survival Estimate"
       ,"pointwise intervals"
       ,"confidence bnads")
       ,lty = 1:3)
detach(bmt)

#Cumulative hazard function
data("tongue")
attach(tongue)

surv_obj <- Surv(time[type == 1], delta[type == 1])
fit <- summary(survfit( surv_obj ~ 1))
H_hat <- -log(fit$surv)
H_hat <- c(H_hat, tail(H_hat, 1))

h_sort_of <- fit$n.event / fit$n.risk
h_tilde <- cumsum(h_sort_of)
h_tilde <- c(h_tilde, tail(h_tilde, 1))

plot(c(fit$time, 250)
     ,H_hat
     ,xlab = "time"
     ,ylab = "cumulative hazard"
     ,main = "comparing cumulative harazrds"
     ,ylim = range(c(H_hat, h_tilde))
     ,type = "s")
points(c(fit$time, 250), h_tilde, lty=2, type ="s")
legend("topleft", legend = c("H.hat", "H.tilde"), lty = 1:2)

detach(tongue)


#Tests for two or more samples







