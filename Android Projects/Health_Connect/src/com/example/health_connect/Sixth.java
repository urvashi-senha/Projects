package com.example.health_connect;
import java.util.ArrayList;
import java.util.List;

import android.app.Activity;
import android.app.ProgressDialog;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;
import android.widget.ListView;
 
import com.parse.FindCallback;
import com.parse.GetDataCallback;
import com.parse.Parse;
import com.parse.ParseAnalytics;
import com.parse.ParseException;
import com.parse.ParseFile;
import com.parse.ParseObject;
import com.parse.ParseQuery;
import com.parse.ParseUser;
 
public class Sixth extends Activity {
	ListView listview;
    List<ParseObject> objects;
    ProgressDialog mProgressDialog;
    ListViewAdapter adapter;
    private List<Report> report_list = null;
    
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        // Get the view from listview_main.xml
        setContentView(R.layout.sixth);
        new RemoteDataTask().execute();
    }
    private class RemoteDataTask extends AsyncTask<Void, Void, Void> {
        @Override
        protected void onPreExecute() {
            super.onPreExecute();
            // Create a progressdialog
            mProgressDialog = new ProgressDialog(Sixth.this);
            // Set progressdialog title
            mProgressDialog.setTitle("Retrieving uploaded reports..");
            // Set progressdialog message
            mProgressDialog.setMessage("Loading...");
            mProgressDialog.setIndeterminate(false);
            // Show progressdialog
            mProgressDialog.show();
        }
 
        @Override
        protected Void doInBackground(Void... params) {
	//	Parse.initialize(this, "e0FVFRBMAWJi5shg4XF8zL3SIuRwDIufww3338so", "toTJmlHTEF43u7PoAFT4fedwqfhoWiSajj1Se7FT");
		ParseAnalytics.trackAppOpened(getIntent());
		ParseUser currentUser = ParseUser.getCurrentUser();
		if (currentUser!=null)
		{
			report_list= new ArrayList<Report>();
			try
			{
				ParseQuery<ParseObject> query = new ParseQuery<ParseObject>("FILES");
		    query.whereEqualTo("U_id",currentUser.getObjectId());
			//query.whereEqualTo("U_id","mEHyXC46y2");
		    query.orderByDescending("updatedAt");
		    objects = query.find();
		    		
			         	Log.d("Check", "here it is");
			           	for (ParseObject r : objects)
			           	{
			           	 ParseFile image = (ParseFile) r.get("file");
			           	//image.getDataInBackground(new GetDataCallback() {

			           	   // @Override
			           	  //  public void done(byte[] imageInBytes, ParseException pEx) {
			           	        // TODO Auto-generated method stub
			           	    //   Bitmap image = BitmapFactory.decodeByteArray(imageInBytes, 0, imageInBytes.length);
			           	    //}
			           //	});
			           	 Report re = new Report();
			           	 re.sethead((String) r.get("ReportHeading"));
			           	 re.setsub((String) r.get("Subject"));
			           	 re.setimag(image.getUrl());
			           	 report_list.add(re); 
			           	Log.d("Check1", "retrieved" + " " + r.getString("ReportHeading"));
			           	}
			}
			catch(ParseException e)
			{
				Log.d("Error", "Oh nooo..");
			    }
		}
		Log.d("Check3", "here it is");
		return null;
		}
        @Override
        protected void onPostExecute(Void result) {
    	Log.d("Check2", "here it is");
    	listview = (ListView) findViewById(R.id.listview); 
    	 adapter = new ListViewAdapter(Sixth.this,
                 report_list);
    	 listview.setAdapter(adapter);
    	 mProgressDialog.dismiss();
    }


    }
}
    
