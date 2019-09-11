# Data center fa19-516-146

## E.datacenter.2.b

### The Dalles data center - Google

Located in the Dalles City, Oregon right off the Columbia river, Google's Dalles
data center opened in 2006 and was the first Google
designed and built itself.

As of the [2019 Quarter 2 performance report](https://www.google.com/about/datacenters/efficiency/internal/#performances-list),
the main
facility has a PUE of 1.11.

According to [baxtel.com](https://baxtel.com/data-center/google-the-dalles-oregon)
the total power for the site was 70.0 megawatts. Other sources online stated that
Google does not disclose details on energy consumption on individual data centers,
but for the sake of this analysis, we will assume this data is correct.

The industrial electricity rate for the Dalles is 4.2¢/kWh. This is considerably
lower than average rates in the United States and Oregon according to
[electricitylocal.com](https://www.electricitylocal.com/states/oregon/the-dalles/).
Assuming Google pays this rate, that would mean this site costs about \$70,560
per day to operate and \$25,754,400 a year.

```math
70,000 kW * 4.2¢/kWh * 24 hours = 70,560
```

```math
70,560 * 365days = 25,754,400
```

[Google claims](https://static.googleusercontent.com/media/www.google.com/en//green/pdfs/google-carbon-offsets.pdf)
that its data centers are carbon neutral. This is not done by running the data
centers off renewable energy directly, rather it accomplishes this by purchasing
carbon offsets.

In a [2018 report](https://www.oregon.gov/energy/Get-Involved/rulemakingdocs/2018-03-21-CO2-RAC-Background.pdf)
Oregon's net emission rate was `0.675 lb. CO2 per kWh`. If we assume since Google
is probably pulling energy from this same system we can estimate carbon footprint
without offsets to be `229,720.05 tons`

```math
70,000kW * 1.11PUE * 0.675lbs. * 24 hours * 365 days = 459,440,100lbs.
```

```math
459,440,100lbs ÷ 2000 = 229,720.05 tons
```

### References

- <https://www.google.com/about/datacenters/inside/locations/the-dalles/>
- <https://www.google.com/about/datacenters/efficiency/internal>
- <https://baxtel.com/data-center/google-the-dalles-oregon>
- <https://www.electricitylocal.com/states/oregon/the-dalles/>
- <https://static.googleusercontent.com/media/www.google.com/en//green/pdfs/google-carbon-offsets.pdf>
- <https://www.oregon.gov/energy/Get-Involved/rulemakingdocs/2018-03-21-CO2-RAC-Background.pdf>

## E.datacenter.3

My footprint is 12240lbs. of CO2 according the <http://carbonfootprint.c2es.org>.
Data record to [spreadsheet](https://docs.google.com/spreadsheets/d/1gh869zfjA4sVxL8-ga0af2_HLTTuOoD1IReuRSrbq4I/edit#gid=314181983).

## E.dataceneter.4

### Hydro

Hydroelectricity is the process of using water power to generate electricity.
This is accomplished by using dams to direct water to turbines that deliver
power generators. Those generators convert that power to electricity.

The Dalles data center presumably pulls power from the Dalles Hydroelectric
dam This dam is one of the largest in the United States and spans the Columbia
River a few miles away for the Google data center.

### References (E.dataceneter.4)

- <https://www.nwp.usace.army.mil/The-Dalles/>

## E.dataceneter.5

### Indiana renewable energy

Indiana produces a large amount of biofuels from corn and soy accounting for 8%
of total production in the United States. Burning ethnol fuel still releases
carbon, despite being a renewable source. It can be argued that since source
of the carbon is from a natural part of the carbon could be considered neutral.
However is not as clean a other renewable sources, such solar or wind.

This state is also 8th in the county when it comes to the number of windmills.
This makes up about 5% of Indiana's electricty.

### References(E.dataceneter.5)

- <https://www.eia.gov/state/?sid=IN>
- <https://www.eia.gov/state/analysis.php?sid=IN>
- <https://www.wlfi.com/content/news/Indiana-sees-surge-in-wind-power-despite-lack-of-standards-559829491.html>

## E.datacenter.8

Google data center outage on June 2, 2019

On Sunday, June 2, 2019, a server configuration change caused a 4 hour outage for Google services in the eastern United States. According to the [Inside Google Cloud article](https://cloud.google.com/blog/topics/inside-google-cloud/an-update-on-sundays-service-disruption) about the incident this resulted in some service being or not available for that region. Google reports YouTube by itself saw a 2.5% drop in views during this time. Other sources, [such as an article from 9to5Google](https://9to5google.com/2019/06/03/google-outage-cause/) reports that YouTube's global views went down by 10%, which is much higher than Google. This would be a significant loss in ads revenue. And that is only one of a many services that were affected. Others reported not being able to control their own thermostat, since Nest relies google services affect in the outage. I imagine the loss in customer good will is as much, if not more of a concern.

### References (E.datacenter.8)

- <https://www.datacenterdynamics.com/news/google-suffers-sunday-outage-impacts-cloud-youtube-gmail-and-more/>
- <https://9to5google.com/2019/06/03/google-outage-cause/>
- <https://cloud.google.com/blog/topics/inside-google-cloud/an-update-on-sundays-service-disruption>
