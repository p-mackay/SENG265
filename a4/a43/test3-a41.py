#!/usr/bin/env python3
'''Assignment 4 Part 3'''
print(__doc__)


from typing import IO
import random
import math

'''ProEpilogue receives a file and writes the headers for HTML open
and SVG open. Also closes the desired HTML and SVG with appropriate whitespace.
Writes a comment above the SVG block.
Writes a title to the output file'''
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
        c = Circle((0,0,0),(0,0,0,0.0))
        r = Rectangle((0,0,0,0), (0,0,0,0.0))

        h.writeHTMLHeader("My Art")
        h.openSVGcanvas(1, (700, 500))
        h.genArt(2)
        h.closeSVGcanvas(1)

class ArtConfig:
    '''ArtConfig class'''
    '''Declaration of validation constants'''
    TABNUM = 1
    FILENAME: str = "SVGArt.html"
    WINART: str = "Python SVG Art"
    H1ART: str = "Python SVG Art"
    SHCNT: int = 0
    CNT: int = 20000 
    CIR: int = 1
    REC: int = 0
    XMIN: int = 0
    YMIN: int = 0 
    XMAX: int = 1920 
    YMAX: int = 1080 

    RADMIN: int = 0
    RADMAX: int = 1000 
    RXMIN: int = XMIN + 10
    RXMAX: int = XMAX - 10
    RYMIN: int = XMIN + 10
    RYMAX: int = XMAX - 10

    WIDMIN: int = 0 
    WIDMAX: int = 1000
    HETMIN: int = 0 
    HETMAX: int = 1000

    REDMIN: int = 0
    REDMAX: int = 255
    GREENMIN: int = 0
    GREENMAX: int = 255
    BLUEMIN: int = 0
    BLUEMAX: int = 255
    OPMIN: float = 0.0
    OPMAX: float = 1.0

class GenRandom:
    '''GenRandom class'''
    '''takes a two numbers, representing a range 
    returns a random number between the range.'''
    def gen_random(mn: int, mx: int):
        '''genRandom method'''
        return random.randrange(mn, mx+1)

'''PyArt constructor receives all the parameters necessary to create a 
HTML file with random SVG shapes(rectangle and circle), sizes, colors, amount of shapes, and
opacity. We create multiple randomly created Circle and Rectangle objects, and
write the information contained in each shape to the specified HTML file. 
So we have one PyArt object which represents a HTML file, that is made up of
many shape objects.'''
class PyArt:
    '''PyArt class'''
    def __init__(self, f: IO[str], win: str, cnt: int, can: tuple, sha: tuple,\
            rad: tuple, rwh: tuple, col: tuple):
        self.f: IO[str] = f
        self.win: str = win
        self.cnt: int = self.is_valid_cnt(cnt)
        self.xmin: tuple = self.is_valid_xcoor(can[0])
        self.xmax: tuple = self.is_valid_xcoor(can[1])
        self.ymin: tuple = self.is_valid_ycoor(can[2])
        self.ymax: tuple = self.is_valid_ycoor(can[3])

        self.sha1: tuple = self.is_valid_sha(sha[0])
        self.sha2: tuple = self.is_valid_sha(sha[1])
        self.radmin: tuple = self.is_valid_rad(rad[0])
        self.radmax: tuple = self.is_valid_rad(rad[1])
        self.widmin: tuple = self.is_valid_rwh(rwh[0])
        self.widmax: tuple = self.is_valid_rwh(rwh[1])
        self.hetmin: tuple = self.is_valid_rwh(rwh[2])
        self.hetmax: tuple = self.is_valid_rwh(rwh[3])
        self.redmin: tuple = self.is_valid_col(col[0])
        self.grmin: tuple = self.is_valid_col(col[1])
        self.blmin: tuple = self.is_valid_col(col[2])
        self.redmax: tuple = self.is_valid_col(col[3]+1)
        self.grmax: tuple = self.is_valid_col(col[4]+1)
        self.blmax: tuple = self.is_valid_col(col[5]+1)
        self.opmin: tuple = self.is_valid_op(col[6])
        self.opmax: tuple = self.is_valid_op(col[7])

    def is_valid_cnt(self, cnt):
        '''is_valid_cnt method'''
        if  cnt < 0 or cnt > ArtConfig.CNT:
            raise ValueError(f"You entered: {cnt}, Shape count must be within 0 < count < 20000.\n")
        return cnt
    
    def is_valid_xcoor(self, xcoor):
        '''is_valid_xcoor method'''
        if  xcoor < ArtConfig.XMIN or xcoor > ArtConfig.XMAX:
            raise ValueError(f"You entered: {xcoor}, X coordinate must be within 0 < xcoor < 1920")
        return xcoor

    def is_valid_ycoor(self, ycoor):
        '''is_valid_ycoor method'''
        if  ycoor < ArtConfig.YMIN or ycoor > ArtConfig.YMAX:
            raise ValueError("X coordinate must be within 0 < ycoor < 1080")
        return ycoor

    def is_valid_sha(self, sha):
        '''is_valid_sha method'''
        if  sha < ArtConfig.REC or sha > ArtConfig.CIR:
            raise ValueError("Two shapes 0 = Rectangle 1 = Circle enter: 0 < sha < 1")
        return sha

    def is_valid_rad(self, rad):
        '''is_valid_rad method'''
        if  rad < ArtConfig.RADMIN or rad > ArtConfig.RADMAX:
            raise ValueError("Radius must be within 0 < rad < 1000")
        return rad

    def is_valid_rwh(self, rwh):
        '''is_valid_rwh method'''
        if  rwh < ArtConfig.WIDMIN or rwh > ArtConfig.WIDMAX:
            raise ValueError(f"You entered: {rwh}, Width and Height must be within 0 < rwh < 1000")
        return rwh

    def is_valid_col(self, col):
        '''is_valid_col method'''
        if  col < ArtConfig.REDMIN or col > ArtConfig.REDMAX+1:
            raise ValueError(f"You entered a value not in the correct range, Color must be within 0 < col < 255")
        return col

    def is_valid_op(self, op):
        '''is_valid_op method'''
        if  op < ArtConfig.OPMIN or op > ArtConfig.OPMAX:
            raise ValueError(f"You entered: {op}, Opacity must be within 0.0 < op < 1.0")
        return op

    def gen_pyart(self):
        '''gen_pyart method'''
        h = ProEpilogue(self.f)
        cir = Circle((0,0,0),(0,0,0,0.0))
        r = Rectangle((0,0,0,0), (0,0,0,0.0))
        h.writeHTMLHeader(self.win)
        h.openSVGcanvas(1, (self.xmax, self.ymax))

        if self.sha1 == 0 and self.sha2 == 0:
            for rec in range(self.cnt):
                r.drawRectangleLine(self.f, 2, Rectangle(\
                        ((GenRandom.gen_random(self.xmin,self.xmax)),\
                        (GenRandom.gen_random(self.ymin,self.ymax)),\
                        (GenRandom.gen_random(self.widmin,self.widmax)),\
                        (GenRandom.gen_random(self.hetmin,self.hetmax))),\
                        ((GenRandom.gen_random(self.redmin,self.redmax)),\
                        (GenRandom.gen_random(self.grmin,self.grmax)),\
                        (GenRandom.gen_random(self.blmin,self.blmax)),\
                        random.uniform(self.opmin, self.opmax))))
            h.closeSVGcanvas(1)
        elif self.sha1 == 1 and self.sha2 == 1:
            for shape in range(self.cnt):
                cir.drawCircleLine(self.f, 2, Circle(\
                        ((GenRandom.gen_random(self.xmin,self.xmax)),\
                        (GenRandom.gen_random(self.ymin,self.ymax)),\
                        (GenRandom.gen_random(self.radmin,self.radmax))),\
                        ((GenRandom.gen_random(self.redmin,self.redmax)),\
                        (GenRandom.gen_random(self.grmin,self.grmax)),\
                        (GenRandom.gen_random(self.blmin,self.blmax)),\
                        random.uniform(self.opmin, self.opmax))))
            h.closeSVGcanvas(1)
        else:
            for shape in range(math.ceil(self.cnt/2)):
                r.drawRectangleLine(self.f, 2, Rectangle(\
                        ((GenRandom.gen_random(self.xmin,self.xmax)),\
                        (GenRandom.gen_random(self.ymin,self.ymax)),\
                        (GenRandom.gen_random(self.widmin,self.widmax)),\
                        (GenRandom.gen_random(self.hetmin,self.hetmax))),\
                        ((GenRandom.gen_random(self.redmin,self.redmax)),\
                        (GenRandom.gen_random(self.grmin,self.grmax)),\
                        (GenRandom.gen_random(self.blmin,self.blmax)),\
                        random.uniform(self.opmin, self.opmax))))
                cir.drawCircleLine(self.f, 2, Circle(\
                        ((GenRandom.gen_random(self.xmin,self.xmax)),\
                        (GenRandom.gen_random(self.ymin,self.ymax)),\
                        (GenRandom.gen_random(self.radmin,self.radmax))),\
                        ((GenRandom.gen_random(self.redmin,self.redmax)),\
                        (GenRandom.gen_random(self.grmin,self.grmax)),\
                        (GenRandom.gen_random(self.blmin,self.blmax)),\
                        random.uniform(self.opmin, self.opmax))))
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

def main():
    '''main method'''
    '''pa1: PyArt = PyArt(file_name, "document title", \
            shapes=5000, canvas=(0, 1000, 0, 500), shapes(0,1), radius(0, 100), \
            rwh=(5, 100, 5, 100), color=(0,0,0, 255, 255, 255, 1.0, 1.0))
    '''
    fnam: str = "Python SVG Art1.html"
    f: IO[str] = open(fnam, "w")
    pa1: PyArt = PyArt(f, "Python SVG Art1", \
            10000, (0, 1920, 0, 1080), (1,0), (0, 200), (1, 500, 5, 50), \
            (0,0,0,255, 255, 255, 0.5, 1.0))

    pa1.gen_pyart()

main()
