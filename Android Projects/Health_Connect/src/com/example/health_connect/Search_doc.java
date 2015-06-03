package com.example.health_connect;

import java.util.ArrayList;
import java.util.List;

import com.parse.ParseException;
import com.parse.ParseObject;
import com.parse.ParseQuery;
import com.parse.ParseUser;

import android.os.Bundle;
import android.app.Activity;
import android.app.ProgressDialog;
import android.text.Editable;
import android.text.TextWatcher;
import android.util.Log;
import android.view.KeyEvent;
import android.view.Menu;
import android.view.View;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemClickListener;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.ListView;
import android.widget.ViewFlipper;

public class Search_doc extends Activity implements TextWatcher,
		OnItemClickListener {

	private static final int LIST_PIC_SCREEN = 0;
	private static final int VIEW_PIC_SCREEN = 1;

	private ArrayList<String>listPicName = new ArrayList<String>();

	private ArrayList<String> listPicType = new ArrayList<String>();
	private List<Integer> listPicDrawable = new ArrayList<Integer>();

	private ArrayList<Picture> listPic = new ArrayList<Picture>();
	private ListView listview;
	private PicListAdapter adapter;
	private EditText searchEdt;
	private ViewFlipper fliper;
	private ImageView viewpic;
	ProgressDialog mProgressDialog;
	List<ParseObject> objects;
	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.search_doc);
		Log.d("Error","in search_doc");
	/*	listPicName.add("icon");
		listPicName.add("pikachu");
		listPicName.add("apple");
		
		listPicType.add("android");
		listPicType.add("cartoon");
		listPicType.add("fruit");
		
		listPicDrawable.add(R.drawable.ic_launcher);
		listPicDrawable.add(R.drawable.pikachu);
		listPicDrawable.add(R.drawable.apple);
		*/
		
		
		ParseUser currentUser = ParseUser.getCurrentUser();
		if (currentUser!=null)
		{
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
			           		listPicName.add((String)r.get("ReportHeading"));
			           		listPicType.add((String)r.get("Subject"));
			           		listPicDrawable.add(R.drawable.pikachu);
			           		Log.d("Check", "in for parse");
			           	}
			}
			catch(ParseException e)
			{
				Log.d("Error", "Oh nooo..");
			    }
		}
		
		Log.d("Error","lists added");
		
		fliper = (ViewFlipper) findViewById(R.id.viewFlipper1);
		listview = (ListView) findViewById(R.id.listView1);
		for (int i = 0; i < listPicName.size(); i++) {
			Log.d("Error","for loop");
			Picture pic = new Picture(listPicName.get(i), listPicType.get(i),
					listPicDrawable.get(i));
			Log.d("Error","pic added");
			listPic.add(pic);
		}
		Log.d("Error","for exited");
		adapter = new PicListAdapter(this, listPic);
		Log.d("Error","returned from adapter");
		listview.setAdapter(adapter);
		Log.d("Error","in adapter");
		listview.setOnItemClickListener(this);
		Log.d("Error","exited adapter");
		searchEdt = (EditText) findViewById(R.id.serach_edt);
		searchEdt.addTextChangedListener(this);
		viewpic = (ImageView) findViewById(R.id.viewpic_img);
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

	/**
	 * @author 9Android.net
	 */
	public void beforeTextChanged(CharSequence s, int start, int count,
			int after) {
		// TODO Auto-generated method stub

	}

	public void onTextChanged(CharSequence s, int start, int before, int count) {
		// TODO Auto-generated method stub

	}

	public void afterTextChanged(Editable s) {
		// TODO Auto-generated method stub
		String text = searchEdt.getText().toString().toLowerCase();
		adapter.filter(text);
	}

	/**
	 *  @author 9Android.net
	 */
	public void onItemClick(AdapterView<?> parent, View view, int position,
			long id) {
		// TODO Auto-generated method stub
		Sliding.slideFromRightToLeft(VIEW_PIC_SCREEN, fliper);
		viewpic.setImageResource(listPic.get(position).getPicSource());

	}

	 
	public boolean onKeyDown(int keyCode, KeyEvent event) {

		if (keyCode == KeyEvent.KEYCODE_BACK) {
			int screen = fliper.getDisplayedChild();

			if (screen == VIEW_PIC_SCREEN) {
				Sliding.slideFromLeftToRight(LIST_PIC_SCREEN, fliper);
				return true;
			}
		}
		return super.onKeyDown(keyCode, event);
	}

}
