class power():
  def __init__(self, battery="/proc/pmu/battery_0", general="/proc/pmu/info"):
    self.battery=open(battery)
    self.general=open(general)

  def update(self):
    self.battery.seek(0)
    self.general.seek(0)
    bat_data = self.battery.read()
    gen_data = self.general.read()
    print bat_data, gen_data
    return self.__parse(bat_data), self.__parse(gen_data)

  def release(self):
    self.battery.close()
    self.general.close()

  def __parse(self, data):
    out = {}
    print data
    for line in data.split("\n"):
      if line in ["\n", ""]: 
        print line
        pass
      else:
        print line
        unpacked = line.split(":")
        print unpacked
        key = unpacked[0].strip(" ")
        val = unpacked[1].strip(" ")
        out[key]=val
    return out

