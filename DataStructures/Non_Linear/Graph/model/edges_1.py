

edges = [
    ["i","j"],
    ["k","i"],
    ["m","k"],
    ["k","l"],
    ["o","n"]
]

edgesOdev = [
    ["a","b"],
    ["a","c"],
    ["a","d"],
    ["b","e"],
    ["c","z"],
    ["c","f"],
    ["d","f"],
    ["e","z"],
    ["f","z"],
]



graph = {
    "i":["j","k"],
    "j":["i"],
    "k":["i","m","l"],
    "l":["k"],
    "o":["n"],
    "n":["o"]
}