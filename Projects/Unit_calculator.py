# Completed using AI

class UnitConverter:
    def convert(self, amount, from_unit, to_unit, category, unit_data):
        # Temperature needs special handling
        if category == "Temperature":
            return self.convert_temperature(amount, from_unit, to_unit)
        # All other categories use ratio-based conversion
        base = unit_data[category][from_unit]
        target = unit_data[category][to_unit]
        return amount * (base / target)
    def convert_temperature(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        # Convert input → Celsius
        if from_unit == "fahrenheit":
            value = (value - 32) * 5 / 9
        elif from_unit == "kelvin":
            value = value - 273.15
        # Convert Celsius → target
        if to_unit == "fahrenheit":
            return (value * 9 / 5) + 32
        elif to_unit == "kelvin":
            return value + 273.15
        else:
            return value

def getinput(unit_data, category):
    units = list(unit_data[category].keys())
    print("\nAvailable units:")
    for i, u in enumerate(units, 1):
        print(f"{i}. {u}")
    try:
        fromunit = int(input("Enter unit number FROM: "))
        tounit = int(input("Enter unit number TO: "))
        amount = float(input("Enter amount: "))
        if not (1 <= fromunit <= len(units)) or not (1 <= tounit <= len(units)):
            print("Invalid unit number")
            return None
        return units[fromunit - 1], units[tounit - 1], amount
    except ValueError:
        print("Invalid input type")
        return None
    
unit_data = {
    "Length": {
        "meter": 1,
        "kilometer": 1000,
        "centimeter": 0.01,
        "millimeter": 0.001,
        "inch": 0.0254,
        "foot": 0.3048,
        "yard": 0.9144,
        "mile": 1609.344
    },
    "Weight": {
        "kilogram": 1,
        "gram": 0.001,
        "milligram": 0.000001,
        "pound": 0.453592,
        "ounce": 0.0283495,
        "ton": 1000
    },
    "Time": {
        "second": 1,
        "minute": 60,
        "hour": 3600,
        "day": 86400,
        "week": 604800,
        "month": 2628000,
        "year": 31536000
    },
    "Area": {
        "square_meter": 1,
        "square_kilometer": 1_000_000,
        "square_centimeter": 0.0001,
        "hectare": 10000,
        "acre": 4046.8564224,
        "square_foot": 0.092903,
        "square_yard": 0.836127
    },
    "Volume": {
        "liter": 1,
        "milliliter": 0.001,
        "cubic_meter": 1000,
        "cubic_centimeter": 0.001,
        "gallon": 3.78541,
        "quart": 0.946353,
        "pint": 0.473176
    },
    "Speed": {
        "meter_per_second": 1,
        "kilometer_per_hour": 0.277778,
        "mile_per_hour": 0.44704,
        "foot_per_second": 0.3048,
        "knot": 0.514444
    },
    "Temperature": {
        "celsius": "C",
        "fahrenheit": "F",
        "kelvin": "K"
    }
}

category_map = {
    1: "Length",
    2: "Weight",
    3: "Time",
    4: "Area",
    5: "Volume",
    6: "Speed",
    7: "Temperature"
}

obj = UnitConverter()
while True:
    print("\n=== UNIT CONVERTER ===")
    print("1.Length\n2.Weight\n3.Time\n4.Area\n5.Volume\n6.Speed\n7.Temperature\n8.Exit")
    try:
        category = int(input("Enter category number: "))
        if category == 8:
            print("Goodbye!")
            break
        if category not in category_map:
            print("Invalid category")
            continue
        cat_name = category_map[category]
        result = getinput(unit_data, cat_name)
        if not result:
            continue
        fromunit, tounit, amount = result
        answer = obj.convert(amount, fromunit, tounit, cat_name, unit_data)
        print(f"\nResult: {answer}")
    except ValueError:
        print("Please enter a valid number")