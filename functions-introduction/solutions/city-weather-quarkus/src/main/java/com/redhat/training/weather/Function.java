package com.redhat.training.weather;

import org.json.simple.JSONObject;
import io.quarkus.funqy.Funq;

public class Function {

    @Funq
    public Output function( Input input ) throws Exception {
        double tempInKelvin = 0.0d;
        Methods methods = new Methods();
        JSONObject cityDetailsJson = new JSONObject(), tempDetailsJson = new JSONObject();
        String cityName = input.getCity();
        boolean isCityNamePresent = false;

        // Get weather data from Json file
        JSONObject weatherData = (JSONObject) methods.read_weather();
        Object obj = weatherData.get( "city" );
        JSONObject weatherDetails = (JSONObject) obj;

        // Get weather by city_name
        if ( weatherDetails.containsKey( cityName ) ) {
            isCityNamePresent = true;
            Object cityDetails = weatherDetails.get( cityName );
            JSONObject city = (JSONObject) cityDetails;

            // Get kelvin temperature from city
            if ( city.containsKey( "main" ) ) {
                Object tempDetails = city.get( "main" );
                JSONObject temperature = (JSONObject) tempDetails;
                tempInKelvin = (double) temperature.get( "temp" );
            }
        }

        // If city name cannot be found
        if ( isCityNamePresent == false ) {
            cityDetailsJson.put( "city", cityName );
            cityDetailsJson.put( "message", "City cannot be found!!" );

            return new Output( cityDetailsJson.toJSONString() );
        }

        // Convert kelvins to Celisus and Fahrenheit.
        // Build the response
        cityDetailsJson.put( "city", cityName );
        tempDetailsJson.put( "celsius", methods.kelvin_to_celsius( tempInKelvin ) );
        tempDetailsJson.put( "fahrenheit", methods.kelvin_to_fahrenheit( tempInKelvin ) );
        tempDetailsJson.put( "kelvin", tempInKelvin );
        cityDetailsJson.put( "temperature", tempDetailsJson );

        return new Output( cityDetailsJson.toJSONString() );
    }
}
