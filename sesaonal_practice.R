library(seasonal)


getwd()
Sys.setenv(X13_PATH = "C:/Users/Home/Documents")
checkX13()

str(AirPassengers)

#vignette("seas")
data(AirPassengers)
m <- seas(AirPassengers)

final(m)
plot(m)
summary(m)
# model
static(m)

#shiny
inspect(m)

# forecast hist
series(m, "forecast.forecasts")


# plotting
m <- seas(AirPassengers
          ,regression.aictest = c("td","easter"))
plot(m)
plot(m, outlier =FALSE)
plot(m, trend = TRUE)

monthplot(m)
monthplot(m, choice = "irregular")

# model analyis
pacf(resid(m))
spectrum(diff(resid(m)))
qqnorm(resid(m))
