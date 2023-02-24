start = input()

start = start.split(" ")

start_s = start[0]
start_d = int(start[1])

startTime = input()
startTime = startTime.split(" :")
startTimeH = int(startTime[0])
startTimeM = int(startTime[1])
startTimeS = int(startTime[2])

end = input()

end = end.split(" ")

end_s = end[0]
end_d = int(end[1])

endTime = input()
endTime = endTime.split(" :")
endTimeH = int(endTime[0])
endTimeM = int(endTime[1])
endTimeS = int(endTime[2])

second = endTimeS - startTimeS
minute = endTimeM - startTimeM
hour = endTimeH - startTimeH
day = end_d - start_d

if second < 0:
    second = second + 60
    minute = minute - 1
if minute < 0:
    minute = minute + 60
    hour = hour - 1
if hour < 0:
    hour = hour + 24
    day = day - 1

print(day, "dia(s)")
print(hour, "hora(s)")
print(minute, "minuto(s)")
print(second, "segundo(s)")
