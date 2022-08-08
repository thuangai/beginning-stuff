def rectangle(w,h):
    per=(w+h)*2
    area=w*h
    return per, area
dai=int(input('wide in cm '))
cao=int(input('high in cm '))
cv,dt=rectangle(dai,cao)
print(cv ,dt)   