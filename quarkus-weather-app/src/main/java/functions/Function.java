package functions;

import java.io.FileReader;
import java.util.Iterator;
import java.util.*;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;
import org.json.simple.JSONObject;
import org.json.simple.parser.*;
import io.quarkus.funqy.Funq;

@Path("")
public class Function {

    @GET
    @Path("/weather/{cityname}")
	@Produces(MediaType.APPLICATION_JSON)
    @Funq
    public Object function(@PathParam("cityname") String cityname) throws Exception
    {
                String fileName = "/home/shajain/DO244-Sample/quarkus-weather-app/cities.json";
                Object obj = new JSONParser().parse(new FileReader(fileName));

                System.out.println("Path param is: "+cityname);
                // typecasting obj to JSONObject
                JSONObject jo = (JSONObject) obj;
                Map city = ((Map)jo.get("city"));
                Iterator<Map.Entry> itr1 = city.entrySet().iterator();
                double temp_kelvin = 0.0d,temp_celsius = 0.0d, temp_fahrenheit = 0.0d;
                Methods methods = new Methods();
                JSONObject finaljson =  new JSONObject();
                JSONObject tempjson =  new JSONObject();
                Map.Entry pair,pair2 = null;
                String str = "tokyo";
                while (itr1.hasNext()) {
                    pair = itr1.next();
                    if(pair.getKey().toString().equals(str))
                    {
                        JSONObject jsonObj =  (JSONObject)pair.getValue();
                        Map map = ((Map)jsonObj.get("main"));
                        Iterator<Map.Entry> itr2 = map.entrySet().iterator();
                        while(itr2.hasNext())
                        {
                            pair2 = itr2.next();
                            if(pair2.getKey().toString().equals("temp"))
                            {
                                temp_kelvin = (double) pair2.getValue();
                            }
                        }
                        System.out.println("The value of temperature is: "+temp_kelvin+" "+'\u00B0'+"K");
                        temp_celsius = methods.kelvin_to_celsius(temp_kelvin);
                        System.out.println("The value of temperature in Celsius is: "+temp_celsius+" "+'\u00B0'+"C");
                        temp_fahrenheit = methods.kelvin_to_fahrenheit(temp_kelvin);
                        System.out.println("The value of temperature in fahrenheit is: "+temp_fahrenheit+" "+'\u00B0'+"F");
                    }
                }
                finaljson.put("city",str);
                tempjson.put("celsius",temp_celsius);
                tempjson.put("fahrenheit",temp_fahrenheit);
                tempjson.put("kelvin",temp_kelvin);
                finaljson.put("temperature",tempjson);

        return finaljson;
    }

}
