package com.redhat.training.weather;

import java.io.*;
import java.net.URISyntaxException;
import java.net.URL;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

public class Methods {
    ClassLoader classLoader = getClass().getClassLoader();
    String jsonFileName = "cities.json";

    public Object read_weather() throws FileNotFoundException, IOException, ParseException, URISyntaxException {
        URL fileResource = classLoader.getResource( jsonFileName );
        File jsonResourceFile = new File( fileResource.toURI() );
        return new JSONParser().parse( new FileReader( jsonResourceFile.toPath().toString() ) );
    }

    public double kelvin_to_celsius( double temp ) {
        return temp - 273.15;
    }

    public double kelvin_to_fahrenheit( double temp ) {
        return temp * 1.8 - 459.67;
    }
}
