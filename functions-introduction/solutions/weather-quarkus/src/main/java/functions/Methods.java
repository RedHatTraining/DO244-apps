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
    Object weather = new Object();
    File jsonResourceFile;

    public Object read_weather() throws URISyntaxException, FileNotFoundException, IOException, ParseException
    {
        InputStream inputStream = classLoader.getResourceAsStream(jsonFileName);
        if (inputStream == null)
        {
            throw new IllegalArgumentException("JSON file not found! " + jsonFileName);
        } else
        {
            // Fetching URL of the JSON file.
            URL resource = classLoader.getResource(jsonFileName);
            if (resource == null) {
                throw new IllegalArgumentException("JSON file not found! " + jsonFileName);
            } else {
                // Creating a new file using url
                jsonResourceFile = new File(resource.toURI());
                weather = new JSONParser().parse(new FileReader(jsonResourceFile.toPath().toString()));
            }
        }

        return weather;
    }

    public double kelvin_to_celsius(double temp)
    {
        temp = temp - 273.15;
        return temp;
    }

    public double kelvin_to_fahrenheit(double temp)
    {
        temp = temp * 1.8 - 459.67;
        return temp;
    }
}
