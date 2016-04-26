
import rootpy.ROOT as R
R.gROOT.SetBatch(True)
from rootpy.io import root_open, DoesNotExist
from rootpy.plotting import Canvas, Hist, Legend
import rootpy.plotting.root2matplotlib as rplt
import matplotlib.pyplot as plt

def drawAll( m, c, eff = True ) :
    can = Canvas( width=600, height=3000 )
    pad = 2;
    can.Divide( 1, 6 )
    
    if ( eff ) :
        can.cd(pad)
        pad+=1
        yePi = f.tofEff.Get( "eff_Pi_"+m+"_"+c )
        yeK = f.tofEff.Get( "eff_K_"+m+"_"+c )
        yeP = f.tofEff.Get( "eff_P_"+m+"_"+c )

        yePi.Draw()
        yePi.SetTitle( "Fit Yields; P [GeV]; dN/(P dP)" )
        yePi.GetYaxis().SetRangeUser(  0.0, 1.7 )
        yeK.SetMarkerColor( R.kRed )
        yeK.Draw( "same")
        yeP.SetMarkerColor( R.kBlue )
        yeP.Draw("same")

    
    
    ############################################
    # zb mu
    can.cd(pad)
    pad+=1

    R.gPad.SetLogy(0)
    piMu = f.Pi_zbMu.Get( "mu_Pi_"+ m +"_" + c  )
    kMu = f.K_zbMu.Get( "mu_K_"+ m +"_" + c  )
    pMu = f.P_zbMu.Get( "mu_P_"+ m +"_" + c  )

    pidMu = f.Pi_zbMu.Get( "deltamu_Pi_"+ m +"_" + c ).Clone( "pisdmu" )
    kdMu = f.K_zbMu.Get( "deltamu_K_"+ m +"_" + c ).Clone( "ksdmu" )
    pdMu = f.P_zbMu.Get( "deltamu_P_"+ m +"_" + c ).Clone( "psdmu" )

    piMu.SetTitle( "<zb_{fit}> - <zb_{exp}>; P [GeV]" )
    R.gPad.SetLogy(0)
    piMu.GetYaxis().SetRangeUser( -0.2, 0.2)
    piMu.Draw()
    kMu.Draw("same")
    kMu.SetMarkerColor( R.kRed )
    pMu.Draw("same")
    pMu.SetMarkerColor( R.kBlue )

    pidMu.Scale(10);
    pidMu.SetMarkerStyle( R.kOpenCircle )
    pidMu.Draw("same")
    kdMu.Scale(10);
    kdMu.SetMarkerColor( R.kRed )
    kdMu.SetMarkerStyle( R.kOpenCircle )
    kdMu.Draw("same")
    pdMu.Scale(10);
    pdMu.SetMarkerColor( R.kBlue )
    pdMu.SetMarkerStyle( R.kOpenCircle )
    pdMu.Draw("same")



    #######################################################
    #zd mu
    try : 
        can.cd(pad)
        pad+=1
        R.gPad.SetLogy(0)
        piMu = f.Pi_zdMu.Get( "mu_Pi_"+ m +"_" + c )
        kMu = f.K_zdMu.Get( "mu_K_"+ m +"_" + c )
        pMu = f.P_zdMu.Get( "mu_P_"+ m +"_" + c )

        pidMu = f.Pi_zbMu.Get( "deltamu_Pi_"+ m +"_" + c ).Clone( "zdpisdmu" )
        kdMu = f.K_zbMu.Get( "deltamu_K_"+ m +"_" + c ).Clone( "zdksdmu" )
        pdMu = f.P_zbMu.Get( "deltamu_P_"+ m +"_" + c ).Clone( "zdpsdmu" )

        piMu.SetTitle( "<zd_{fit}> - <zd_{exp}>" )
        piMu.Draw()
        zdSig = 0.08
        piMu.GetYaxis().SetRangeUser( -zdSig * 5.0, zdSig * 5.0)
        kMu.Draw("same")
        kMu.SetMarkerColor( R.kRed )
        pMu.Draw("same")
        pMu.SetMarkerColor( R.kBlue )

        pidMu.Scale(10);
        pidMu.SetMarkerStyle( R.kOpenCircle )
        pidMu.Draw("same")
        kdMu.Scale(10);
        kdMu.SetMarkerColor( R.kRed )
        kdMu.SetMarkerStyle( R.kOpenCircle )
        kdMu.Draw("same")
        pdMu.Scale(10);
        pdMu.SetMarkerColor( R.kBlue )
        pdMu.SetMarkerStyle( R.kOpenCircle )
        pdMu.Draw("same")
    except :
        print "no"
    
    ##########################################################
    #zbSig
    try : 
        can.cd(pad)
        pad+=1
        R.gPad.SetLogy(0)
        piMu = f.Pi_zbSigma.Get( "sigma_Pi_"+ m +"_" + c  )
        kMu = f.K_zbSigma.Get( "sigma_K_"+ m +"_" + c )
        pMu = f.P_zbSigma.Get( "sigma_P_"+ m +"_" + c  )

        piMu.SetTitle( "#sigma zb_{fit}" )
        piMu.Draw()
        piMu.GetYaxis().SetRangeUser( 0.000, 0.055)
        kMu.Draw("same")
        kMu.SetMarkerColor( R.kRed )
        pMu.Draw("same")
        pMu.SetMarkerColor( R.kBlue )
        R.gPad.SetGrid(1, 1)
    except :
        print "no"
    
    ##########################################################
    #zdSig
    can.cd(pad)
    try :
        pad+=1
        R.gPad.SetLogy(0)
        piMu = f.Pi_zdSigma.Get( "sigma_Pi_"+ m +"_" + c  )
        kMu = f.K_zdSigma.Get( "sigma_K_"+ m +"_" + c  )
        pMu = f.P_zdSigma.Get( "sigma_P_"+ m +"_" + c  )

        piMu.SetTitle( "#sigma zd_{fit}" )
        piMu.Draw()
        piMu.GetYaxis().SetRangeUser( 0.0, 0.09)
        kMu.Draw("same")
        kMu.SetMarkerColor( R.kRed )
        pMu.Draw("same")
        pMu.SetMarkerColor( R.kBlue )
        R.gPad.SetGrid(1,1)
    except :
        print "no"
    
    ##########################################################
    #Yield
    can.cd(1)
    yPi = f.Pi_yield.Get( "yield_Pi_"+m+"_"+c )
    yK = f.K_yield.Get( "yield_K_"+m+"_"+c )
    yP = f.P_yield.Get( "yield_P_"+m+"_"+c )

    yPi.Draw()
    yPi.SetTitle( "Fit Yields; P [GeV]; dN/(P dP)" )
    yPi.GetYaxis().SetRangeUser( 1e-6, yPi.GetMaximum() *10 )
    yK.SetMarkerColor( R.kRed )
    yK.Draw( "same")
    yP.SetMarkerColor( R.kBlue )
    yP.Draw("same")
    R.gPad.SetLogy(1)
    return can