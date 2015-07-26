library(hflights)
library(data.table)

DT <- as.data.table(hflights)
#first is where state
# 2nd is the select
# third is the group by
DT[Month==10, mean(na.omit(AirTime)),   by=UniqueCarrier]

class(DT)

#the i is the where used for subsetting
#these do the same
DT[3:5,]
DT[3:5]
# column names can be used too
DT[UniqueCarrier=='AA']
# return last row and then next to last
DT[.N]
DT[.N-1]

# the part is select or simply 'do stuff'
   #i part left blank
DT[   , mean(na.omit(ArrDelay))]

# .() must be used for several columns
DT[,.(mean(na.omit(DepDelay)),
      mean(na.omit(ArrDelay))
      )]
# these can be named on output
DT[,.(Avg_DepDelay = mean(na.omit(DepDelay)),
      Avg_ArrDelay = mean(na.omit(ArrDelay))
)]

# using i and j - where and select combined\
DT[UniqueCarrier=='AA',
   .(Avg_ArrDelay = mean(na.omit(ArrDelay)),
   plot(DepTime, DepDelay, ylim=c(-15,200)),
   abline(h=0))0
   ]

# the by part is group by
DT[,mean(na.omit(DepDelay)), by=Origin]

DT[,.(Avg_Delay_byWeekdays = 
        mean(na.omit(DepDelay))),
   by = .(Origin, Weekdays = DayOfWeek)
   ]

# all three parts used in tandem
DT[UniqueCarrier=='DL',
    .(Avg_DepDelay = mean(na.omit(DepDelay)),
      Avg_ArrDelay = mean(na.omit(ArrDelay)),
      Compensation = mean(na.omit(ArrDelay - DepDelay))),
          by = .(Origin, Weekdays = DayOfWeek)]


#--------------------------------------
# doing a speed test vs Dplyr and Base

system.time(
  DT[
    #UniqueCarrier=='DL'
     ,.(Avg_DepDelay = mean(na.omit(DepDelay)),
       Avg_ArrDelay = mean(na.omit(ArrDelay)),
       Compensation = mean(na.omit(ArrDelay - DepDelay))),
     by = .(Origin, Weekdays = DayOfWeek)]
  )

library(dplyr)

system.time(
as.data.frame(DT) %>%
  #filter(UniqueCarrier=='DL') %>%
  group_by(Origin, DayOfWeek) %>%
  summarize(
    Avg_DepDelay = mean(na.omit(DepDelay)),
    Avg_ArrDelay = mean(na.omit(ArrDelay)),
    Compensation = mean(na.omit(ArrDelay - DepDelay))
    )
)


# base R approximation

blah <- function(x) {
#sub =  subset(as.data.frame(x), UniqueCarrier=='DL')
sub = x
  
aggregate(DepDelay ~ Origin + DayOfWeek, data=sub, mean)

aggregate(ArrDelay ~ Origin + DayOfWeek, data=sub, mean)

sub$Compensation = sub$ArrDelay - sub$DepDelay

aggregate(Compensation ~ Origin + DayOfWeek, data=sub, mean)
}

system.time(blah(DT))



