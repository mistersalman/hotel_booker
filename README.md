# hotel_booker

Introduction:
  This project was created as part of the interview process for LA-based Keypr
  
  When working, it will allow for an admin to set a maximum number of rooms (default 100) and overbooking percentage (default 10)
  When working, it will allow for a user to book a reservation for a day, only if the range is valid and available
  

Context:
  This project uses Python with Django and REST.
  I have a decent understanding of Python, but have never touched the latter two. Most of the time spent on this project is admittedly research
  

How to Run:
  My settings:
    I designed this project in PyCharm in order to minimize issues with preparing a virtual environment for Django. I highly encourage you do the same.
    The application, as is, should be able to run out of the box. 'Run' the program and you will be directed to an admin login.
    Here, enter testAdmin as the login and password12 as the password. This will give you superuser access.


#TODO

  -Implement better front-end which allows for users to book multiple days (currently using default; needt o learn how to design this)
  
  -Auto-initialize HotelSetting table with a range of calendar days to choose from (need to study Django more and figure out where 
  
    the SQLite interaction would take place)
    
  -Ipmlement SQLite logic for only allowing valid bookings and update max rooms and overbook rates:
  
    -Default day initialization would be 100 max, 10% overbook; can update any time
    
    -When a range is selected, iterate through each date, and confirm that that that day isn't past the max overbook
    
      #assuming String givenDate is initialized as the current date in the list and bool
      
      int currBook = cursor.execute('SELECT COUNT(*) FROM RESERVATION r, HOTELSETTING h WHERE r.date = h.date AND h.date = (%s)', date)
      
      int maxRms = cursor.execute('SELECT max_rooms FROM HOTELSETTING WHERE date = (%s)', date)
      
      int obpct = cursor.execute('SELECT max_overbook FROM HOTELSETTING WHERE date = (%s)', date)
      
      if(currBook >= int(maxRms * (1 + obpct)))
      
      {
      
        return false;
        
      }
      
      return true;
      
    -If the above function returns true, do the following to update the entry
    
      R1 = {firstname, lastname, email, date)
      
      cursor.execute('INSERT INTO RESERVATION((%s), (%s), (%s), (%s))', R1)
      
    -If one wants to update the max rooms or bookings using rVal and bVal
    
      cursor.execute('UPDATE HOTELSETTING SET max_rooms to rVAL, max_overbook to bVAL WHERE date = (%s)', date)
      
  -Learn how to use REST API calls and integrate that into the project (late-stage)
  
