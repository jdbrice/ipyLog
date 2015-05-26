## Notes on embedding efficiency

- Cut on GEANT id and plc charge


email to staratrice: 
Hi all,

I have a few questions about efficiencies calculated from embedding. Here is a quick outline of my method with the questions in context:

1. Apply the same event cuts(excluding trigger) as my analysis

2. Q: Should I correct the reference multiplicity for the embedded data using StRefMultCorr or should I use the reference multiplicity as provided? 

3. For filling the denominator - ie total MC tracks  
  - require the GEANT id to be equal to the plc of interest ( ie 8 for pi+ )  
  - require that plc's charge be equal to the charge of interest ( ie +1 for pi plus )
  - Fill histogram to count tracks in bins of pt, y, centrality ( using ptMc, and y calculated from Mc p, pZ )
  
4.  For filling the numerator ( tracks that pass cuts )
  - Require that tracks pass your analysis track cuts ( eg nHitsFit > 15, nHitsDedx > 10 etc. )
  - Fill histogram to count tracks in bins of pt, y, centrality 
  - Q : Should I use the MC values or the reconstructed values of pt, y? I expect that I should use the reconstructed values - but for low statistics this allows the possibility of the efficiency to be greater than 1 in cases when tracks get reconstructed with the wrong momentum and end up in the wrong bin with respect to its MC counterpart. 
  - Q : Should I require that the reconstructed track have the correct charge? ( I think yes since this is know even in the "real" data )

5. Use the TGraphAsymmErrors to calculate the efficiencies with Bayesian uncertainties ie TGraphAsymmErrors::BayesDivide(...)

Feedback on these points would be helpful, and if you suspect I am missing an important step / cut etc. please also correct me in that.

Thanks,
Daniel 