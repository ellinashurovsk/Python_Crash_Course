peaks = ["Elbrus", "Narodnaya", "Bolshoi Tkach",
         "Kyzyl-Taiga", "Munku-Sardyk", "Belukha"]

print(peaks[0].upper())
print(f"Great peaks are {peaks[0]}, {peaks[1]}.")
peaks[0] = "Peak Shchurovskogo"
print(peaks)
peaks.append("Elbrus")
print(peaks)
del(peaks[-1])
peaks.insert(0, "Elbrus")
print(peaks)
peaks.pop()
print(peaks)
peaks.pop(0)
print(peaks)
peaks.remove("Narodnaya")
print(peaks)

print(len(peaks))

print(sorted(peaks))
print(peaks)

peaks.sort()
print(peaks)

peaks.reverse()
print(peaks)
