package com.example.hackathon;

import com.parse.Parse;
import com.parse.ParseAnalytics;
import com.parse.ParseException;
import com.parse.ParseUser;
import com.parse.SignUpCallback;

import android.app.Activity;
import android.app.ProgressDialog;
import android.content.Intent;
import android.os.Bundle;
import android.text.TextUtils;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class Second extends Activity {
	
protected ProgressDialog proDialog;
	
	
	protected void startLoading() {
	    proDialog = new ProgressDialog(this);
	    proDialog.setMessage("loading...");
	    proDialog.setProgressStyle(ProgressDialog.STYLE_SPINNER);
	    proDialog.setCancelable(false);
	    proDialog.show();
	}

	protected void stopLoading() {
	    proDialog.dismiss();
	    proDialog = null;
	}
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		// TODO Auto-generated method stub
		super.onCreate(savedInstanceState);
		setContentView(R.layout.second);
		Parse.initialize(this, "Q41kE80rWOGz6khmLdhvMPSZd5CJL1YUw35ro9ht", "FaZ2FwBQj8fGCaPblg7T7o6qRX0HwHZNtqIydC68");
		ParseAnalytics.trackAppOpened(getIntent());
		
		Button b = (Button) findViewById(R.id.register);
		b.setOnClickListener(new OnClickListener() {
			
			@Override
			public void onClick(View v) {
				
				// TODO Auto-generated method stub
				EditText name = (EditText) findViewById(R.id.name);
				EditText pass = (EditText) findViewById(R.id.password);
				EditText bd = (EditText) findViewById(R.id.emailid);
				EditText place = (EditText) findViewById(R.id.place);
				EditText eid = (EditText) findViewById(R.id.voterid);
				if( TextUtils.isEmpty(place.getText().toString()) || TextUtils.isEmpty(name.getText().toString()) ||  TextUtils.isEmpty(eid.getText().toString())  || TextUtils.isEmpty(bd.getText().toString()) || TextUtils.isEmpty(pass.getText().toString()))
				{
					
					Log.d("Check", "Invalid");
					TextView tv = (TextView) findViewById(R.id.error);
					tv.setText("Invalid Input");
				//	tv.setText(name.getText().toString());
				}
				else
				{
					Log.d("Check", "Reached in else part");
					ParseUser user = new ParseUser();
					if(!name.getText().toString().equalsIgnoreCase("admin"))
					{
						user.setUsername(name.getText().toString());
					
					user.setPassword(pass.getText().toString());
					user.setEmail(bd.getText().toString());
					 
					// other fields can be set just like with ParseObject
					user.put("Place", place.getText().toString());
					user.put("Voter_id", eid.getText().toString());
					startLoading(); 
					user.signUpInBackground(new SignUpCallback() {
					  public void done(ParseException e) {
					    if (e == null) {
					      Log.d("Check","Hooray! Let them use the app now.");
					      stopLoading();
			              finish();
					      Intent intent = new Intent(Second.this, SwipeHome.class);
						  startActivity(intent);
					    } 
					    else {
					    	stopLoading();
					    	 Log.d("Check","NO");
					    	 Log.d("Check", "NOOO", e);
					    	// e.getCode();
					      // Sign up didn't succeed. Look at the ParseException
					      // to figure out what went wrong
					    }
					  }
					  }
					);
					}	
				}                 // end of else
			}
		});

	}

}
