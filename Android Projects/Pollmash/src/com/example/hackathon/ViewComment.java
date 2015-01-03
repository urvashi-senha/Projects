package com.example.hackathon;

import java.util.ArrayList;
import java.util.List;




import com.parse.Parse;
import com.parse.ParseException;
import com.parse.ParseObject;
import com.parse.ParseQuery;
import com.parse.ParseUser;

import android.os.Bundle;
import android.app.Activity;
import android.app.ProgressDialog;
import android.util.Log;
import android.view.Menu;
import android.view.View;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemClickListener;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.ViewFlipper;

public class ViewComment extends Activity implements OnItemClickListener {

protected ProgressDialog proDialog;
private static final int LIST_PIC_SCREEN = 0;
private static final int VIEW_PIC_SCREEN = 1;
private ArrayList<String>listPicContent = new ArrayList<String>();
private ArrayList<String> listPicBy = new ArrayList<String>();
private ArrayList<Comments> listPic = new ArrayList<Comments>();
ParseUser currentUser;
ListView listView ;
List<ParseObject> objects;
private CommentPicAdapter adapter;
private ViewFlipper fliper;
private TextView viewname;
private TextView viewby;
	
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
		Parse.initialize(this, "Q41kE80rWOGz6khmLdhvMPSZd5CJL1YUw35ro9ht", "FaZ2FwBQj8fGCaPblg7T7o6qRX0HwHZNtqIydC68");
		// ParseAnalytics.trackAppOpened(getIntent());
		super.onCreate(savedInstanceState);
		setContentView(R.layout.view_comment);
		currentUser = ParseUser.getCurrentUser();
		final String s_user_name;
		final String s_user_id;
		s_user_id = getIntent().getStringExtra("Id");
		s_user_name = getIntent().getStringExtra("name");
		Log.d("ERRRORRR","IN COMMENT");
		Log.d("Check!!!!","here");
		ParseQuery<ParseObject> query = new ParseQuery<ParseObject>("Posts");
		query.whereEqualTo("for",s_user_name);

		
		
		try
		{
			objects = query.find();
			for(ParseObject r : objects)
			{
				
				listPicContent.add((String)r.get("Content"));
				Log.d("check!!!!", "add");
				listPicBy.add((String)r.get("By"));
				

			}
		}
		catch (ParseException e) 
		{
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		fliper = (ViewFlipper) findViewById(R.id.viewFlipper);
		listView = (ListView) findViewById(R.id.listView);
		listPic.clear();

		for (int i = 0; i < listPicContent.size(); i++) {
			Log.d("Error","for loop");
			Comments pic = new Comments(listPicContent.get(i), listPicBy.get(i));
			Log.d("Error","pic added");
			listPic.add(pic);
		}
		adapter = new CommentPicAdapter(this, listPic);
		listView.setAdapter(adapter);
		Log.d("Error","in adapter");
		listView.setOnItemClickListener(this);
	
		
	}
	
	public boolean onCreateOptionsMenu(Menu menu) {
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

	@Override
	public void onItemClick(AdapterView<?> arg0, View arg1, int arg2, long arg3) {
		// TODO Auto-generated method stub
		
	}

}
