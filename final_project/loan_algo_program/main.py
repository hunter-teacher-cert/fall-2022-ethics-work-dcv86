import random
import math

#for our model the location will not matter as much as we are running numbers based off max suggestions for budgeting.  It is impossible to ignore the impact of ones living location on their cost of living, their salary, and relative housing prices, but for our model we are only looking at the overall wealth of individuals based on approval for their first home.
#we are assuming a 10% down payment as people with high credit scores can get approved via FHA loans with 3% down. Also assuming 30 year fixed rate at an APR of 6.53%
#to keep things simple savings are in a high yeilds saving account growing at 3% a year and no stocks or investment outside 401K retirement fund which we are not tracking.  We are only focusing on how home ownership will directly impact wealth so we are trying to keep all other factors minimal and standard based on budgetary suggestions.

#print("They do not have traditional credit, but otherwise have very strong financial management and pay their rent on time and all other bills.  There are two possibilities in our simulation.  Both are random and highlight the disparities in traditional loan approvals.  If a loan algorithm can address these biases then the impact will be huge for those individuals who should have been approved and our society as a whole.  Simulation A is a person whose demographic, espcially their lack of credit, would likely not get approved or approved with a higher rate than someone with a similar demographic, but with some traditional credit. Simulation B is a member of a minority community who are approved at siginificantly lower rates than their white counterparts even with comparable financial profiles.  Our model assumes that a more progressive algorithm will approve our applicant for a loan verse a traditional approvah that would deny them.  Our model will trace each person's financial health and growth overtime.  Then we can compare the impact home laon approval has on possible overall outcomes.")

#steps to code:
#set up our profile and demographic data of applicant--one of two options--1-solid financial management, but no traditional credit--2-member of a minority community that is discriminated against in terms of loan approval

#setup the applicant's profile and overall networth

#our model does not look at utilities and other possible expenses.  We are simulating with perfect savings numbers of 20% and will track payments on the loan ammount for overall networth tracking.  So although per month is less there are other costs to owning a home which may balance out the per month costs, but we are specifically looking at savings and networth which will grow consistently.


#set up initial net worth tracker for each -- post home purchase
class Applicant:
  applicantName = input("what is your name")
  applicantRacePossible = ["black", "hispanic", "asian", "middle eastern"]
  applicantRace = random.choice(applicantRacePossible)
  applicantLGBTQ = random.randint(0, 1)
  applicantAge = random.randint(22, 30)
  applicantSalary = random.randint(45000, 150000)
  applicantRent = round((applicantSalary * .25) / 12, 2)
  print(applicantRent)
  homeCost = applicantSalary * 3.0
  homeValue = homeCost
  downPayment = homeCost * .10
  homeMortgage = round(homeCost - downPayment, 2)
  x = (1.0 + .0054)**360.0
  currentMortgageAmount = homeMortgage
  applicantMortgage = round((homeMortgage * (.0054 * x) / (x - 1)), 2)
  #assumed to have 6 + emergency fund and current savings.  Other net worth is in the downpayment.
  currentSavings = applicantRent * random.randint(3, 9)
  print(currentSavings)
  #netWorth = downPayment + int(currentSavings)
  print(applicantName + " is " + str(applicantAge) +
        " years old.  They earn $" + str(applicantSalary) + " per year.")
  print("They are applying for a $" + str('%.2f' % homeMortgage) +
        " mortgage.")
  print(
    "If purchasing the home their monthly payments on their mortgage will be $ "
    + str(applicantMortgage) +
    ".  If they are renting their monthly payments will be 25% of their current salary, which is currently $"
    + str(applicantRent))
  approvedNetWorth = round(currentSavings + homeCost - homeMortgage, 2)
  print("When approved Dave starts with net worth of $" +
        str(approvedNetWorth))
  deniedNetWorth = round(currentSavings + downPayment, 2)
  deniedCurrentSavings = deniedNetWorth 
  print("When not approved Dave starts with net worth of $" +
        str(deniedNetWorth))
  count = 0
  homeAppreciation = 0
  while count < 5:
    count += 1
    homeAppreciation = homeAppreciation + round(homeValue * .10, 2)
    savingsNew = applicantSalary * .20
    applicantSalary = applicantSalary + (applicantSalary* .03)
    savingsGrowth = currentSavings * .03
    currentSavings = currentSavings + savingsGrowth 
    currentMortgageAmount = currentMortgageAmount - applicantMortgage*12
    approvedUpdatednetWorth = (homeValue + homeAppreciation) + savingsNew + currentSavings - currentMortgageAmount
    print("After " + str(count) + " years, Dave's new Approved networth is: " +
          str('%.2f' % approvedUpdatednetWorth))
    
    savingsNew = applicantSalary * .20
    applicantSalary = applicantSalary + (applicantSalary * .03)
    deniedSavingsGrowth = deniedCurrentSavings * .03
    deniedCurrentSavings = deniedCurrentSavings + deniedSavingsGrowth
    deniedUpdatednetWorth = deniedCurrentSavings + savingsNew
    print("After " + str(count) + " years, Dave's new Denied networth is: " +
          str('%.2f' % deniedUpdatednetWorth))

  print(
    "If Dave is approved for a home his final net worth will be $" + str('%.2f' % approvedUpdatednetWorth) + ". If Dave is denied for a home his final net worth will be $" + str('%.2f' % deniedUpdatednetWorth) +".")
  netWorthdifference = round(approvedUpdatednetWorth - deniedUpdatednetWorth,2)
  print("The difference is $" + str(netWorthdifference) + ".  There are many different factors that can be at play but just in terms of wealth being built via homeownership and its associated appreciation and equity outcomes could not be more staggering.")
  currentSavings = currentSavings + savingsNew
  deniedCurrentSavings = deniedCurrentSavings + savingsNew
  
