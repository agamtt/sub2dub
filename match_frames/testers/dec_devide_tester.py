from decimal import Decimal, getcontext
getcontext().prec = 28


frames = 93
fps = 25
total_seconds = frames / fps

print("nonimal : total_seconds_f %.100f" % total_seconds)
print("nonimal : int(total_seconds) : %.100f "% int(total_seconds))
print("nonimal : total_seconds - int(total_seconds) : %.100f "% (total_seconds - int(total_seconds)))

total_seconds = Decimal(frames) / Decimal(fps)
print("decimal : total_seconds_f %.100f" % total_seconds)
print("decimal : int(total_seconds) : %.100f "% int(total_seconds))
print("decimal : total_seconds - int(total_seconds) : %.100f "% (total_seconds - int(total_seconds)))