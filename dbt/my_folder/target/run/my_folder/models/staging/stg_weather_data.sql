
  create view "weather"."public"."stg_weather_data__dbt_tmp"
    
    
  as (
    SELECT 
    id as Observation_ID,
    name as City,
    region as Region,
    country as Country,
    cast(timezone_id as timestamp) as Timezone,
    cast(local_time as timestamp) as Local_time,
    cast(last_updated as timestamp) as Last_updated,
    cast(is_day as boolean) as Is_day,
    temp_celcius as Temp_celsius,
    temp_farenheit as Temp_fahrenheit,
    heatindex_celcius as Heatindex_celsius,
    heatindex_farenheit as Heatindex_fahrenheit,
    cast(will_it_rain as boolean) as Will_it_rain,
    chance_of_rain as Chance_of_rain

FROM "weather"."public"."weather_data"
  );