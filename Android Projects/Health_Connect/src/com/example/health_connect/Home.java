package com.example.health_connect;

import java.io.File;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Arrays;
import java.util.Calendar;

import com.parse.Parse;
import com.parse.ParseAnalytics;
import com.parse.ParseFile;
import com.parse.ParseObject;
import com.parse.ParseUser;



import android.os.Bundle;
import android.app.Activity;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TabHost;
import android.widget.TextView;
import android.widget.Toast;
import android.widget.TabHost.TabSpec;
import android.content.Intent;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.View.OnClickListener;


public class Home extends Activity implements OnClickListener{
	
	private static final int REQUEST_PICK_FILE = 1;

    private TextView mFilePathTextView;
    private Button mStartActivityButton;
    private File selectedFile;
    
    
    
    @Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.home, menu);
		return true;
	}
    
    public void MessageBox(String message)
    {
       Toast.makeText(this, message, Toast.LENGTH_SHORT).show();
    } 

    
	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.home);
		
		Parse.initialize(this, "e0FVFRBMAWJi5shg4XF8zL3SIuRwDIufww3338so", "toTJmlHTEF43u7PoAFT4fedwqfhoWiSajj1Se7FT");
		ParseAnalytics.trackAppOpened(getIntent());
		final ParseUser currentUser = ParseUser.getCurrentUser();
		if (currentUser == null)
		{
			Intent intent = new Intent(Home.this, MainActivity.class);
			startActivity(intent);
		}
		
		
		
		TabHost tabHost=(TabHost)findViewById(R.id.tabhost);
		tabHost.setup();

		TabSpec spec1=tabHost.newTabSpec("VIEW");
		spec1.setContent(R.id.VIEW);
		spec1.setIndicator("VIEW");

		TabSpec spec2=tabHost.newTabSpec("EDIT");
		spec2.setIndicator("EDIT");
		spec2.setContent(R.id.EDIT);

		TabSpec spec3=tabHost.newTabSpec("UPLOAD");
		spec3.setIndicator("UPLOAD");
		spec3.setContent(R.id.UPLOAD);

		tabHost.addTab(spec1);
		tabHost.addTab(spec2);
		tabHost.addTab(spec3);
		
		/*
		
		Button urv = (Button) findViewById(R.id.button3);
		urv.setOnClickListener(new OnClickListener() {
			
			@Override
			public void onClick(View v) {
				// TODO Auto-generated method stub
			
				Intent iii = new Intent(Home.this,Fifth_new.class);
				startActivity(iii);
			}
		});
		
		
		*/
		
		ImageView birthdaypic = (ImageView) findViewById(R.id.imageView2);
		TextView wish = (TextView) findViewById(R.id.textView23);
		TextView hbday = (TextView) findViewById(R.id.textView24);
		
		String date_of_birth = currentUser.getString("Dob");
		
		Calendar c = Calendar.getInstance();
		SimpleDateFormat df = new SimpleDateFormat("dd/MM/yyyy");
		String formattedDate = df.format(c.getTime());
		//Log.d("Check",formattedDate);

		
		if( (formattedDate.substring(0,2).equalsIgnoreCase(date_of_birth.substring(0,2))) && (formattedDate.substring(3,5).equalsIgnoreCase( date_of_birth.substring(3,5))) )
	//	if(d1==d2 && m1==m2)
		{		
			
		}
		else
		{
		//	Log.d("Check", d1);
			birthdaypic.setImageDrawable(null);
			wish.setText(null);
			hbday.setText(null);
			wish.setVisibility(View.GONE);
			hbday.setVisibility(View.GONE);
		}
		
		
		TextView a_name = (TextView) findViewById(R.id.textView6);
		TextView a_eid = (TextView) findViewById(R.id.textView8);
		TextView a_nat = (TextView) findViewById(R.id.textView10);
		TextView a_dob = (TextView) findViewById(R.id.textView12);
		TextView a_w = (TextView) findViewById(R.id.textView14);
		TextView a_h = (TextView) findViewById(R.id.textView16);
		TextView a_bg = (TextView) findViewById(R.id.textView18);
		TextView a_fname = (TextView) findViewById(R.id.textView20);
		TextView a_da = (TextView) findViewById(R.id.textView22);
		
		
		TextView a_na = (TextView) findViewById(R.id.na);
		TextView a_ei = (TextView) findViewById(R.id.ei);
		
		
		a_na.setText(currentUser.getUsername());
		a_ei.setText(currentUser.getEmail());
		
		a_name.setText(currentUser.getUsername());
		a_bg.setText(currentUser.getString("BG"));
		a_dob.setText(currentUser.getString("Dob"));
		a_fname.setText(currentUser.getString("Fname"));
		a_h.setText(currentUser.getString("Height"));
		a_nat.setText(currentUser.getString("Nation"));
		a_w.setText(currentUser.getString("Weight"));
		a_eid.setText(currentUser.getEmail());
		a_da.setText(currentUser.getString("DA"));

//		EditText e_name = (EditText) findViewById(R.id.editText1);
//		EditText e_eid = (EditText) findViewById(R.id.editText2);
		final EditText e_nat = (EditText) findViewById(R.id.editText3);
		final EditText e_dob = (EditText) findViewById(R.id.editText4);
		final EditText e_w = (EditText) findViewById(R.id.editText5);
		final EditText e_h = (EditText) findViewById(R.id.editText6);
		final EditText e_bg = (EditText) findViewById(R.id.editText7);
		final EditText e_fname = (EditText) findViewById(R.id.editText8);
		final EditText e_da = (EditText) findViewById(R.id.editText9);
		
	//	e_name.setText(currentUser.getUsername());
		e_bg.setText(currentUser.getString("BG"));
		e_dob.setText(currentUser.getString("Dob"));
		e_fname.setText(currentUser.getString("Fname"));
		e_h.setText(currentUser.getString("Height"));
		e_nat.setText(currentUser.getString("Nation"));
		e_w.setText(currentUser.getString("Weight"));
	//	e_eid.setText(currentUser.getEmail());
		e_da.setText(currentUser.getString("DA"));
		
		Button sz = (Button) findViewById(R.id.save);
		sz.setOnClickListener(new OnClickListener() {
			
			@Override
			public void onClick(View v) {
				// TODO Auto-generated method stub
				currentUser.put("BG", e_bg.getText().toString());
				currentUser.put("Dob", e_dob.getText().toString());
				currentUser.put("Fname", e_fname.getText().toString());
				currentUser.put("Height", e_h.getText().toString());
				currentUser.put("Nation", e_nat.getText().toString());
				currentUser.put("Weight", e_w.getText().toString());
				currentUser.put("DA", e_da.getText().toString());
				currentUser.saveInBackground();
				MessageBox("Changes Saved");
				Intent i2= new Intent(Home.this,Home.class);
				startActivity(i2);
			}
		});
		
		
		mFilePathTextView = (TextView)findViewById(R.id.textView4);
	    mStartActivityButton = (Button)findViewById(R.id.button1);
	    mStartActivityButton.setOnClickListener(this);
	}
	
	public void onClick(View v) {
		switch(v.getId()) {
        case R.id.button1:
            // Create a new Intent for the file picker activity
            Intent intent = new Intent(this, FilePickerActivity.class);

            // Set the initial directory to be the sdcard
            //intent.putExtra(FilePickerActivity.EXTRA_FILE_PATH, Environment.getExternalStorageDirectory());

            // Show hidden files
            //intent.putExtra(FilePickerActivity.EXTRA_SHOW_HIDDEN_FILES, true);

            // Only make .png files visible
            //ArrayList<String> extensions = new ArrayList<String>();
            //extensions.add(".png");
            //intent.putExtra(FilePickerActivity.EXTRA_ACCEPTED_FILE_EXTENSIONS, extensions);

            // Start the activity
            startActivityForResult(intent, REQUEST_PICK_FILE);
            break;
            }

        //case R.id.You_can_handle_more_onclick_events_from_here:
            //Do something
        //    break;
		
	}
	
	@Override
	public void onBackPressed() {
		// TODO Auto-generated method stub
	//	super.onBackPressed();
		Intent intent = new Intent(Home.this, MainActivity.class);
		intent.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);
		intent.putExtra("Exit me", true);
		startActivity(intent);
		finish();
		
	}
	
	
	 @Override
	    public boolean onOptionsItemSelected(MenuItem item) {
	    	
	    	switch(item.getItemId())
	    	{
	    	case R.id.logout : 
	    		Log.i("Check","LOGOUT");
	    		Parse.initialize(this, "e0FVFRBMAWJi5shg4XF8zL3SIuRwDIufww3338so", "toTJmlHTEF43u7PoAFT4fedwqfhoWiSajj1Se7FT");
	    		ParseAnalytics.trackAppOpened(getIntent());
	    		ParseUser.logOut();
	    		Intent intent = new Intent(Home.this, MainActivity.class);
	    		intent.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);
	    	  //  intent.putExtra("Exit me", true);
				startActivity(intent);
				finish();
	    		return true;
	    		
	    	default: 
	    		return super.onOptionsItemSelected(item);
	    	
	    	}
	    }
	    
	
	
	
	
	
	
	
	
	
	
	protected void onActivityResult(int requestCode, int resultCode, Intent data) {
		       if(resultCode == RESULT_OK) {
		           switch(requestCode) {
		            case REQUEST_PICK_FILE:
		                if(data.hasExtra(FilePickerActivity.EXTRA_FILE_PATH)) {
		                    // Get the file path
		                    selectedFile = new File(data.getStringExtra(FilePickerActivity.EXTRA_FILE_PATH));
		                    // Set the file path text view
		                    mFilePathTextView.setText(selectedFile.getPath());  
		                    //Now you have your selected file, You can do your additional requirement with file.                
		                    final ParseUser currentUser = ParseUser.getCurrentUser();
		                    if (currentUser == null)
		            		{
		            			Intent intent = new Intent(Home.this, MainActivity.class);
		            			startActivity(intent);
		            		}
		                    
		                    Button bt = (Button) findViewById(R.id.button2);
		                    bt.setOnClickListener(new OnClickListener() {
								
								@Override
								public void onClick(View v) {
									// TODO Auto-generated method stub
									
									
									byte[] dat = "Working at Parse is great!".getBytes();
				                    ParseFile fil = new ParseFile(mFilePathTextView.getText().toString(), dat);
				                    fil.saveInBackground();
				                    EditText sub = (EditText) findViewById(R.id.sub);
				                    EditText rep = (EditText) findViewById(R.id.head);
				              //      currentUser.put("Subject",sub.getText().toString());
				                //    currentUser.put("ReportHeading",rep.getText().toString());
				            		
				                    ParseObject f = new ParseObject("FILES");
				                    f.put("file", fil);
				                    f.put("Subject",sub.getText().toString());
				                    f.put("ReportHeading",rep.getText().toString());
				                    f.put("U_id", currentUser.getObjectId());
				             //       currentUser.put("FILE_h",fil);
				                    
				            
				                    
				                    f.saveInBackground();
									mFilePathTextView.setText("Done !!");
									MessageBox("File Successfully Uploaded");
									Intent intent = new Intent(Home.this, Home.class);
			            			startActivity(intent);
									
								}
							});
		                    
		                    
		                    
		              
		                }
		            }
		        }
		    }
		}