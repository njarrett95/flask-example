from flask import Flask
application = Flask(__name__)
app = application

@app.route('/')     # decorator assigning route for index() function
def index():
    return 'Hello there. From Python.'

@app.route('/<celsius>')     # must have different route or FIFO takes place
def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        return str(fahrenheit)
    except ValueError:
        return "invalid input"

if __name__ == "__main__":
    celsius = input("Celsius: ")
    print("Fahrenheit:", fahrenheit_from(celsius))