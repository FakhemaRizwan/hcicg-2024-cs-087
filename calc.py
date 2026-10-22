w, h, bpp, hz = 1920, 1200, 32, 60

size = w * h * (bpp // 8)
print("Frame size:", size, "B =", round(size / 1048576, 2), "MiB")
print(
    "Bandwidth:",
    size * hz,
    "B/s =",
    round(size * hz / 1048576, 2),
    "MiB/s",
)
print("Aspect:", round(w / h, 4))
dbl = 2 * w * h * 4 + w * h * 4
print("Double buffer + depth:", dbl, "B =", round(dbl / 1048576, 2), "MiB")
