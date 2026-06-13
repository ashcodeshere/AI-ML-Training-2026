## Original Code

```# Unit Converter

class UnitConverter:  
    def __init__(self):
        pass
    def convertLWTAVS(self,amount,fromunit,tounit,category,unit_data):
        base=unit_data[category][fromunit]
        target=unit_data[category][tounit]
        return amount * (base/target)
    


def getinput(unit_data,category):
    fromunit=int(input("Enter unit no from which you want to convert: "))
    tounit=int(input("Enter unit no to which you want to convert: "))
    amount=float(input("Enter Amount: "))
    if (fromunit>len(unit_data[category]) or fromunit<1) or (tounit>len(unit_data[category]) or tounit<1):
        print("Not a valid unit number")
        return
    return fromunit,tounit,amount

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

obj=UnitConverter()
print("Enter category number which you want to convert: ")
print("1.Length\n2.Weight\n3.Time\n4.Area\n5.Volume\n6.Speed\n7.Temperature")
category=int(input("Enter Number"))
if category==1:
    print("List\n1.Meters\n2.Kilometers\n3.centimeter\n4.millimeter\n5.inch\n6.foot\n7.yard\n8.mile")
    fromunit,tounit,amount=getinput(unit_data,"Length")
    funit=list(unit_data["Length"].keys())
    tunit=list(unit_data["Length"].keys())
    obj.convertLWTAVS(amount,funit[fromunit],tunit[tounit],"Length",unit_data)
elif category==2:
    print("List\n1.kilogram\n2.gram\n3.milligram\n4.pound\n5.ounce\n6.ton")
    fromunit,tounit,amount=getinput(unit_data,"Weight")
    obj.convertLWTAVS(amount,fromunit,tounit,"Weight",unit_data)
elif category==3:
    print("List\n1.second\n2.minute\n3.hour\n4.day\n5.week\n6.month\n7.year")
    fromunit,tounit,amount=getinput(unit_data,"Time")
    obj.convertLWTAVS(amount,fromunit,tounit,"Time",unit_data)
elif category==4:
    print("List\n1.square_meter\n2.square_kilometer\n3.square_centimeter\n4.hectare\n5.acre\n6.square_foot\n7.square_yard")
    fromunit,tounit,amount=getinput(unit_data,"Area")
    obj.convertLWTAVS(amount,fromunit,tounit,"Area",unit_data)
elif category==5:
    print("List\n1.liter\n2.milliliter\n3.cubic_meter\n4.cubic_centimeter\n5.gallon\n6.quart\n7.pint")
    fromunit,tounit,amount=getinput(unit_data,"Volume")
    obj.convertLWTAVS(amount,fromunit,tounit,"Volume",unit_data)
elif category==6:
    print("List\n1.meter_per_second\n2.kilometer_per_hour\n3.mile_per_hour\n4.foot_per_second\n5.knot")
    fromunit,tounit,amount=getinput(unit_data,"Speed")
    obj.convertLWTAVS(amount,fromunit,tounit,"Speed",unit_data)
else:
    print("Not a category")

```