{{ config(materialized='table')}}

SELECT
    Observation_ID,
    City,
    Region,
    Country,
    Timezone,
    Local_time,
    Last_updated,
    Is_day,
    round(avg(Temp_celsius)::numeric, 2) as Avg_temp_celsius,
    round(avg(Temp_fahrenheit)::numeric, 2) as Avg_temp_fahrenheit,
    round(avg(Heatindex_celsius)::numeric, 2) as Avg_heatindex_celcius,
    round(avg(Heatindex_fahrenheit)::numeric, 2) as Avg_heatindex_fahrenheit,
    will_it_rain,
    chance_of_rain
FROM {{ref("stg_weather_data")}}
