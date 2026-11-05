times = '1h 45m,360s,25m,30m 120s,2h 60s'
half = times.split(',')
print(half)

total = 0

for schet in half:
    print(schet)
    secondschet = schet.split()

    for part in secondschet:
        if 'h' in part:
            print('о часики')
            hours = int(part.replace('h', ''))
            total = total + hours * 60

        if 'm' in part:
            minutes = int(part.replace('m', ''))
            total = total + minutes

        if 's' in part:
            seconds = int(part.replace('s', ''))
            total = total + seconds // 60

print(total)