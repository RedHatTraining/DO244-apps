//Creating a custom node module
// And making different functions

//Converting temperature unit from kelvin to celsius
exports.kelvin_to_celsius = function (temp_kelvin)
 {
    let temp_celsius = (temp_kelvin - 273.15);
    return temp_celsius;
 };

//Converting temperature unit from kelvin to fahrenheit
 exports.kelvin_to_farhenheit = function (temp_kelvin)
 {
    let temp_fahrenheit = (temp_kelvin * 1.8) - 459.67
    return temp_fahrenheit;
 };
