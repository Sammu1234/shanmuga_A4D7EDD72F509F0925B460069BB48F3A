def cgpaCalculator():
  TotalScoreOfferable = 0
  obtainedGrade = 0
  numberOfCourses = int(input("Please Enter the number of Courses you Offered: "))
  print ("**********************************")
  for x in range(numberOfCourses):
    Course1 = input("Enter The Course code of the  course you took:")
    unit = int(input ("How many Unit is the Course you took: "))
    score = int(input("Please Enter your Score:"))
    print ("*********************************")
    TotalScoreOfferable += unit* 5
    if (score >= 70):
      grade = 5
    elif(score < 70 and  score >= 60):
      grade = 4 
    elif(score < 60 and  score >= 50 ):
      grade = 3
    elif(score < 50 and  score >=45):
      grade = 2
    elif (score < 45 and  score>=40):
      grade = 1
    else :
      grade = 0 


    obtainedGrade += unit*grade

  Cgpa =float((obtainedGrade / TotalScoreOfferable) * 5)
  print("THANKS FOR ALL YOUR INPUT YOUR CGPA IS : " + str(Cgpa))


cgpaCalculator()