from flask import Flask
from flask import request

application = Flask(__name__)
app = application

@app.route('/')     # decorator assigning route for index() function
def index():
    celsius = request.args.get("celsius", "")
    return (
        """<form action="" method="get">
                <input type="text" name="celsius">
                <input type="submit" value="Convert">
              </form>"""
        + celsius
    )

@app.route('/<int:celsius>')     # must have different route or FIFO takes place
                                 # can check for data type and pass into function with <>
def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    fahrenheit = float(celsius) * 9 / 5 + 32
    fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
    return str(fahrenheit)

if __name__ == "__main__":
    celsius = input("Celsius: ")
    print("Fahrenheit:", fahrenheit_from(celsius))