freqdf = as.data.frame(accidentsbyzipcode)
popdf = as.data.frame(`2010+Census+Population+By+Zipcode+(ZCTA)(1)`)

#look at data
head(freqdf)
head(popdf)
tail(freqdf)
tail(popdf)

#clean the dataframes by dropping rows not in both
dropthese = which(!freqdf$Zipcode %in% popdf$Zip.Code.ZCTA)    
freqdf = freqdf[-dropthese,]
dropthese = which(!popdf$Zip.Code.ZCTA %in% freqdf$Zipcode)    
popdf = popdf[-dropthese,]


#look at new data
head(freqdf)
head(popdf)
tail(freqdf)
#u can see a duplicate after looking at the end of popdf... we'll have to remove the duplicates
tail(popdf)


#this shows there are more rows in popdf then freqdf...
nrow(popdf)
nrow(freqdf)

#clean pop data
library(dplyr)
popdf = distinct(popdf,Zip.Code.ZCTA, .keep_all = TRUE)

#check
nrow(popdf)
nrow(freqdf)
head(freqdf)
head(popdf)
tail(freqdf)
tail(popdf)

freqbypopDF = data.frame("Zipcode"=freqdf$Zipcode, "Accidents"=freqdf$Freq, "Population"=popdf$X2010.Census.Population)
head(freqbypopDF)

#save as csv
write.csv(freqbypopDF,"accidentsbypopulation.csv", row.names = FALSE)
