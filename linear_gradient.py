from math import floor
import re


def is_valid_rgb(rgb: dict) -> bool:
    if len(rgb.items()) != 3:
        if not ("r" in rgb.values() and "g" in rgb.values() and "b" in rgb.values()):
            pattern = re.compile(r"^[a-fA-F0-9]{2}$")
            if not (pattern.match(rgb["r"]) and pattern.match(rgb["g"]) and pattern.match(rgb["b"])):
                return False
    return True


def is_valid_hex(hex: str) -> bool:
    pattern = re.compile(r"^#[a-fA-F0-9]{6}$")
    if pattern.match(hex):
        return True
    return False


def hex2rgb(hex: str) -> tuple:
    if not is_valid_hex(hex):
        return {"r": 0, "g": 0, "b": 0}
    return {"r": int(hex[1:3], 16), "g": int(hex[3:5], 16), "b": int(hex[5:7], 16)}


def rgb2hex(rgb: dict) -> str:
    if not is_valid_rgb(rgb):
        return "#000000"
    return f"#{rgb['r']:02x}{rgb['g']:02x}{rgb['b']:02x}"

    
def linear_gradient(start_hex: str, end_hex: str, n: int):
    s = hex2rgb(start_hex)
    e = hex2rgb(end_hex)

    rgb_gradient = []

    for i in range(0, n):
        r = s["r"] + i/(n-1) * (e["r"]-s["r"])
        g = s["g"] + i/(n-1) * (e["g"]-s["g"])
        b = s["b"] + i/(n-1) * (e["b"]-s["b"])
        rgb_gradient.append({"r": floor(r), "g": floor(g), "b": floor(b)})

    return [rgb2hex(rgb) for rgb in rgb_gradient]

if __name__ == "__main__":
    gradient = linear_gradient("#ffffff", "#000000", 20)