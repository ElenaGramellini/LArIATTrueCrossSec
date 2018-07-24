# LArIATTrueCrossSec
Please, read this readme in your terminal... I swear it looks better than this... 

This folder contains the following:
0. (Note for future Elena) In order to produce the tables, do 
	- source /grid/fermiapp/larsoft/products/setup
	- cd /lariat/app/users/elenag/Hans/G4HadStudies-install/bin
	- setup root v6_08_06g -q debug:e14:nu
	- setup geant4 v4_10_1_p03f -q debug:e14 
	- g4had Kaon+_QGSP_BERT_000.in 
1. the tables for the Geant4.10.1.p3 cross section for PiMinus and KPlus on Argon ( KaonPlusG4.txt  PionMinusG4.txt)
2. the cross section resulting from the application of the sliced TPC method on true quantities (true energy deposition with simIDE and fix slice length of 0.47 cm)
  (TrueXSKaon.root TrueXSPion.root)
3. scripts to plot the comparispn (G4XSKaons.py	    G4XSPions.py)

A bit more details in what follows...


1. Table are from  Geant4.10.1.p3. 
Geant4 version Name: geant4-10-01-patch-03    (5-February-2016)
       	       	     Copyright : Geant4 Collaboration
		     Reference : NIM A 506 (2003), 250-303
		     WWW : http://cern.ch/geant4

The following models are applied
---------------------------------------------------
                           Hadronic Processes for pi-
  Process: pi-Inelastic
        Model:                      QGSP: 12 GeV ---> 100 TeV
        Model:                      FTFP: 9.5 GeV ---> 25 GeV
        Model:            BertiniCascade: 0 eV  ---> 9.9 GeV
     Cr_sctns:      G4CrossSectionPairGG: 0 eV  ---> 100 TeV
                         G4CrossSectionPairGG: G4PiNuclearCrossSection cross sections 
                           below 91 GeV, Glauber-Gribov above 
     Cr_sctns:      G4CrossSectionPairGG: 0 eV  ---> 100 TeV
                         G4CrossSectionPairGG: G4PiNuclearCrossSection cross sections 
                           below 91 GeV, Glauber-Gribov above 
     Cr_sctns:          GheishaInelastic: 0 eV  ---> 100 TeV

  Process: hadElastic
        Model:              hElasticLHEP: 0 eV  ---> 1.0001 GeV
        Model:           hElasticGlauber: 1 GeV ---> 100 TeV
     Cr_sctns:       Barashenkov-Glauber: 0 eV  ---> 100 TeV
     Cr_sctns:            GheishaElastic: 0 eV  ---> 100 TeV

  Process: hBertiniCaptureAtRest


---------------------------------------------------
                           Hadronic Processes for kaon+

  Process: kaon+Inelastic
        Model:                      QGSP: 12 GeV ---> 100 TeV
        Model:                      FTFP: 9.5 GeV ---> 25 GeV
        Model:            BertiniCascade: 0 eV  ---> 9.9 GeV
     Cr_sctns:  ChipsKaonPlusInelasticXS: 0 eV  ---> 100 TeV
     Cr_sctns:          GheishaInelastic: 0 eV  ---> 100 TeV

  Process: hadElastic
        Model:              hElasticLHEP: 0 eV  ---> 100 TeV
     Cr_sctns:            GheishaElastic: 0 eV  ---> 100 TeV

---------------------------------------------------


2. Files are generated with the module TrueXS_module.cc on the feature/elenag_Sim branch. These root files contain only MC truth information.
The interesting plots are:
TH1D	h_DXUniform             Uniform lenght of 0.47 cm along the particle trajectory (Algorithm cross check) [cm]
TH1D	h_DEUniform             Integrated energy deposition from simIDE over the uniform lenght of 0.47 cm along the particle trajectory [MeV]
TH1D	h_DEDEXUniform  	dE/dX of previous 2 quantities [MeV/cm]
TH1D	hInitialPz		Pz @ WC4 [MeV/c]
TH1D	hInitialKE		Kinetic Energy @ WC4 [MeV]
TH1D	hKEAtTPCFF		Kinetic Energy @ TPC Front Face [MeV]
TH1D	hIncidentKE		Incident Kinetic Energy [MeV]                     -- Info from sum of true energy deposition (simIDE)
TH1D	hInteractingKE		Interacting Kinetic Energy for Total XS     [MeV] -- Info from sum of true energy deposition (simIDE)
TH1D	hInteractingKEEl	Interacting Kinetic Energy for Elastic XS   [MeV] -- Info from last trajectory point
TH1D	hInteractingKEElDep	Interacting Kinetic Energy for Elastic XS   [MeV] -- Info from sum of true energy deposition (simIDE)
TH1D	hInteractingKEInel	Interacting Kinetic Energy for Inelastic XS [MeV] -- Info from sum of true energy deposition (simIDE)
TH1D	h_DeltaE		Difference between K.E. calculated from trjPoint and simIDE for elastic scattering
TH1D	hCrossSection		Total Cross-Section [barn]
TH1D	hCrossSectionEl		Elastic Cross-Section [barn]
TH1D	hCrossSectionInel	Inelastic Cross-Section [barn]

There's a TTree as well. Interesting quantities there are:
finalKE         Kinetic Energy at last point
G4Process       Nature of the last point (elastic, inelastic, decay, throughgoing...)



3. Simply launch by
> python G4XSKaons.py
