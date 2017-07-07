import gps

# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)


while True:
    try:
        report = session.next()
        # Wait for a 'TPV' report and display the current time
        # To see all report data, uncomment the line below
        # print report
        if report['class'] == 'TPV':
<<<<<<< HEAD
            if hasattr(report, 'lon'):
                print report.lon
=======
            if hasattr(report, 'lat'):
                print report.lat
>>>>>>> 20c6e4e85556d31305bc51a1479e56b43ab162e8
    except KeyError:
        pass
    except KeyboardInterrupt:
        quit()
    except StopIteration:
        session = None
        print "GPSD has terminated"
