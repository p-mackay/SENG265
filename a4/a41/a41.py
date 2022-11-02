#!/usr/bin/env python3
'''Assignment 4 Part 1 template'''
print(__doc__)

from typing import IO

class ProEpilogue:
    '''ProEpilogue class'''
    def __init__(self, f: IO[str]):
        self.f: IO[str] = f 

    def writeHTMLline(self, t: int, line: str):
         '''writeLineHTML method'''
         ts: str  = "   " * t
         self.f.write(f"{ts}{line}\n")

    def writeHTMLHeader(self, winTitle: str):
        '''writeHeadHTML method'''
        self.writeHTMLline(0, "<html>")
        self.writeHTMLline(0, "<head>")
        self.writeHTMLline(1, f"<title>{winTitle}</title>")
        self.writeHTMLline(0, "</head>")
        self.writeHTMLline(0, "<body>")

    def writeHTMLcomment(self, t: int, com: str):
        '''writeHTMLcomment method'''
        ts: str = "   " * t
        self.f.write(f'{ts}<!--{com}-->\n')

    def openSVGcanvas(self, t: int, canvas: tuple):
         '''openSVGcanvas method'''
         ts: str = "   " * t
         self.writeHTMLcomment(t, "Define SVG drawing box")
         self.f.write(f'{ts}<svg width="{canvas[0]}" height="{canvas[1]}">\n')

    def closeSVGcanvas(self, t: int):
        '''closeSVGcanvas method'''
        ts: str = "   " * t
        self.f.write(f'{ts}</svg>\n')
        self.f.write(f'</body>\n')
        self.f.write(f'</html>\n')

    def writeHTMLfile(self):
        '''writeHTMLfile method'''
        h = ProEpilogue(self.f)
        c = Circle((50,50,50),(255,0,0,1.0))
        r = Rectangle((50,50,50,50), (0,230,23,1.0))

        h.writeHTMLHeader("My Art")
        h.openSVGcanvas(1, (550, 350))
        r.drawRectangleLine(self.f, 2, r)
        r.genArt(self.f, 2)
        c.drawCircleLine(self.f, 2, c)
        c.genArt(self.f, 2)
        h.closeSVGcanvas(1)

class Rectangle:
    '''Rectangle class'''
    def __init__(self, rec: tuple, col: tuple):
        self.x: int = rec[0]
        self.y: int = rec[1]
        self.wid: int = rec[2]
        self.hei: int = rec[3]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]

    def drawRectangleLine(self, f: IO[str], t: int, r: 'Rectangle'):
        '''drawRectangle method'''
        ts: str = "   " * t
        line: str = f'<rect x="{r.x}" y="{r.y}" width="{r.wid}" height="{r.hei}" fill="rgb({r.red}, {r.green}, {r.blue})" fill-opacity="{r.op}"></rect>'
        f.write(f"{ts}{line}\n")

    def genArt(self, f: IO[str], t: int):
       '''genART method'''
       self.drawRectangleLine(f, t, Rectangle((50,50,50,50), (0,230,23,1.0)))
       self.drawRectangleLine(f, t, Rectangle((250,150,150,150), (255,0,230,1.0)))
       self.drawRectangleLine(f, t, Rectangle((150,150,150,150), (0,0,230,1.0)))
       self.drawRectangleLine(f, t, Rectangle((50,250,200,300), (255,0,0,1.0)))
       self.drawRectangleLine(f, t, Rectangle((150,250,500,500), (100,205,0,1.0)))
       self.drawRectangleLine(f, t, Rectangle((250,250,50,200), (255,0,255,1.0)))
       self.drawRectangleLine(f, t, Rectangle((350,250,50,200), (255,0,0,1.0)))
       self.drawRectangleLine(f, t, Rectangle((450,250,50,100), (255,0,255,1.0)))

class Circle:
    '''Circle class'''
    def __init__(self, cir: tuple, col: tuple):
        self.cx: int = cir[0]
        self.cy: int = cir[1]
        self.rad: int = cir[2]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]

    def drawCircleLine(self, f: IO[str], t: int, c: 'Circle'):
        '''drawCircle method'''
        ts: str = "   " * t
        line: str = f'<circle cx="{c.cx}" cy="{c.cy}" r="{c.rad}" fill="rgb({c.red}, {c.green}, {c.blue})" fill-opacity="{c.op}"></circle>'
        f.write(f"{ts}{line}\n")

    def genArt(self, f: IO[str], t: int):
       '''genART method'''
       self.drawCircleLine(f, t, Circle((50,50,50), (255,0,0,1.0)))
       self.drawCircleLine(f, t, Circle((150,50,50), (255,255,0,1.0)))
       self.drawCircleLine(f, t, Circle((250,150,50), (255,0,255,1.0)))
       self.drawCircleLine(f, t, Circle((350,50,50), (255,0,0,1.0)))
       self.drawCircleLine(f, t, Circle((450,50,50), (255,0,0,1.0)))
       self.drawCircleLine(f, t, Circle((50,250,50), (255,0,0,1.0)))
       self.drawCircleLine(f, t, Circle((150,250,50), (255,255,0,1.0)))
       self.drawCircleLine(f, t, Circle((250,250,50), (255,0,255,1.0)))
       self.drawCircleLine(f, t, Circle((350,250,50), (255,0,0,1.0)))
       self.drawCircleLine(f, t, Circle((450,250,50), (255,0,255,1.0)))

def main():

    '''main method'''
    fnam: str = "a41.html"
    f: IO[str] = open(fnam, "w")
    h = ProEpilogue(f)
    h.writeHTMLfile()


main()
