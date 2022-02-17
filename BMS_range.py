class BMSRange:
  def __init__(self, parameter, min_limit, max_limit, check_early_warning, tolerance):
    self.parameter = parameter
    self.min_limit = min_limit
    self.max_limit = max_limit
    self.check_early_warning = check_early_warning
    self.tolerance = tolerance

bms_range_dict = {"Temperature":      BMSRange("Temperature",     0,  45,   True, 5),
                  "State of Charge":  BMSRange("State of Charge", 20, 80,   True, 5),
                  "Charge Rate":      BMSRange("Charge Rate",     0,  0.8,  True, 5)}
