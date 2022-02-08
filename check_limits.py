import BMS_range

class CheckLimit:
  def __init__(self, value, range):
    self.value = value
    self.range = range
  
  def check_limit(self):
    withinLimit = False
    if self.value < self.range.max_limit:
      print(self.range.parameter + ' is below minimum limit!')
    elif self.value > self.range.max_limit:
      print(self.range.parameter + ' is exceeding the maximum limit!')
    else:
      withinLimit = True
      
    return withinLimit
  
def battery_is_ok(temperature, soc, charge_rate):
  temperature_check = CheckLimit(temperature, BMSRange.temperature_range)
  soc_check = CheckLimit(soc, BMSRange.soc_range)
  charge_rate_check = CheckLimit(charge_rate, BMSRange.charge_rate_range)
  
  return temperature_check.check_limit() and soc_check.check_limit() and charge_rate_check.check_limit()

def test_battery():
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
  assert(battery_is_ok(20, 60, 0.9) is False)
  
if __name__ == '__main__':
    test_battery()
