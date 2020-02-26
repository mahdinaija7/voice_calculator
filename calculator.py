import speech_recognition as sr
import time
import sympy
from sympy import Float,Rational


r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

with mic as source :
    while True:
        print("Starting Detection")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print("Transforming Audio To Text")
        try:
            equation=r.recognize_google(audio).lower()
            if equation=="stop":
                break
            else:
                try:
                    result=sympy.sympify(equation)
                    if "/" in str(result):
                        num1,num2=list(map(int,str(result).split("/")))
                        result=Float(Rational(num1,num2),2)
                    print(result)
                except SyntaxError:
                    print("Invalid Equation Try Again")
        except :
            pass
        time.sleep(0.2)
print("existing program")