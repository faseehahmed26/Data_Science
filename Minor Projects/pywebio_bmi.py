###Create A bmi calculator application
from pywebio.input import *
from pywebio.output import *
def bmicalculator():
    height=input("Please Enter the height in cm",type='float')
    weight=input("Please Enter the weight in kg",type='float')
    bmi=weight/(height/100)**2
    bmi_output=[(16,"Severley UNderweight"),(18.5,'UnderWeight'),(25,'Normal'),(30,'Overweight'),(35,'Moderately Obese'),(40,'Obese'),(float('inf'),'Extremely Obese')]
    
    for tup1,tup2 in bmi_output:
        if bmi<=tup1:
            put_text('Your BMI is :%.1f and the person is :%s'%(bmi,tup2))
            break
#bmicalculator()
if __name__=='__main__':
    bmicalculator()