from tkinter import *
from tkinter import ttk


class ConversionAdministrator():
    """
    This class takes in the selected measurement type, unit converting from, value of the converting from unit,
    and the desired converted unit from the user interface. With the inputs, it creates and calls the correct object
    to convert the value and returns the converted value to the interface. 
    """
    def __init__(self, measurementType, convertFromUnit, convertFromValue, convertToUnit):
        self.measurementType = measurementType
        self.convertFromUnit = convertFromUnit
        self.convertFromValue = float(convertFromValue)
        self.convertToUnit = convertToUnit
        self.convertToValue = float(1)
        # Array containing basic conversions for each length combination
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
        # Array containing basic conversions for each time combination
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
        """
        This method determines the measurement type selected and creates
        and calls the corresponding object to convert the unit and return
        the value to the user interface
        """
        # First check if the from and to units are the same. If so return the convertFromValue
        if self.convertFromUnit == self.convertToUnit:
            return self.convertFromValue
        # Checks to see if the user is converting temperature 
        if self.measurementType == 'Temperature':
            # Note that the convertTemperature object does not need a convertList 
            convertTemperature = UnitConverter(self.convertFromUnit, self.convertFromValue, self.convertToUnit, None)
            self.convertToValue = convertTemperature.temperatureConverter()
        # Checks to see if the user is converting length
        elif self.measurementType == 'Length':
            convertLength = UnitConverter(self.convertFromUnit, self.convertFromValue, self.convertToUnit, self.lengthConvertList)
            self.convertToValue = convertLength.lengthConverter()
        # Checks to see if the user is converting time
        elif self.measurementType == 'Time':
            convertTime = UnitConverter(self.convertFromUnit, self.convertFromValue, self.convertToUnit, self.timeConvertList)
            self.convertToValue = convertTime.timeConverter()
        # If none of the options above were selected, return an error
        else:
            return 'Measurment Type could not be determined'
        # Returns the value from the UnitConverter objects 
        return self.convertToValue
        
    
class UnitConverter():
    """
    This class takes in the unit converting from, value of the converting from unit,
    the desired converted unit, and converter list and converts the value to the desired
    unit. Then, it returns the value to the ConversionAdministrator.
    """
    def __init__(self, convertFromUnit, convertFromValue, convertToUnit, convertList):
        self.convertFromUnit = convertFromUnit
        self.convertFromValue = float(convertFromValue)
        self.convertToUnit = convertToUnit
        self.convertToValue = float(1)
        self.convertList = convertList
    
    # Method for converting length
    def lengthConverter(self):        
        # Iterates through each row in the array to find the row that contains the matching convertFrom and To units
        for row in self.convertList:
            # Check if the item in current row's index 0 matches the convertFromUnit and index 2 matches convertToUnit
            if row[0] == self.convertFromUnit and row[2] == self.convertToUnit:
                # If it does, get the base value for converting from and to from the row
                baseFromValue = row[1]
                baseToValue = row[3]
                
                # Perform the calculation using the known conversion ratio to find the convertToValue the user wants
                self.convertToValue = (baseToValue * self.convertFromValue) / baseFromValue
                return self.convertToValue
        # If no row was found containing the convertFromUnit and convertToUnit, return an error
        return 'Could not find {} and {} in the convertList'.format(self.convertFromUnit, self.convertToUnit)
    
    # Method for converting time
    def timeConverter(self):
        # Iterates through each row in the array to find the row that contains the matching convertFrom and To units
        for row in self.convertList:
            # Check if the item in current row's index 0 matches the convertFromUnit and index 2 matches convertToUnit
            if row[0] == self.convertFromUnit and row[2] == self.convertToUnit:
                # If it does, get the base value for converting from and to from the row
                baseFromValue = row[1]
                baseToValue = row[3]
                
                # Perform the calculation using the known conversion ratio to find the convertToValue the user wants
                self.convertToValue = (baseToValue * self.convertFromValue) / baseFromValue
                return self.convertToValue
        # If no row was found containing the convertFromUnit and convertToUnit, return an error
        return 'Could not find {} and {} in the convertList'.format(self.convertFromUnit, self.convertToUnit)
    
    # Method for converting temperature
    def temperatureConverter(self):
        # Checks what the convertFromUnit and convertToUnit is to determine which formula needs to be used
        if self.convertFromUnit == 'Fahrenheit' and self.convertToUnit == 'Celsius':
            # Fahrenheit to Celsius formula
            self.convertToValue = (self.convertFromValue - 32) * (5/9)
            return self.convertToValue
            
        elif self.convertFromUnit == 'Fahrenheit' and self.convertToUnit == 'Kelvin':
            # Fahrenheit to Kelvin formula
            self.convertToValue = ((self.convertFromValue - 32) * (5/9)) + 273.15
            return self.convertToValue
            
        elif self.convertFromUnit == 'Celsius' and self.convertToUnit == 'Fahrenheit':
            # Celsius to Fahrenheit formula
            self.convertToValue = (self.convertFromValue * (9/5)) + 32
            return self.convertToValue
            
        elif self.convertFromUnit == 'Celsius' and self.convertToUnit == 'Kelvin':
            # Celsius to Kelvin formula
            self.convertToValue = self.convertFromValue + 273.15
            return self.convertToValue
            
        elif self.convertFromUnit == 'Kelvin' and self.convertToUnit == 'Celsius':
            # Kelvin to Celsius formula
            self.convertToValue = self.convertFromValue - 273.15
            return self.convertToValue
            
        elif self.convertFromUnit == 'Kelvin' and self.convertToUnit == 'Fahrenheit':
            # Kelvin to Fahrenheit formula
            self.convertToValue = ((self.convertFromValue - 273.15) * (9/5)) + 32
            return self.convertToValue
        # If no matching convertFromUnit and convertToUnit was found, return an error
        else:
            return 'Unable to convert from {} to {}'.format(self.convertFromUnit, self.convertToUnit)

###########################################################################################################
"""
tkinter secion that defines interface layout and widgets
"""


# Function that bridges the interface with the Unit Conversion classes
def calculate(*args):
    # Try block used to convert the unit
    try:
        # Gets the value from the interface's text box and converts it to a float
        convertFromValue = float(fromValue.get())
        # Gets the measurement type selected from the interface's dropdown
        measurementType = selectedMeasurement.get()
        # Gets the convertFromUnit from the interface's dropdown
        convertFromUnit = selectedFromUnit.get()
        # Gets the convertToUnit from the interface's dropdown
        convertToUnit = selectedToUnit.get()
        # Creates an object with the given inputs from the user interface
        convertValue = ConversionAdministrator(measurementType, convertFromUnit, convertFromValue, convertToUnit)
        # sets the returned value to equal the response from the conversionPicker method
        returnedValue = convertValue.conversionPicker()
        # Checks to see if the returned value is a string
        if isinstance(returnedValue, str):
            # If it is a string, it means there was an error and a string should be passed back to the convertToValue label on the interface
            convertToValue.set(returnedValue)
        # If the data type is not a string 
        else:
            # Rounds the value to the nearest second decimal place and passes it to the convertToValue label on the interface
            convertToValue.set(round(returnedValue, 2))
    # If the calculation failed, return an error that the value is invalid
    except ValueError:
        
        convertToValue.set('Invalid entries. Please check selections')

# Unit dictionary used for the dropdown menus
units = {
    'Temperature': ('Fahrenheit', 'Celsius', 'Kelvin'),
    'Length': ('Millimeters', 'Centimeters', 'Meters', 'Kilometers', 'Inches', 'Feet', 'Yards', 'Miles'),
    'Time': ('Seconds', 'Minutes', 'Hours', 'Days', 'Years')
}

# Function that dynamically sets the unitFromDropdown and unitToDropdown menu selections based on what measurement type was selected
def updateDropdownValues(event):
    # Gets the measurementType selected from the drop down
    measurementSelected = selectedMeasurement.get()
    # Using the selected measurement, gets the dictionary values for the correct measurement type and sets the values to the dropdown menus
    unitFromDropdown['values'] = units.get(measurementSelected, ())
    unitToDropdown['values'] = units.get(measurementSelected, ())
    
    # Clears the previous values
    selectedFromUnit.set('')
    selectedToUnit.set('')


# Defines the base components of the tkinter interface
root = Tk()
root.title('Unit Conversion Tool')

# Builds a mainframe to place widgets inside
mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

############# Interface Widgets #############

# Measurement dropdown widget
selectedMeasurement = StringVar(value ='Select measurement type...' )
measurementDropdown = ttk.Combobox(
    mainframe,
    textvariable=selectedMeasurement,
    values=('Temperature', 'Length', 'Time'),
    state='readonly',
    width=25
)
measurementDropdown.grid(column=3, row=1, sticky=W)
measurementDropdown.bind("<<ComboboxSelected>>", updateDropdownValues)

# UnitFrom dropdown widget
selectedFromUnit = StringVar(value = 'Select unit...')
unitFromDropdown = ttk.Combobox(
    mainframe,
    textvariable=selectedFromUnit,
    state='readonly',
    width=25
)
unitFromDropdown.grid(column=3, row=2, sticky=W)


# UnitTo dropdown widget
selectedToUnit = StringVar(value = 'Select unit...')
unitToDropdown = ttk.Combobox(
    mainframe,
    textvariable=selectedToUnit,
    state='readonly',
    width=25
)
unitToDropdown.grid(column=3, row=3, sticky=W)

# convertFromValue Entry widget
convertFromValue = StringVar(value = 'Enter unit value...')
fromValue = ttk.Entry(mainframe, width=20, textvariable=convertFromValue)
fromValue.grid(column=2, row=2, sticky=(W, E))

# convertToValue Label widget
convertToValue = StringVar()
ttk.Label(mainframe, textvariable=convertToValue).grid(column=2, row=3, sticky=W)

# Calculate Button widget
ttk.Button(mainframe, text='Calculate', command=calculate).grid(column=3, row=4, sticky=W)

# '=' sign Label widget
ttk.Label(mainframe, text='=').grid(column=1, row=3, sticky=E)




# Defines the base components of the tkinter interface
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(2, weight=1)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

measurementDropdown.focus()
root.bind("<Return>", calculate)

root.mainloop()