void make_Track_QA_plots() {

	RooPlotLib rpl;
	Reporter rp( "rqa_Track.pdf", 500, 500 );

	TFile * f = new TFile( "setA_qa.root", "READ" );



	rpl.style( (TH1*)f->Get( "track_cuts" ) )
		.set( "title", "Track Cuts" )
		.set( "logy", 0 ).draw();
	rp.savePage();

	// TODO: same bins as corr RefMult for comparison
	// rpl.style( (TH1*)f->Get( "event_refMult" ) )
	// 	.set( "logy", 1 )
	// 	.set( "yr", 1, 1e4 )
	// 	.set( "title", "Raw refMult" ).draw();
	// rp.savePage();

	rpl.style( (TH1*)f->Get( "track_nHitsFit" ) )
		.set( "logy", 1 )
		.set( "title", "# HitsFit" ).draw();
	rp.savePage();

	rpl.style( (TH1*)f->Get( "track_nHitsDedx" ) )
		.set( "logy", 0 )
		.set( "title", "# Hits dEdx" ).draw();
	rp.savePage();

	rpl.style( (TH2*)f->Get( "track_nHitsFitOverPoss" ) )
		.set( "title", "# HitsFit / # Hits Possible" )
		.set( "draw", "col" )
		.draw();
	rp.savePage();

	rpl.style( (TH1*)f->Get( "track_ptRatio" ) )
		.set( "title", "pT Global / pT Primary" )
		.set( "logy", 1 )
		.set( "draw", "" )
		.draw();
	rp.savePage();

	rpl.style( (TH1*)f->Get( "track_dca" ) )
		.set( "title", "DCA; [cm]; dN/dDCA" )
		.set( "logy", 1 )
		.set( "draw", "" )
		.draw();
	rp.savePage();

	rpl.style( (TH2*)f->Get( "track_eta" ) )
		.set( "title", "#eta" )
		.set( "logy", 1 )
		.set( "draw", "" )
		.draw();
	rp.savePage();



}