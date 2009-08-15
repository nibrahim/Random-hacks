#!/usr/bin/python
"""Tiny script to create PyCon India id cards using reportlab"""

from reportlab.pdfgen import canvas, textobject, pdfimages
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4


cheight = 8 * cm # Card is 8 cm heigh
cwidth  = cheight * 1.61803399 # Golden section ratio to be pleasing to the eye

ml, mr, mb, mt = 0.25*cm, cwidth - 2.5*cm, 0.25*cm, cheight - 2.5*cm # l,r, b, t Borders

def draw_borders(c):
    """Draws the two borders around the card"""
    c.rect(0,0,cwidth - 2*cm,cheight - 2*cm, stroke = 1 )
    c.roundRect(ml,mb,mr,mt, radius = 5, stroke = 1)

def draw_banner(c):
    """Draws the 'Pycon India 2009' banner and the line below it at
    the top"""
    c.setFont("Helvetica-Bold",15)
    c.drawCentredString(cwidth/2 -cm, mt - 0.5*cm, "PyCon India 2009")
    c.line(ml + 0.5 *cm,
           mt - cm,
           mr - 0.5 *cm,
           mt - cm)
    
def draw_image(c):
    """Draws the logo image at the correct position"""
    c.drawImage("logo.jpg",cwidth/2 + cm, 0 + cm, width = 3*cm, height = 3*cm, preserveAspectRatio = True)

def write_details(c,name,org,regno):
    """Writes the registration details. Name, org and regno with
    correct fonts and sizes"""
    t = c.beginText()
    t.setTextOrigin(ml + 0.5*cm,mt - 2* cm)
    t.setFont("Times-Bold",14)
    t.textLine(name)
    t.setFont("Times-Roman",14)
    t.textLine(org)
    t.moveCursor(0,14*2.5)
    t.setFont("Times-Italic",50)
    t.setFillColorRGB(0.7,0.7,0.7)
    t.textLine(regno)
    c.drawText(t)
    
def main(name,org,regno):
    """Function that calls the correct drawing routines (Expects three
    strings name, organisation and registration number)"""
    c = canvas.Canvas("id0.pdf", bottomup = 1, pagesize = A4)
    c.translate(2*cm,2*cm)
    draw_borders(c)
    draw_banner(c)
    draw_image(c)
    write_details(c,name,org,regno)
    c.showPage()
    c.save()

if __name__ == "__main__":
    main("Name of delegate","Organisation might be a long string?","42")
