void make_Event_QA_plots() {

	RooPlotLib rpl;
	Reporter rp( "rqa.pdf", 500, 500 );

	TFile * f = new TFile( "setA_qa.root", "READ" );



	rpl.style( (TH1*)f->Get( "event_cuts" ) )
		.set( "title", "Event Cuts" )
		.set( "logy", 0 ).draw();
	rp.savePage();

	// TODO: same bins as corr RefMult for comparison
	// rpl.style( (TH1*)f->Get( "event_refMult" ) )
	// 	.set( "logy", 1 )
	// 	.set( "yr", 1, 1e4 )
	// 	.set( "title", "Raw refMult" ).draw();
	// rp.savePage();

	rpl.style( (TH1*)f->Get( "event_corrRefMult" ) )
		.set( "logy", 1 )
		.set( "xr", 0, 400 )
		.set( "yr", 1, 1e4 )
		.set( "title", "Corrected refMult" ).draw();
	rp.savePage();

	rpl.style( (TH1*)f->Get( "event_refMultBins" ) )
		.set( "logy", 0 )
		.set( "title", "StRefMultCorr bin9" ).draw();
	rp.savePage();

	rpl.style( (TH2*)f->Get( "event_vX_vY" ) )
		.set( "title", "vX vs. vY; vX [cm]; vY[cm]" )
		.set( "draw", "col" )
		.draw();
	rp.savePage();

	rpl.style( (TH1*)f->Get( "event_vR" ) )
		.set( "yto", 1.3 )
		.set( "xto", 0.9 )
		.set( "title", "Radial Vertex;  (vX^{2} + vY^{2})^{1/2} [cm]; dN/dvR" )
		.set( "logy", 1 )
		.set( "draw", "" )
		.draw();
	rp.savePage();

	rpl.style( (TH1*)f->Get( "event_nTofMatchA" ) )
		.set( "yto", 1.3 )
		.set( "xto", 0.9 )
		.set( "title", "# TOF Matched Tracks; #TOF Matched Tracks; dN/dTOFMatch" )
		.set( "logy", 1 )
		.set( "draw", "" )
		.draw();
	rp.savePage();

	rpl.style( (TH2*)f->Get( "event_nTofMatchA_corrRefMult" ) )
		.set( "yto", 1.3 )
		.set( "xto", 0.9 )
		.set( "title", "# TOF Matched Tracks vs. Corrected RefMult; #TOF Matched Tracks; Corrected RefMult" )
		.set( "logy", 1 )
		.set( "logx", 1 )
		.set( "draw", "col" )
		.draw();
	rp.savePage();



}