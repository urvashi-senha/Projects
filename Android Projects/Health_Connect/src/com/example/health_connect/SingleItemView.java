package com.example.health_connect;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.widget.ImageView;
import android.widget.TextView;

public class SingleItemView extends Activity{
	
	    String heading;
	    String subject;
	    String image;
	    
	    ImageLoader imageLoader = new ImageLoader(this);

	    
	    @Override
	    public void onCreate(Bundle savedInstanceState) {
	        super.onCreate(savedInstanceState);
	        Log.d("check11","in singleitem class");
	        // Get the view from singleitemview.xml
	        setContentView(R.layout.singleitemview);
	 
	        Log.d("Check8", "here it is in single item view starting intent");
	        Intent i = getIntent();
	       
	        heading = i.getStringExtra("heading");
	        subject = i.getStringExtra("subject");
	        image = i.getStringExtra("image");
	        
	        TextView txthead = (TextView) findViewById(R.id.headtxt);
	        TextView txtsub = (TextView) findViewById(R.id.subtxt);
	     
	        ImageView img = (ImageView) findViewById(R.id.imag);
	        
	        txthead.setText(heading);
	        txtsub.setText(subject);
	        imageLoader.DisplayImage(image, img);
	        Log.d("Check6", "settext and setimage");
}
}