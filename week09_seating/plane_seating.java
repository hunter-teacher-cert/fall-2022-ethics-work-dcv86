// Collaobrators: Dave Ciolino-Volano and Maxwell Yearwood

public class Airplane {
  
  // STEP #1
  //Create airplane seats
  int [][] seats = new int[21][6];

  
  //STEP #2
  // Initialize airplane seats : empty = 0
  public void initializeAllSeats()
  {
    for(int [] seat : seats)
      {
        for(int col = 0; col < seat.length; col++)
          {
            seat[col]= 0;
          }
      }
  }

   //STEP #3
  // Randomly Fills the first 10 seats with Economy Plus passengers with probability 90% of the time
  // on the basis of previous seasonal studies
  // Seats assigned at time of ticket purchase

  public void randomFillEconomyPlus()
  {
    for (int row = 0; row < 10; row++)
      {
        for (int col= 0 ;col < seats[row].length; col++)
          {
            if (Math.random() < 0.9)
            {
              seats[row][col] = 1;
            }
          }
      }
  }
  
 // STEP #4
  // Randomly fill block of 4 economy passengers with probability 66.75% for rows 11 to 12 on the basis of previous 
  // seasonsal studies
  // Assigned seats at time of puchase
  
  public void fillBlockOfFourEconomy()
  {
    for (int row = 10; row < 12; row++)
      {
        for (int col= 0 ;col < seats[row].length-4; col++)
          {
            if (Math.random() < 0.6675)
            {
              seats[row][col] = 1;
              seats[row][col + 1] = 1;
              seats[row][col + 2] = 1;
              seats[row][col +3] = 1;
            }
          }
      }
  }


  // STEP #5
  // Randomly fill block of 3 economy passengers with probability 75% for rows 13 to 15 on the basis of previous 
  // seasonsal studies
  // Assign seats at time of ticket purchase
  public void fillBlockOfThreeEconomy()
  {
    for (int row = 12; row < 15; row++)
      {
        for (int col= 0 ;col < seats[row].length - 3; col++)
          {
            if (Math.random() < 0.75)
            {
              seats[row][col] = 1;
              seats[row][col + 1] = 1;
              seats[row][col + 2] = 1;
            }
          }
      }
  }


 //STEP #6
  // Randomly fill block of 2 economy passengers with probability 55.56% for rows 16 to 21 on the basis of previous 
  // seasonsal studies
  // Seats assigned at time of ticket purchase
  
  public void fillBlockOfTwoEconomy()
  {
    for (int row = 15; row <=20; row++)
      {
        for (int col= 0 ;col < seats[row].length - 1; col++)
          {
            if (Math.random() < 0.5556)
            {
              seats[row][col] = 1;
              seats[row][col + 1] = 1;
            }
          }
      }
  }

  // STEP#7: Fill All Remaining Seats with SOLO Travelers
  
public void fillSingleSeats()
  {
    for(int row = 0; row < seats.length; row++)
      {
        for(int col = 0; col < seats[row].length; col++)
          {
            if(seats[row][col] == 0)
            {
              seats[row][col] = 1;
            }
          }
      }
  }
  
 
  
  public void displaySeats()
  {
    System.out.print("\tA \tB \tC \tD \tE \tF \n");
    for(int row = 0; row < seats.length; row++)
      {
       System.out.print(row + 1 + " ");
        for(int seatNum = 0; seatNum < seats[row].length; seatNum++)
          {
            if(seats[row][seatNum] == 1)
            {
              System.out.print("\tX   ");
            }else {
              System.out.print("\t0   ");
            }
          }
        
      }
  }

 
  
  public int countSeatsAvail ()
  {
   int count = 0;
   for (int [] numEmpty : seats)
     {
       for (int j = 0; j < numEmpty.length; j++)
         {
           if(numEmpty[j] == 0)
            {
             count++;
            }
         }
     }
    return count;
  }

  
  public int countTakenSeats()
  {
    int count = 0;
    for (int [] numOnPlane : seats)
      {
        for (int j = 0; j < numOnPlane.length; j++)
          {
            if(numOnPlane[j] == 1)
            {
              count++;
            }
          }
      }
    return count;
  }

 // Did not RUN
  public int seatsAvailInRow(int row)
  {
    int rowSum = 0;
    int rowNum = row - 1;
    int avail;
    for (int [] rowSeats : seats)
      {
        rowSum = 0;
        
        for(int j = 0; j < rowSeats.length; j++)
          {
            rowSum += seats[rowNum][j];
          }
      }
    avail = seats[row].length - rowSum;
    return avail;
  }
  
}
