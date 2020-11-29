mydata = accidentsbypopulation

library(stargazer)

fit <- lm(Accidents ~ Population, data=mydata)

stargazer(fit, type="html", style = "qje",
          dep.var.labels=c("Car Accidents"), 
          covariate.labels=c("Population"))
