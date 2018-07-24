from ROOT import *
import os
import math
import argparse

from ROOT import TEfficiency
from ROOT import gStyle , TCanvas , TGraphErrors
from array import array


kineticEnergy = []
crossSec      = []
crossSec_el   = []
crossSec_inel = []
zero          = []





parser = argparse.ArgumentParser()
parser.add_argument("fname"   , nargs='?', default = 'PionPlusG4.txt', type = str, help="insert fileName")
args    = parser.parse_args()
fname   = args.fname

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


title = ""
with open(fname) as f:
    for fLine in f.readlines():
        w = fLine.split()
        if is_number(w[0]):
            runIn    = int(w[0])
            ke       = float(w[1])
            xs_el       = float(w[2])
            xs_in       = float(w[3])
            xstot       = float(w[4])
            kineticEnergy.append(ke)
            crossSec.append(xstot)
            crossSec_el.append(xs_el)
            crossSec_inel.append(xs_in)
            zero.append(0.)
        else:
            if "for" not in fLine: 
                continue
            title =  fLine[9:]




c1=TCanvas("c1" ,"Data" ,200 ,10 ,500 ,500) #make nice
c1.SetGrid ()
#define some data points . . .
x      = array('f', kineticEnergy )
y      = array('f', crossSec)
y_el   = array('f', crossSec_el)
y_inel = array('f', crossSec_inel)
exl    = array('f', zero)
exr    = array('f', zero)


nPoints=len(x)
# . . . and hand over to TGraphErros object
gr      = TGraphErrors ( nPoints , x , y     , exl, exr )
grel    = TGraphErrors ( nPoints , x , y_el  , exl, exr )
grinel  = TGraphErrors ( nPoints , x , y_inel, exl, exr )
gr.SetTitle(title+"; Kinetic Energy [MeV]; Cross Section [barn]")


gr . SetLineWidth(2) ;
grel . SetLineWidth(2) ;
grinel . SetLineWidth(2) ;

gr . SetLineColor(kGreen-2) ;
grel . SetLineColor(kBlue) ;
grinel . SetLineColor(kRed) ;



gr . SetFillColor(0)
grel . SetFillColor(0)
grinel . SetFillColor(0)

gr . Draw ( "APL" ) ;
grel . Draw ( "PLsame" ) ;
grinel . Draw ( "PLsame" ) ;
gr . GetXaxis().SetLimits(0,2000)
gr . GetYaxis().SetRangeUser(0,2.)


legend = TLegend(.44,.70,.84,.89)
legend.AddEntry(gr,"G4 Prediction Tot XS")
legend.AddEntry(grel,"G4 Prediction Elastic XS")
legend.AddEntry(grinel,"G4Prediction Inelastic XS")
legend.Draw("same")

c1 . Update ()



raw_input()  
