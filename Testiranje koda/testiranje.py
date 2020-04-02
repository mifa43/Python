from graphics import *  # modul za grafiku

def main():
    win = GraphWin("Moj Prozor", 500, 500)  #prozor u kome se crta grafika '500' je visina i sirina
    #win.setBackground('black')  # boja prozora

    pt1 = Point(250, 250)   #pozicija gde ce da se crta
    pt2 = Point(350, 350)   #pozicija 2 

    txt = Text(Point(150, 200), 'Zdravo, kako si? ' )

    ln = Rectangle(pt1, pt2)     #ln je pozicija jedan i dva
    ln.setOutline(color_rgb(255, 100, 50))  #boja linije
    ln.setFill(color_rgb(255, 255, 100))
    ln.draw(win)    # ovo crta liniju
    

    txt.draw(win)
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()



# https://www.youtube.com/watch?v=nYhxBVDW7sM
# ln.setWidth(7)      # debljina linije
#txt = Text(Point(150, 200), 'Zdravo, kako si? ' ) #unos teksta
#txt.draw(win) = ovo je naredba da napise
# setTextColor() = za boju teksta dodaje se rgb
# Line = graficka linija
# Rectangle = kocka
# Circle = krug
# Polygon = kvadrat

#nastavi