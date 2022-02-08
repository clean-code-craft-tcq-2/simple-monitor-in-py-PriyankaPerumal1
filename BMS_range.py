class BMSRange:
  def __init__(self, parameter, min_limit, max_limit):
    self.parameter = parameter
    self.min_limit = min_limit
    self.max_limit = max_limit

temperature_range = BMSRange("Temperature",0, 45)
soc_range = BMSRange("State of Charge",20, 80)
charge_rate_range = BMSRange("Charge Rate",0, 0.8)
