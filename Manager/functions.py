from StudentManager.models import Seasons, Students, CurrentSeason

def setCurrentSeason(season):
    season = Seasons.objects.get(SeasonName=season)
    if CurrentSeason.objects.filter(pk=1).exists():
        CurrentSeason.objects.filter(pk=1).update(Season=season)
        CurrentSeason.save
    else:
        CurrentSeason.objects.create(Season=season)
        CurrentSeason.save

def InitializeOtherSeasonValues(Season):
    try:
        season = Seasons.objects.get(SeasonName=Season)
        print(Season)
        print(season)
        total = Students.objects.all().count()
        print(total)
        season.TotalStudents = total
        season.TotalCheckIn = 0
        season.TotalNotCheckIn = total
        season.TotalCheckOut = 0

        setCurrentSeason(Season)

        season.save()
        return "Operation Successfull!"
    except Exception as ex:
        return "Operation Failed: " + str(ex)

def incrementTotalStudentsByOne():
    try:
        cs = CurrentSeason.objects.get(pk=1).Season
        season = Seasons.objects.get(SeasonName=cs)

        season.TotalStudents = season.TotalStudents + 1
        season.save()
        return "Operation Successfull!"
    except Exception as ex:
        return "Operation Failed!: " + str(ex)

def decrementTotalStudentsByOne():
    try:
        cs = CurrentSeason.objects.get(pk=1).Season
        season = Seasons.objects.get(SeasonName=cs)

        if season.TotalStudents > 0:
            season.TotalStudents = season.TotalStudents - 1
            season.save()
        return "Operation Successfull!"
    except Exception as ex:
        return "Operation Failed!: " + str(ex)

def setTotalStudents():
    try:
        cs = CurrentSeason.objects.get(pk=1).Season
        season = Seasons.objects.get(SeasonName=cs)
        season.TotalStudents = Students.objects.all().count()
        season.save()
        return "Operatioin was Successfull!"
    except Exception as ex:
        return "Operation Failed!: " + str(ex)

def incrementTotalCheckIn():
    try:
        print("here 00000")
        print("test : " + str(CurrentSeason.objects.get(pk=1).Season))
        cs = CurrentSeason.objects.get(pk=1).Season
        print(cs)
        print("season : " + str(Seasons.objects.get(SeasonName=cs)))
        season = Seasons.objects.get(SeasonName=cs)
        print('beforemiddle')
        season.TotalCheckIn = season.TotalCheckIn + 1
        print("middel")
        if season.TotalNotCheckIn > 1:
            season.TotalNotCheckIn = season.TotalNotCheckIn - 1

        print("afternoon")
        print('total : ' + str(season.TotalCheckIn))
        season.save()
        return "Operation Successfull!"
    except Exception as ex:
        return "Operation Failed!: " + str(ex)

def decrementTotalCheckIn():
    try:
        cs = CurrentSeason.objects.get(pk=1).Season
        season = Seasons.objects.get(SeasonName=cs)

        season.TotalNotCheckIn = season.TotalNotCheckIn + 1

        if season.TotalCheckIn > 1:
            season.TotalCheckIn = season.TotalCheckIn - 1

        season.save()
        return "Operation Successfull!"
    except Exception as ex:
        return "Operation Failed!: " + str(ex)