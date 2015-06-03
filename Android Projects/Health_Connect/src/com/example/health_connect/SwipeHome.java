package com.example.health_connect;

import android.os.Bundle;

import java.io.File;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.List;

import com.parse.Parse;
import com.parse.ParseAnalytics;
import com.parse.ParseFile;
import com.parse.ParseObject;
import com.parse.ParseUser;

import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentActivity;
import android.support.v4.view.ViewPager;
import android.support.v4.view.ViewPager.OnPageChangeListener;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TabHost;
import android.widget.TextView;
import android.widget.Toast;
import android.widget.TabHost.OnTabChangeListener;

import android.app.Activity;
import android.content.Intent;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.View.OnClickListener;

public class SwipeHome extends FragmentActivity implements OnTabChangeListener, OnPageChangeListener {

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
	
	 MyPageAdapter pageAdapter;
	    private ViewPager mViewPager;
	    private TabHost mTabHost;
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.s_home);
		mViewPager = (ViewPager) findViewById(R.id.viewpager);
		
		 Parse.initialize(this, "e0FVFRBMAWJi5shg4XF8zL3SIuRwDIufww3338so", "toTJmlHTEF43u7PoAFT4fedwqfhoWiSajj1Se7FT");
			ParseAnalytics.trackAppOpened(getIntent());
			final ParseUser currentUser = ParseUser.getCurrentUser();
       // Tab Initialization
       initialiseTabHost();

       // Fragments and ViewPager Initialization
       List<Fragment> fragments = getFragments();
       pageAdapter = new MyPageAdapter(getSupportFragmentManager(), fragments);
       mViewPager.setAdapter(pageAdapter);
       mViewPager.setOnPageChangeListener(SwipeHome.this);
       
      
		//final ParseUser currentUser = ParseUser.getCurrentUser();
	/*	if (currentUser == null)
		{
			Intent intent = new Intent(SwipeHome.this, MainActivity.class);
			startActivity(intent);
		}
		*/
		

		
	}
	
	private static void AddTab(SwipeHome activity, TabHost tabHost, TabHost.TabSpec tabSpec) {
       tabSpec.setContent(new MyTabFactory(activity));
       tabHost.addTab(tabSpec);
   }

   // Manages the Tab changes, synchronizing it with Pages
   public void onTabChanged(String tag) {
       int pos = this.mTabHost.getCurrentTab();
       this.mViewPager.setCurrentItem(pos);
   }

   @Override
   public void onPageScrollStateChanged(int arg0) {
   }

   // Manages the Page changes, synchronizing it with Tabs
   @Override
   public void onPageScrolled(int arg0, float arg1, int arg2) {
       int pos = this.mViewPager.getCurrentItem();
       this.mTabHost.setCurrentTab(pos);
   }

   @Override
       public void onPageSelected(int arg0) {
   }

   private List<Fragment> getFragments(){
       List<Fragment> fList = new ArrayList<Fragment>();

       // TODO Put here your Fragments
       MySampleFragment f1 = MySampleFragment.newInstance("Sample Fragment 1");
       MySampleFragment1 f2 = MySampleFragment1.newInstance("Sample Fragment 2");
       MySampleFragment2 f3 = MySampleFragment2.newInstance("Sample Fragment 3");
       fList.add(f1);
       fList.add(f2);
       fList.add(f3);

       return fList;
   }

   // Tabs Creation
   private void initialiseTabHost() {
       mTabHost = (TabHost) findViewById(android.R.id.tabhost);
       mTabHost.setup();

       // TODO Put here your Tabs
       SwipeHome.AddTab(this, this.mTabHost, this.mTabHost.newTabSpec("VIEW").setIndicator("",getApplicationContext().getResources().getDrawable(R.drawable.view)));
       SwipeHome.AddTab(this, this.mTabHost, this.mTabHost.newTabSpec("EDIT").setIndicator("",getApplicationContext().getResources().getDrawable(R.drawable.edit)));
       SwipeHome.AddTab(this, this.mTabHost, this.mTabHost.newTabSpec("UPLOAD").setIndicator("",getApplicationContext().getResources().getDrawable(R.drawable.upload)));

       mTabHost.setOnTabChangedListener(this);
   }

   /*
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
	*/
	@Override
	public void onBackPressed() {
		// TODO Auto-generated method stub
	//	super.onBackPressed();
		Intent intent = new Intent(SwipeHome.this, Welcome.class);
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
	    		Intent intent = new Intent(SwipeHome.this,Welcome.class);
	    		intent.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);
	    	  //  intent.putExtra("Exit me", true);
				startActivity(intent);
				finish();
	    		return true;
	    	case R.id.file_a:
	    		Intent intent2 = new Intent(SwipeHome.this,Search_doc.class);
	    		startActivity(intent2);
	    		return true;
	    		
	    	default: 
	    		return super.onOptionsItemSelected(item);
	    	
	    	}
	    }
	    
		

}