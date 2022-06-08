package functions;

public class Methods
{
    public double kelvin_to_celsius(double temp)
    {
        double temp_celsius = 0.0d;
        temp_celsius = temp - 273.15;
        return temp_celsius;
    }

    public double kelvin_to_fahrenheit(double temp)
    {
        double temp_fahrenheit = 0.0d;
        temp_fahrenheit = (temp * 1.8) - 459.67;
        return temp_fahrenheit;
    }
}
