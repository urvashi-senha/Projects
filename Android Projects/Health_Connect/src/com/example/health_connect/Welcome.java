package com.example.health_connect;

import java.util.Timer;
import java.util.TimerTask;

import com.parse.Parse;
import com.parse.ParseAnalytics;
import com.parse.ParseUser;

import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.view.Menu;

public class Welcome extends Activity {
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.timer);
		

		if( getIntent().getBooleanExtra("Exit me", false)){
		       finish();
		       return; // add this to prevent from doing unnecessary stuffs
		   }
		
		Parse.initialize(this, "e0FVFRBMAWJi5shg4XF8zL3SIuRwDIufww3338so", "toTJmlHTEF43u7PoAFT4fedwqfhoWiSajj1Se7FT");
		ParseAnalytics.trackAppOpened(getIntent());

		final ParseUser currentUser = ParseUser.getCurrentUser();
		if (currentUser != null)
		{
			Intent intent2 = new Intent(Welcome.this,SwipeHome.class);
			startActivity(intent2);
		}
		Timer timer = new Timer();
		timer.schedule(new TimerTask() {

		   public void run() {

		      //here you can start your Activity B.
			   Intent intent= new Intent(Welcome.this, MainActivity.class);
	            startActivity(intent); 

		   }

		}, 2000);
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

}