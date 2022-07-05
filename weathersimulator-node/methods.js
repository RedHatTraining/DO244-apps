const path = require('path');
var fs = require("fs");

exports.read_weather = function (filename)
{
   if (!fs.existsSync(path.resolve(__dirname, filename))) {
       console.error('File not found'+filename);
       process.exit();
   }

   const filecontents = fs.readFileSync(path.resolve(__dirname, filename), "utf8");
   let weather = JSON.parse(filecontents);
   return weather;
}

exports.kelvin_to_celsius = function (temp_kelvin)
{
   let temp_celsius = (temp_kelvin - 273.15);
   return temp_celsius;
};

exports.kelvin_to_farhenheit = function (temp_kelvin)
{
   let temp_fahrenheit = (temp_kelvin * 1.8) - 459.67
   return temp_fahrenheit;
};
