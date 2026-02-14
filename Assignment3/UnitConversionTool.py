from tkinter import *
from tkinter import ttk

class ConversionAdministrator():
    def __init__(self, measurementType, convertFromUnit, convertFromValue, convertToUnit):
        self.measurementType = measurementType
        self.convertFromUnit = convertFromUnit
        self.convertFromValue = float(convertFromValue)
        self.convertToUnit = convertToUnit
        self.convertToValue = float(1)

        self.lengthConvertList = [
            ["Millimeters", 1, "Centimeters", 0.1],
            ["Millimeters", 1, "Meters", 0.001],
            ["Millimeters", 1, "Kilometers", 0.000001],
            ["Millimeters", 1, "Inches", 0.0393701],
            ["Millimeters", 1, "Feet", 0.00328084],
            ["Millimeters", 1, "Yards", 0.00109361],
            ["Millimeters", 1, "Miles", .00000062137],
            ["Centimeters", 1, "Millimeters", 10],
            ["Centimeters", 1, "Meters", 0.01],
            ["Centimeters", 1, "Kilometers", 0.00001],
            ["Centimeters", 1, "Inches", 0.393701],
            ["Centimeters", 1, "Feet", 0.0328084],
            ["Centimeters", 1, "Yards", 0.0109361],
            ["Centimeters", 1, "Miles", 0.0000062137],
            ["Meters", 1, "Millimeters", 1000],
            ["Meters", 1, "Centimeters", 100],
            ["Meters", 1, "Kilometers", 0.001],
            ["Meters", 1, "Inches", 39.3701],
            ["Meters", 1, "Feet", 3.28084],
            ["Meters", 1, "Yards", 1.09361],
            ["Meters", 1, "Miles", 0.000621371],
            ["Kilometers", 1, "Millimeters", 1000000],
            ["Kilometers", 1, "Centimeters", 100000],
            ["Kilometers", 1, "Meters", 1000],
            ["Kilometers", 1, "Inches", 39370.1],
            ["Kilometers", 1, "Feet", 3280.84],
            ["Kilometers", 1, "Yards", 1093.61],
            ["Kilometers", 1, "Miles", 0.621371],
            ["Inches", 1, "Millimeters", 25.4],
            ["Inches", 1, "Centimeters", 2.54],
            ["Inches", 1, "Meters", 0.0254],
            ["Inches", 1, "Kilometers", 0.0000254],
            ["Inches", 1, "Feet", 0.0833333],
            ["Inches", 1, "Yards", 0.0277778],
            ["Inches", 1, "Miles", 0.000015783],
            ["Feet", 1, "Millimeters", 304.8],
            ["Feet", 1, "Centimeters", 30.48],
            ["Feet", 1, "Meters", 0.3048],
            ["Feet", 1, "Kilometers", 0.0003048],
            ["Feet", 1, "Inches", 12],
            ["Feet", 1, "Yards", 0.333333],
            ["Feet", 1, "Miles", 0.000189394],
            ["Yards", 1, "Millimeters", 914.4],
            ["Yards", 1, "Centimeters", 91.44],
            ["Yards", 1, "Meters", 0.9144],
            ["Yards", 1, "Kilometers", 0.0009144],
            ["Yards", 1, "Inches", 36],
            ["Yards", 1, "Feet", 3],
            ["Yards", 1, "Miles", 0.000568182],
            ["Miles", 1, "Millimeters", 1609340],
            ["Miles", 1, "Centimeters", 160934],
            ["Miles", 1, "Meters", 1609.34],
            ["Miles", 1, "Kilometers", 1.60934],
            ["Miles", 1, "Inches", 63360],
            ["Miles", 1, "Feet", 5280],
            ["Miles", 1, "Yards", 1760]
        ]

        self.timeConvertList = [
            ["Seconds", 60, "Minutes", 1],
            ["Seconds", 3600, "Hours", 1],
            ["Seconds", 86400, "Days", 1],
            ["Seconds", 31536000, "Years", 1],
            ["Minutes", 1, "Seconds", 60],
            ["Minutes", 60, "Hours", 1],
            ["Minutes", 1440, "Days", 1],
            ["Minutes", 525600, "Years", 1],
            ["Hours", 1, "Seconds", 3600],
            ["Hours", 1, "Minutes", 60],
            ["Hours", 24, "Days", 1],
            ["Hours", 8760, "Years", 1],
            ["Days", 1, "Seconds", 86400],
            ["Days", 1, "Minutes", 1440],
            ["Days", 1, "Hours", 24],
            ["Days", 365, "Years", 1],
            ["Years", 1, "Seconds", 31536000],
            ["Years", 1, "Minutes", 525600],
            ["Years", 1, "Hours", 8760],
            ["Years", 1, "Days", 365]
        ]
        
    def conversionPicker(self):
        if self.measurementType == 'Temperature':
            convertTemperature = UnitConverter(self.convertFromUnit, self.convertFromValue, self.convertToUnit, None)
            self.convertToValue = convertTemperature.temperatureConverter()
        elif self.measurementType == 'Length':
            convertLength = UnitConverter(self.convertFromUnit, self.convertFromValue, self.convertToUnit, self.lengthConvertList)
            self.convertToValue = convertLength.lengthConverter()
        elif self.measurementType == 'Time':
            convertTime = UnitConverter(self.convertFromUnit, self.convertFromValue, self.convertToUnit, self.timeConvertList)
            self.convertToValue = convertTime.timeConverter()
        else:
            return 'Measurment Type could not be determined'
        return self.convertToValue
        
    
class UnitConverter():
    def __init__(self, convertFromUnit, convertFromValue, convertToUnit, convertList):
        self.convertFromUnit = convertFromUnit
        self.convertFromValue = float(convertFromValue)
        self.convertToUnit = convertToUnit
        self.convertToValue = float(1)
        self.convertList = convertList
        
    def lengthConverter(self):        
        for row in self.convertList:
            if row[0] == self.convertFromUnit and row[2] == self.convertToUnit:
                baseFromValue = row[1]
                baseToValue = row[3]
                
                self.convertToValue = (baseToValue * self.convertFromValue) / baseFromValue
                return self.convertToValue
        return 'Could not find {} and {} in the convertList'.format(self.convertFromUnit, self.convertToUnit)
                
    def timeConverter(self):
        for row in self.convertList:
            if row[0] == self.convertFromUnit and row[2] == self.convertToUnit:
                baseFromValue = row[1]
                baseToValue = row[3]
                
                self.convertToValue = (baseToValue * self.convertFromValue) / baseFromValue
                return self.convertToValue
        return 'Could not find {} and {} in the convertList'.format(self.convertFromUnit, self.convertToUnit)
               
    def temperatureConverter(self):
        if self.convertFromUnit == 'Fahrenheit' and self.convertToUnit == 'Celsius':
            self.convertToValue = (self.convertFromValue - 32) * (5/9)
            return self.convertToValue
        elif self.convertFromUnit == 'Fahrenheit' and self.convertToUnit == 'Kelvin':
            self.convertToValue = ((self.convertFromValue - 32) * (5/9)) + 273.15
            return self.convertToValue
        elif self.convertFromUnit == 'Celsius' and self.convertToUnit == 'Fahrenheit':
            self.convertToValue = (self.convertFromValue * (9/5)) + 32
            return self.convertToValue
        elif self.convertFromUnit == 'Celsius' and self.convertToUnit == 'Kelvin':
            self.convertToValue = self.convertFromValue + 273.15
            return self.convertToValue
        elif self.convertFromUnit == 'Kelvin' and self.convertToUnit == 'Celsius':
            self.convertToValue = self.convertFromValue - 273.15
            return self.convertToValue
        elif self.convertFromUnit == 'Kelvin' and self.convertToUnit == 'Fahrenheit':
            self.convertToValue = ((self.convertFromValue - 273.15) * (9/5)) + 32
            return self.convertToValue
        else:
            return 'Unable to convert from {} to {}'.format(self.convertFromUnit, self.convertToUnit)

def calculate(*args):
    try:
        convertFromValue = float(fromValue.get())
        measurementType = measurement_var.get()
        convertFromUnit = unitFrom_var.get()
        convertToUnit = unitTo_var.get()
        convertValue = ConversionAdministrator(measurementType, convertFromUnit, convertFromValue, convertToUnit)
        returnedValue = convertValue.conversionPicker()
        if isinstance(returnedValue, str):
            convertToValue.set(returnedValue)
        else:
            convertToValue.set(round(returnedValue, 2))
    except ValueError:
        convertToValue.set('Could not calculate value entered')

units = {
    'Temperature': ('Fahrenheit', 'Celsius', 'Kelvin'),
    'Length': ('Millimeters', 'Centimeters', 'Meters', 'Kilometers', 'Inches', 'Feet', 'Yards', 'Miles'),
    'Time': ('Seconds', 'Minutes', 'Hours', 'Days', 'Years')
}

def update_units(event):
    selected_measurement = measurement_var.get()
    unitFromDropdown['values'] = units.get(selected_measurement, ())
    unitToDropdown['values'] = units.get(selected_measurement, ())
    
    # Clear previous selections
    unitFrom_var.set('')
    unitTo_var.set('')



root = Tk()
root.title('Unit Conversion Tool')

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# --- Measurement dropdown ---
measurement_var = StringVar(value ='Select measurement type...' )
measurementDropdown = ttk.Combobox(
    mainframe,
    textvariable=measurement_var,
    values=('Temperature', 'Length', 'Time'),
    state='readonly',
    width=25
)
measurementDropdown.grid(column=3, row=1, sticky=W)
measurementDropdown.bind("<<ComboboxSelected>>", update_units)

# --------------------------------


# --- UnitFrom dropdown ---
unitFrom_var = StringVar(value = 'Select unit...')
unitFromDropdown = ttk.Combobox(
    mainframe,
    textvariable=unitFrom_var,
    state='readonly',
    width=25
)
unitFromDropdown.grid(column=3, row=2, sticky=W)
# --------------------------------


# --- UnitTo dropdown ---
unitTo_var = StringVar(value = 'Select unit...')
unitToDropdown = ttk.Combobox(
    mainframe,
    textvariable=unitTo_var,
    state='readonly',
    width=25
)
unitToDropdown.grid(column=3, row=3, sticky=W)
# --------------------------------


convertFromValue = StringVar(value = 'Enter unit value...')
fromValue = ttk.Entry(mainframe, width=20, textvariable=convertFromValue)
fromValue.grid(column=2, row=2, sticky=(W, E))


convertToValue = StringVar()
ttk.Label(mainframe, textvariable=convertToValue).grid(column=2, row=3, sticky=W)

ttk.Button(mainframe, text='Calculate', command=calculate).grid(column=3, row=4, sticky=W)

ttk.Label(mainframe, text='=').grid(column=1, row=3, sticky=E)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(2, weight=1)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

measurementDropdown.focus()
root.bind("<Return>", calculate)

root.mainloop()