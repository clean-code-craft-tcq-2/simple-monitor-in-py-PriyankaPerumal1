import BMS_range
from termcolor import colored

messages = {
  'EN' : {
    'Temperature'    : 'Temperature',
    'State of Charge': 'State of Charge',
    'Charge Rate'    : 'Charge Rate',
    'Low'            : 'Low',
    'High'           : 'High',
    'Normal'         : 'Normal',
    'Warning'        : 'Warning',
    'Breach'         : 'Breach'
  },
  'DE' : {
    'Temperature'    : 'Temperatur',
    'State of Charge': 'Ladezustand',
    'Charge Rate'    : 'Ladestrom',
    'Low'            : 'Niedrig',
    'High'           : 'Hoch',
    'Normal'         : 'Normal',
    'Warning'        : 'Warnung',
    'Breach'         : 'Verstoß'
  }
}
class CheckLimit:
  def __init__(self, value, range, Language):
    self.value = value
    self.range = range
    self.messages = messages[Language]
    
  
  def get_min_tolerance(self):
    return self.range.min_limit + ((self.range.max_limit * self.range.tolerance)/100)
  
  def get_max_tolerance(self):
    return self.range.max_limit - ((self.range.max_limit * self.range.tolerance)/100)

  def print_alert_message(self, type_of_breach, parameter):
    print(colored(self.messages['Breach']  + ': ' + type_of_breach + ' ' + parameter, 'red'))
  
  def print_warning_message(self, type_of_warning, parameter):
    print(colored(self.messages['Warning'] + ': ' + type_of_warning + ' ' + parameter, 'yellow'))

  def print_normal_message(self, parameter):
    print(colored(self.messages['Normal']  + ': ' + parameter, 'green'))

  def check_limit(self):
    range_ok = False
    if self.value < self.range.min_limit:
      self.print_alert_message(self.messages['Low'], self.messages[self.range.parameter])
    elif self.value > self.range.max_limit:
      self.print_alert_message(self.messages['High'], self.messages[self.range.parameter])
    else:
      range_ok = self.check_warning()
      
    return range_ok
  
  def check_warning(self):
    tolerance_ok = False
    if self.range.check_early_warning and self.value <= self.get_min_tolerance():
      self.print_warning_message(self.messages['Low'], self.messages[self.range.parameter])
    elif self.range.check_early_warning and self.value >= self.get_max_tolerance():
      self.print_warning_message(self.messages['High'], self.messages[self.range.parameter])
    else:
      self.print_normal_message(self.messages[self.range.parameter])
      tolerance_ok = True

    return tolerance_ok

    
def battery_is_ok(battery_values, Language):
  within_range = True
  for parameter in battery_values:
      if not CheckLimit(battery_values[parameter], BMS_range.bms_range_dict[parameter], Language).check_limit():
        within_range = False

  return within_range

def test_battery():
  assert(battery_is_ok({"Temperature": 25,"State of Charge": 70,"Charge Rate": 0.7 }, 'EN') is True)
  assert(battery_is_ok({"Temperature": 50,"State of Charge": 85,"Charge Rate": 0 }, 'DE') is False)
  assert(battery_is_ok({"Temperature": 20,"State of Charge": 60,"Charge Rate": 0.9 }, 'EN') is False)
  assert(battery_is_ok({"Temperature": 20,"State of Charge": 60,"Charge Rate": 0.76 }, 'DE') is False)
  assert(battery_is_ok({"Temperature": 1000,"State of Charge": 900,"Charge Rate": 10 }, 'DE') is False)
  assert(battery_is_ok({"Temperature": 25,"State of Charge": 70,"Charge Rate": 0.7 }, 'EN') is True)
  assert(battery_is_ok({"Temperature": 2.25,"State of Charge": 24,"Charge Rate": 0.04 }, 'EN') is False)
  assert(battery_is_ok({"Temperature": 42.75,"State of Charge": 76,"Charge Rate": 0.76 }, 'EN') is False)
  assert(battery_is_ok({"Temperature": 42.74,"State of Charge": 75,"Charge Rate": 0.75 }, 'EN') is True)
  assert(battery_is_ok({"Temperature": 0,"State of Charge": 20,"Charge Rate": 0 }, 'EN') is False)
  assert(battery_is_ok({"Temperature": 45,"State of Charge": 80,"Charge Rate": 0.81 }, 'EN') is False)
  assert(battery_is_ok({"Temperature": 45,"State of Charge": 81,"Charge Rate": 0.80 }, 'EN') is False)

  
if __name__ == '__main__':
    test_battery()

