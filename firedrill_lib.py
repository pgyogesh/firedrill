def get_config():
    var={}
    with open("config.txt","r") as file:
        for line in file:
            line=line.strip()

            k , v = line.split("=")
            var[k]=v
    return var

