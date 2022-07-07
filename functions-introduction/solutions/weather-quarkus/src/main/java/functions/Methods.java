package functions;

import java.io.*;
import java.net.URISyntaxException;
import java.net.URL;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

public class Methods
{
    ClassLoader classLoader = getClass().getClassLoader();
    String jsonFileName = "cities.json";
    Object weatherData = new Object();
    File jsonResourceFile;

    public Object read_weather() throws FileNotFoundException, IOException, ParseException, URISyntaxException {
        InputStream inputStream = classLoader.getResourceAsStream(jsonFileName);
        if (inputStream == null) {
            throw new IllegalArgumentException("JSON file not found! " + jsonFileName);
        } else {
            // Fetching URL of the JSON file.
            URL resource = classLoader.getResource(jsonFileName);
            if (resource == null) {
                throw new IllegalArgumentException("JSON file not found! " + jsonFileName);
            } else {
                // Creating a new file using url
                jsonResourceFile = new File(resource.toURI());
                weatherData = new JSONParser().parse(new FileReader(jsonResourceFile.toPath().toString()));
            }
        }
        return weatherData;
    }

    public double kelvin_to_celsius(double temp) {
        return temp - 273.15;
    }

    public double kelvin_to_fahrenheit(double temp) {
        return temp * 1.8 - 459.67;
    }
}
