
from Examen import clear_display
from tkinter import *
import parser #me permite tomar la expresion y evaluarla
ventana =Tk()
ventana.title("Calculadora")# titulo
display=Entry(ventana)
display.grid(row=1, columnspan=6, sticky=W+E)
i=0
class Calculadora:
    #--funcion añadir numero
    def get_numbers(self,n):
        global i
        display.insert(i, n)
        i+=1
    #--funcion añadir operadores
    def get_operation(self,operator):
        global i
        operator_length= len(operator)#guardamosla longuitud delopertor 
        display.insert(i, operator)#añadimos en pantalla  
        i+=operator_length
        
        #--funcion limpiar
    def clear_display():
        display.delete(0, END)

#--funcion para quitar solo un elemento        
    def undo():
        display_state=display.get()#obtenemos el estado actual de la pantalla
        if len(display_state):#comprovamos la longitud
            display_new_state=display_state[:-1]#eliminamos el ultimo elemento de array
            clear_display()#limpio la pantalla  
            display.insert(0, display_new_state)#le mostramos devuelta al input 
        else:
            clear_display() 
            display.insert(0, 'ERROR')
#-----calcular------
    def calcular(self):
        display_state=display.get()
        try:
            self.math_expression=parser.expr(display_state).compile()
            self.result=eval(self.math_expression)
            clear_display()#limpiamos la pantalla 
            self.display.insert(0, self.result)#mostramos el resultado
        except expression as identifier:
            clear_display()
            display.insert(0, 'ERROR')

    
#-----declaramos nuestro objeto------        
calculadora=Calculadora()
#--creamos los botones
Button(ventana, text="1", command=lambda:calculadora.get_numbers(1)).grid(row=2, column=0)
Button(ventana, text="2", command=lambda:calculadora.get_numbers(2)).grid(row=2, column=1)
Button(ventana, text="3", command=lambda:calculadora.get_numbers(3)).grid(row=2, column=2)

Button(ventana, text="4", command=lambda:calculadora.get_numbers(4)).grid(row=3, column=0)
Button(ventana, text="5", command=lambda:calculadora.get_numbers(5)).grid(row=3, column=1)
Button(ventana, text="6", command=lambda:calculadora.get_numbers(6)).grid(row=3, column=2)

Button(ventana, text="7", command=lambda:calculadora.get_numbers(7)).grid(row=4, column=0)
Button(ventana, text="8", command=lambda:calculadora.get_numbers(8)).grid(row=4, column=1)
Button(ventana, text="9", command=lambda:calculadora.get_numbers(9)).grid(row=4, column=2)

#-------botones adicionales
Button(ventana, text="0", command=lambda:calculadora.get_numbers(0)).grid(row=5, column=1)
Button(ventana, text="AC", command=lambda:calculadora.clear_display()).grid(row=5, column=2)
Button(ventana, text="=", command=lambda:calculadora.calcular()).grid(row=5, column=0)
#Button(ventana, text="/").grid(row=5, column=2)
#-------botones para las operaciones--
Button(ventana, text="/", command=lambda:calculadora.get_operation("/")).grid(row=2, column=5, sticky=W+E)
Button(ventana, text="+", command=lambda:calculadora.get_operation("+")).grid(row=3, column=4, sticky=W+E)
Button(ventana, text="*", command=lambda:calculadora.get_operation("*")).grid(row=4, column=4, sticky=W+E)
Button(ventana, text="-", command=lambda:calculadora.get_operation("-")).grid(row=5, column=4, sticky=W+E)
Button(ventana, text="←", command=lambda:calculadora.undo()).grid(row=2, column=4, sticky=W+E)
ventana.mainloop()