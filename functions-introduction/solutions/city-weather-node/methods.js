const path = require('path');
var fs = require("fs");


module.exports = {

   read_weather(cityName) {
      const filePath = path.resolve(__dirname, "cities.json");

      if (!fs.existsSync(filePath)) {
          console.error('File not found'+filename);
          process.exit();
      }

      const filecontents = fs.readFileSync(filePath, "utf8");
      const weather = JSON.parse(filecontents);

      const cityLowerCase = (cityName || "").toLowerCase()
      return weather.city[cityLowerCase];
   },

   kelvin_to_celsius(temp_kelvin) {
      return temp_kelvin - 273.15;
   },

   kelvin_to_farhenheit(temp_kelvin) {
      return temp_kelvin * 1.8 - 459.67;
   }
}