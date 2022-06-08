package functions;

import java.io.FileReader;
import java.util.Iterator;
import java.util.*;
import org.json.simple.JSONObject;
import org.json.simple.parser.*;
import io.quarkus.funqy.Funq;

public class Function {

    @Funq
    public Output function(Input input) throws Exception
    {
                String fileName = "/home/shajain/DO244-Sample/quarkus-weather-app/cities.json";
                Object obj = new JSONParser().parse(new FileReader(fileName));

                // typecasting obj to JSONObject
                JSONObject jo = (JSONObject) obj;
                Map city = ((Map)jo.get("city"));
                Iterator<Map.Entry> itr1 = city.entrySet().iterator();
                double temp_kelvin = 0.0d,temp_celsius = 0.0d, temp_fahrenheit = 0.0d;
                Methods methods = new Methods();
                JSONObject finaljson =  new JSONObject();
                JSONObject tempjson =  new JSONObject();
                Map.Entry pair,pair2 = null;
                String str = input.getMessage();
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
                        temp_celsius = methods.kelvin_to_celsius(temp_kelvin);
                        temp_fahrenheit = methods.kelvin_to_fahrenheit(temp_kelvin);
                    }
                }
                finaljson.put("city",str);
                tempjson.put("celsius",temp_celsius);
                tempjson.put("fahrenheit",temp_fahrenheit);
                tempjson.put("kelvin",temp_kelvin);
                finaljson.put("temperature",tempjson);

        return new Output(finaljson.toJSONString());
    }

}
