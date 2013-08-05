class power():
  def __init__(self, battery="/proc/pmu/battery_0", general="/proc/pmu/info"):
    self.battery=battery
    self.general=general

  def printdata(self):
    data = self.__update()
    print data["AC Power"], data["time rem."]

  def __update(self):
    batfile = open(self.battery)
    genfile = open(self.general)
    bat_data = batfile.read()
    gen_data = genfile.read()
    batfile.close()
    genfile.close()
    out = {}
    out =  self.__parse(bat_data).items() + self.__parse(gen_data).items()
    return out

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

