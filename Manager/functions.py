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
        season = Seasons.objects.get(pk=1)
        season.TotalStudents = season.TotalStudents + 1
        season.save()
        return "Operation Successfull!"
    except Exception as ex:
        return "Operation Failed!: " + str(ex)

def decrementTotalStudentsByOne():
    try:
        season = Seasons.objects.get(pk=1)
        if season.TotalStudents > 0:
            season.TotalStudents = season.TotalStudents - 1
            season.save()
        return "Operation Successfull!"
    except Exception as ex:
        return "Operation Failed!: " + str(ex)

def setTotalStudents():
    try:
        season = Seasons.objects.get(pk=1)
        season.TotalStudents = Students.objects.all().count()
        season.save()
        return "Operatioin was Successfull!"
    except Exception as ex:
        return "Operation Failed!: " + str(ex)

def incrementTotalCheckIn():
    try:
        season = Seasons.objects.get(pk=1)
        season.TotalCheckIn = season.TotalCheckIn + 1

        if season.TotalNotCheckIn > 1:
            season.TotalNotCheckIn = season.TotalNotCheckIn - 1

        season.save()
        return "Operation Successfull!"
    except Exception as ex:
        return "Operation Failed!: " + str(ex)

def decrementTotalCheckIn():
    try:
        season = Seasons.objects.get(pk=1)

        season.TotalNotCheckIn = season.TotalNotCheckIn + 1

        if season.TotalCheckIn > 1:
            season.TotalCheckIn = season.TotalCheckIn - 1

        season.save()
        return "Operation Successfull!"
    except Exception as ex:
        return "Operation Failed!: " + str(ex)