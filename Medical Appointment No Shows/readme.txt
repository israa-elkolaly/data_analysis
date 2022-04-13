Dataset Description
This dataset collects information from 100k medical appointments in Brazil and is focused on the question of whether or not patients show up for their appointment.

A number of characteristics about the patient are included in each row:

Gender: (str) F for female and M for male.

ScheduledDay : (str) tells us on what day the patient set up their appointment.

AppointmentDay : (str) the date on which the patient has to show up.

Age : (int64) the patient age in appointment set up day.

Neighbourhood: (str) indicates the location of the hospital.

Scholarship : (int64) [0 or 1] ndicates whether or not the patient is enrolled in Brasilian welfare program Bolsa Família.

Hipertension: (int64) [0,1]

Diabetes : (int64) [0,1]

Alcoholism : (int64) [0,1]

Handcap : (int64) [0,1,2,3,4] Handcap degree

SMS_received : (int64) [0,1]

No-show : (str) No for showing up and yes for not showing up





1- Question(s) for Analysis
Q1 - which gender shows up for thier appointment?
Q2 - Is any disease affect showing up for thier appointment?
Q3 - Is Alcoholism, Handcap degree and Scholarship affect showing up for thier appointment?
Q4 - Is reciving SMS- message affect showing up for thier appointment?
Q5 - Is appointment month/day/hour affect showing up for thier appointment?
Q6 - what age range was most showing up for thier appointment?
Q7 - Is the waiting days affect the patient's show?¶