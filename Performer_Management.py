def get_band_name(name):
    if len(name) > 3 and len(name) < 20:
        return "Hello " + name + "."
    else:
        return "Please input a proper band name."

bandName = ""
while get_band_name() == "Please input a proper band name.":
    bandName = input("Enter band name: ")