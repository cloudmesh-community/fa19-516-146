# Data center fa19-516-146

## E.datacenter.2.b

### The Dalles data center - Google

Located in the Dalles City, Oregon right off the Columbia river, Google's Dalles data center opened in 2006 and was the first Google designed and built itself.

As of the [2019 Quarter 2 performance report](https://www.google.com/about/datacenters/efficiency/internal/#performances-list), the main facility has a PUE of 1.11.

According to [baxtel.com](https://baxtel.com/data-center/google-the-dalles-oregon) the total power for the site was 70.0 megawatts. Other sources online state that Google does not disclose details on enery comsuption on individual data centers.

The industrial electricity rate for the Dalles is 4.2¢/kWh. This is considerable lower than average rates in the United States and Oregon according to [electricitylocal.com](https://www.electricitylocal.com/states/oregon/the-dalles/). Assuming Google pays this rate, that would mean this site costs about \$70,560 a per day to operate and \$25,754,400 a year.

```math
70,000 kW \times
4.2¢/kWh \times 24 hours
= \$70,560
```

```math
\$70,560 \times 365days = \$25,754,400
```

[Google claims](https://static.googleusercontent.com/media/www.google.com/en//green/pdfs/google-carbon-offsets.pdf) that its data centers are carbon neutral. This is not done by running the data centers off renewable energery directly, rather it accomplishes this by purchasing carbon offsets.

In a [2018 report](https://www.oregon.gov/energy/Get-Involved/rulemakingdocs/2018-03-21-CO2-RAC-Background.pdf) Oregan's net emission rate was `0.675 lb. CO2 per kWh`. If we assume since Google is probably pulling energy from this same system we can estimate carbon footprint without offsets to be `229,720.05 tons`

```math
70,000kW \times
1.11PUE \times
0.675lbs. \times
24 hours \times 365 days
= 459,440,100lbs.
```

```math
\frac{459,440,100lbs}{2000}
= 229,720.05 tons
```

### References

- <https://www.google.com/about/datacenters/inside/locations/the-dalles/>
- <https://www.google.com/about/datacenters/efficiency/internal>
- <https://baxtel.com/data-center/google-the-dalles-oregon>
- <https://www.electricitylocal.com/states/oregon/the-dalles/>
- <https://static.googleusercontent.com/media/www.google.com/en//green/pdfs/google-carbon-offsets.pdf>
- <https://www.oregon.gov/energy/Get-Involved/rulemakingdocs/2018-03-21-CO2-RAC-Background.pdf>