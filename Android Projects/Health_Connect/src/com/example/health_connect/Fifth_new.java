package com.example.health_connect;

import java.util.ArrayList;
import java.util.List;
import java.text.Format;
import com.parse.CountCallback;
import com.parse.FindCallback;
import com.parse.GetCallback;
import com.parse.Parse;
import com.parse.ParseAnalytics;
import com.parse.GetDataCallback;
import com.parse.ParseException;
import com.parse.ParseObject;
import com.parse.ParseQuery;
import com.parse.ParseUser;

import android.os.Bundle;
import android.app.Activity;
import android.util.Log;
import android.view.Menu;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.TextView;

public class Fifth_new extends Activity {

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		ListView lv;
		setContentView(R.layout.fifth_new);
		
		Parse.initialize(this, "e0FVFRBMAWJi5shg4XF8zL3SIuRwDIufww3338so", "toTJmlHTEF43u7PoAFT4fedwqfhoWiSajj1Se7FT");
		ParseAnalytics.trackAppOpened(getIntent());
		ParseUser currentUser = ParseUser.getCurrentUser();
		if (currentUser!=null)
		{	
		final TextView text1 = (TextView) findViewById(R.id.headtxt);
		final TextView text2 = (TextView) findViewById(R.id.subtxt);
	//	final TextView text3 = (TextView) findViewById(R.id.textView3);
		lv = (ListView) findViewById(R.id.listView1);
		final ArrayList<String> report_list = new ArrayList<String>();
	//	final ArrayList<String> subject_list = new ArrayList<String>();
		    ParseQuery<ParseObject> query = ParseQuery.getQuery("FILES");
		    query.whereEqualTo("U_id",currentUser.getObjectId());
		    query.orderByDescending("updatedAt");
		    query.findInBackground(new FindCallback<ParseObject>(){
		    public void done(List<ParseObject> objects, ParseException e) {
		         if (e == null){ 
		        	
		        	 Log.d("Check", "here it is");
		        	  for (int i=0;i< objects.size();i++) {
		        	      
		        	 String report = objects.get(i).getString("ReportHeading");
		        	 String subject = objects.get(i).getString("Subject");
		        	 Log.d("Check",report+" "+subject);
		        	 text1.setText(report);
		        	 text2.setText(subject);
		        	 report_list.add(report);
		        	 report_list.add(subject);
		        	  }
		         }
		         
		         else {
		        	 text2.setText("here");
		         }
   		    }
		    });
		    
		    
		ArrayAdapter<String> arrayAdapter =      
		         new ArrayAdapter<String>(this,android.R.layout.activity_list_item, report_list);
		         lv.setAdapter(arrayAdapter); 
		}	}   

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

}
//ParseFile image = (ParseFile) aParseObject.get("photp");
//image.getDataInBackground(new GetDataCallback() {

  //  @Override
   // public void done(byte[] imageInBytes, ParseException pEx) {
        // TODO Auto-generated method stub
     //   bmp = BitmapFactory.decodeByteArray(imageInBytes, 0, imageInBytes.length);
    //}
//});
