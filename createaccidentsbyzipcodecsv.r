zipdf = data.frame(zipcodes)

table(zipdf$Zipcode)

myfreq = as.data.frame(table(zipdf$Zipcode))

names(myfreq)[1] = 'Zipcode'

myfreq

write.csv(myfreq,"accidentsbyzipcode.csv", row.names = FALSE)
