class power():
  def __init__(self, battery="/proc/pmu/battery_0", general="/proc/pmu/info"):
    self.battery=battery
    self.general=general

  def printdata(self):
    data = self.update()
    print data["AC Power"], float(data["time rem."])/3600

  def update(self):
    batfile = open(self.battery)
    genfile = open(self.general)
    bat_data = batfile.read()
    gen_data = genfile.read()
    batfile.close()
    genfile.close()
    return dict(self.__parse(bat_data).items() + self.__parse(gen_data).items()) 

  def __parse(self, data):
    out = {}
    for line in data.split("\n"):
      if line in ["\n", ""]: 
        pass
      else:
        unpacked = line.split(":")
        key = unpacked[0].strip(" ")
        val = unpacked[1].strip(" ")
        out[key]=val
    return out

