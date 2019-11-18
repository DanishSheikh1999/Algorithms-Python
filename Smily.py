from graphics import *

win = GraphWin("Midpoint Circle", 600, 600)
def midPointCircleDraw(x_centre, y_centre, r,flag):
    x = r
    y = 0

    print("(", x + x_centre, ", ", y + y_centre, ")")

    if r > 0:
        print("({xval}, {yval})".format(xval=x+x_centre, yval=y+y_centre))
        print("(", y + x_centre, ", ", x + y_centre, ")")
        print("(", -y + x_centre, ", ", x + y_centre, ")")

    P = 1 - r
    while x > y:
        y += 1
        if P <= 0:
            P = P + 2 * y + 1
        else:
            x -= 1
            P = P + 2 * y - 2 * x + 1
        if x < y:
            break

        print("(", x + x_centre, ", ", y + y_centre, ")")
        print("(", -x + x_centre, ", ", y + y_centre, ")")
        print("(", x + x_centre, ", ", -y + y_centre, ")")
        print("(", -x + x_centre, ", ", -y + y_centre, ")")
        if flag=='c':
            plotPoints(x + x_centre, y + y_centre)
            plotPoints(-x + x_centre, y + y_centre)
            plotPoints(x + x_centre, -y + y_centre)
            plotPoints(-x + x_centre, -y + y_centre)

        if x != y :
            print("(", y + x_centre, ", ", x + y_centre, ")")
            print("(", -y + x_centre, ", ", x + y_centre, ")")
            print("(", y + x_centre, ", ", -x + y_centre, ")")
            print("(", -y + x_centre, ", ", -x + y_centre, ")")

            plotPoints(y + x_centre, x + y_centre)
            plotPoints(-y + x_centre, x + y_centre)
            if flag == 'c':
                plotPoints(y + x_centre, -x + y_centre)
                plotPoints(-y + x_centre, -x + y_centre)


def getInput():
    x,y,r = [int(x) for x in input("Enter the  coordinates and the radius of the centre: ").split()]
    return x, y, r


def plotPoints(x, y):
    point = Point(x, y)
    point.draw(win)


if __name__ == '__main__':
    #xc, yc, rc = getInput()
    midPointCircleDraw(300, 300, 300,'c')
    midPointCircleDraw(150, 200, 50,'c')
    midPointCircleDraw(450, 200, 50,'c')
    midPointCircleDraw(300, 350, 150, 's')
    win.getMouse()
    win.close()