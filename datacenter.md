# Data center fa19-516-146

## E.datacenter.2.b

### The Dalles data center - Google

Located in the Dalles City, Oregon right off the Columbia river, Google's Dalles data center opened in 2006 and was the first Google designed and built itself.

As of the [2019 Quarter 2 performance report](https://www.google.com/about/datacenters/efficiency/internal/#performances-list), the main facility has a PUE of 1.11.

According to [baxtel.com](https://baxtel.com/data-center/google-the-dalles-oregon) the total power for the site was 70.0 megawatts. Other sources online stated that Google does not disclose details on energy consumption on individual data centers, but for the sake of this analysis, we will assume this data is correct.

The industrial electricity rate for the Dalles is 4.2¢/kWh. This is considerably lower than average rates in the United States and Oregon according to [electricitylocal.com](https://www.electricitylocal.com/states/oregon/the-dalles/). Assuming Google pays this rate, that would mean this site costs about \$70,560 per day to operate and \$25,754,400 a year.

```math
70,000 kW * 4.2¢/kWh * 24 hours = 70,560
```

```math
$70,560 * 365days = 25,754,400
```

[Google claims](https://static.googleusercontent.com/media/www.google.com/en//green/pdfs/google-carbon-offsets.pdf) that its data centers are carbon neutral. This is not done by running the data centers off renewable energy directly, rather it accomplishes this by purchasing carbon offsets.

In a [2018 report](https://www.oregon.gov/energy/Get-Involved/rulemakingdocs/2018-03-21-CO2-RAC-Background.pdf) Oregon's net emission rate was `0.675 lb. CO2 per kWh`. If we assume since Google is probably pulling energy from this same system we can estimate carbon footprint without offsets to be `229,720.05 tons`

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