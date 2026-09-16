def convert_temperature(value, conversion_func):
    """
    Convert temperature using the provided conversion function.
    
    Args:
        value: Temperature value to convert
        conversion_func: Function that performs the conversion
    
    Returns:
        Converted temperature value
    """
    return conversion_func(value)


# Conversion functions
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32


def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin"""
    return celsius + 273.15


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9


def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin"""
    return (fahrenheit - 32) * 5/9 + 273.15


def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius"""
    return kelvin - 273.15


def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit"""
    return (kelvin - 273.15) * 9/5 + 32


# Example usage
if __name__ == "__main__":
    # Convert 0°C to Fahrenheit
    result1 = convert_temperature(0, celsius_to_fahrenheit)
    print(f"0°C = {result1}°F")
    
    # Convert 98.6°F to Celsius
    result2 = convert_temperature(98.6, fahrenheit_to_celsius)
    print(f"98.6°F = {result2}°C")
    
    # Convert 300K to Celsius
    result3 = convert_temperature(300, kelvin_to_celsius)
    print(f"300K = {result3}°C")