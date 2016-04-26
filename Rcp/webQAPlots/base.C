
TFile * hFile = nullptr;

void setColors(){
	cout << "Setting Colors" << endl;
    const Int_t NRGBs = 5;
    const Int_t NCont = 255;

    Double_t stops[NRGBs] = { 0.00, 0.34, 0.61, 0.84, 1.00 };
    Double_t red[NRGBs]   = { 0.00, 0.00, 0.87, 1.00, 0.51 };
    Double_t green[NRGBs] = { 0.00, 0.81, 1.00, 0.20, 0.00 };
    Double_t blue[NRGBs]  = { 0.51, 1.00, 0.12, 0.00, 0.00 };
    TColor::CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont);
    gStyle->SetNumberContours(NCont);
}

TH1D * get1D( string name ){
	if ( nullptr != hFile ){
		return (TH1D*)hFile->Get( name.c_str() );
	} 
	return nullptr;
}

TH2D * get2D( string name ){
	if ( nullptr != hFile ){
		return (TH2D*)hFile->Get( name.c_str() );
	} 
	return nullptr;
}


void vLine( TH1 * h, double x, int color = kRed, int width = 2 ){
	line = new TLine( x, h->GetYaxis()->GetXmin(), x, h->GetYaxis()->GetXmax() );
	line->SetLineColor( color );
	line->SetLineWidth( width );
	line->Draw("same");
}

void hLine( TH1 * h, double y, int color = kRed, int width = 2 ){
	line = new TLine( h->GetXaxis()->GetXmin(), y, h->GetXaxis()->GetXmax(), y );
	line->SetLineColor( color );
	line->SetLineWidth( width );
	line->Draw("same");
}


void topLeft( TPaveStats* s ){
	s->SetX1NDC( 0.1 );
	s->SetX2NDC( 0.4 );
	s->SetY1NDC( 0.7 );
	s->SetY2NDC( 0.9 );
}

void bottomRight( TPaveStats* s ){
	s->SetX1NDC( 0.6 );
	s->SetX2NDC( 0.9 );
	s->SetY1NDC( 0.1 );
	s->SetY2NDC( 0.3 );
}

void topRight( TPaveStats* s ){
	s->SetX1NDC( 0.6 );
	s->SetX2NDC( 0.9 );
	s->SetY1NDC( 0.7 );
	s->SetY2NDC( 0.9 );
}