from ROOT import *
import os
import math
import argparse



hDecay        = TH1D("hDecay"       , "Decay      Kinetic Energy [MeV]", 40, 0, 1000); 
hHadElastic   = TH1D("hHadElastic"  , "HadElastic Kinetic Energy [MeV]", 40, 0, 1000); 
hInelastic    = TH1D("hInelastic"   , "Inelastic  Kinetic Energy [MeV]", 40, 0, 1000); 
hThroughgoing = TH1D("hThroughgoing", "Througoing Kinetic Energy [MeV]", 40, 0, 1000); 

nEvents = 0
nDecayAtRest = 0
nDecayInFlight = 0

f = TFile.Open("TrueXSKaon.root")
tree = f.Get("TruthTeller/effTree")
for event in tree :
      fKE = event.finalKE
      if nEvents % 10000 == 0:
            print nEvents
      if fKE > -10:
            nEvents +=1
            process =  event.G4Process.data()
            if process == "Decay":
                  hDecay     .Fill(fKE)
                  if fKE < 50:
                        nDecayAtRest+=1
                  else:
                        nDecayInFlight+=1

            elif process == "hadElastic":
                  hHadElastic.Fill(fKE)
            elif process == "kaon+Inelastic":
                  hInelastic .Fill(fKE)
            elif process == "throughgoing":
                  hThroughgoing.Fill(fKE)    

print "Decay at rest:   ",nDecayAtRest  , 100.*nDecayAtRest/(nDecayAtRest+nDecayInFlight)   ," % of decays"
print "Decay in flight: ",nDecayInFlight, 100.*nDecayInFlight/(nDecayAtRest+nDecayInFlight)," % of decays"

c1=TCanvas("c1" ,"Data" ,200 ,10 ,500 ,500) 
c1.SetGrid ()

s = THStack("s", "Interaction Type Per True Energy Bin normalized by total number of interactions; True K.E. [MeV]; Normalized Number of Interactions");

hHadElastic.SetFillColor(2)
hInelastic .SetFillColor(3)
hDecay     .SetFillColor(4)
hThroughgoing.SetFillColor(5)

hHadElastic.Scale(1./nEvents)
hInelastic .Scale(1./nEvents)
hDecay     .Scale(1./nEvents)
hThroughgoing.Scale(1./nEvents)


s.Add(hHadElastic);
s.Add(hInelastic );
s.Add(hDecay     );
s.Add(hThroughgoing);
s.Draw("");
s.GetYaxis().SetTitleOffset(1.4)
c1.Update()

legend = TLegend(.44,.52,.74,.75)
legend.AddEntry(hHadElastic ,"hadElastic")
legend.AddEntry(hInelastic  ,"K+Inelastic")
legend.AddEntry(hDecay      ,"Decay")
legend.AddEntry(hThroughgoing,"Througoing")
legend.Draw("same")
c1.Update()

outFileRoot    = TFile('InteractionsKaonsBreakdown.root', "RECREATE" )
hHadElastic  .Write()
hInelastic   .Write()
hDecay       .Write()
hThroughgoing.Write()

outFileRoot.Close()


raw_input()  
