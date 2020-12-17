def fg(string, col):
    return(colors[col] + string + colors["res"])

def bfg(string, fgcol, bgcol):
    return(colors[fgcol] + bg_colors[bgcol] + string + colors["res"])

colors = {"bla" : "\u001b[30m",
          "red" : "\u001b[31m",
          "gre" : "\u001b[32m",
          "yel" : "\u001b[33m",
          "blu" : "\u001b[34m",
          "mag" : "\u001b[35m",
          "cya" : "\u001b[36m",
          "whi" : "\u001b[37m",
          "res" : "\u001b[0m" }

bg_colors = {"bla" : "\u001b[40m",
          "red" : "\u001b[41m",
          "gre" : "\u001b[42m",
          "yel" : "\u001b[43m",
          "blu" : "\u001b[44m",
          "mag" : "\u001b[45m",
          "cya" : "\u001b[46m",
          "whi" : "\u001b[47m",
          "res" : "\u001b[0m" }
          
